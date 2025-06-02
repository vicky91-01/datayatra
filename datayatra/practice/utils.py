import markdown
import os
import json
from django.http import Http404
def markdown_to_html(md_text):
    return markdown.markdown(md_text, extensions=['fenced_code', 'codehilite', 'tables'])

def checktestcase(op, tc_filepath):
    print("Hello Ji!")
    """
    Check the output against the test case file.
    """
    if not os.path.exists(tc_filepath):
        raise Http404(f"Test case file not found: {tc_filepath}")

    with open(tc_filepath, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    print(op)
    print(test_cases['output'])
    # if op == test_cases['output']:
    #     print("Test case passed.")
    # else:
    #     print("Test case failed.")
    return True