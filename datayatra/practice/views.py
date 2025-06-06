from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
import markdown
import os
from django.http import Http404
from .utils import markdown_to_html
from .utils import checktestcase
from .models import Question, Submisson

def index(request):
    """
    Render the index page of the practice app.
    """
    # get question by id from database
    # question = get_object_or_404(Question, pk="0002_some_patients")
    # # get markdown file path from question model
    # print(question.get_markdown_path())
    filepath = os.path.join("./practice/questions/0002_some_patients/question.md")
    print(f"Loading question from: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    question_description = markdown_to_html(md_text)
    context = {'question_description': question_description}
    return render(request, 'practice/index.html', context)


def run_code(request):
    if request.method == "POST":
        user_input = request.POST.get("user_code")
        is_ordered = False
        tc_filepath = "./practice/questions/0002_some_patients/testcases.json"
        with open(tc_filepath, 'r', encoding='utf-8') as f:
            test_cases = json.load(f)
        with connection.cursor() as cursor:
            #execute test case setup
            setup_qry = test_cases[0]['setup']
            print(f"Executing setup query: {setup_qry}")
            for qry in setup_qry:
                if not qry.strip():
                    continue

                cursor.execute(qry)

            # Execute user input query
            print(f"Executing user input query...")
            cursor.execute(user_input)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            user_op = [dict(zip(columns, row)) for row in result]
            # Test case query execution
            print("Executing test case query...")
            cursor.execute(test_cases[0]['query'])
            tc_result = cursor.fetchall()
            tc_columns = [desc[0] for desc in cursor.description]
            tc_op = [dict(zip(tc_columns, row)) for row in tc_result]
        
        print("Checking test case...")
        
        if user_op == tc_op and is_ordered == True:
            print("Test case passed.")
            status = {"status": "success", "message": "Test case passed."}
        elif sorted(result) == sorted(tc_result) and columns == tc_columns and is_ordered == False:
            print("Test case passed.")
            status = {"status": "success", "message": "Test case passed."}
        else:
            print("Test case failed.")
            status = {"status": "error", "message": "Test case failed."}
        
        context = {"result": result, "columns": columns,
                   "tc_result": tc_result, "tc_columns": tc_columns,
                   "status": status}
        return JsonResponse(context)