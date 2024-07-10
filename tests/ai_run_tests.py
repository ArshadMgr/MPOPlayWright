import openai
import subprocess

import pytest

# Set your OpenAI API key
openai.api_key = ''

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_test(test_path):
    try:
        result = subprocess.run(['pytest', test_path, '-v'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running tests:\n{e.output}"

def run_multiple_tests(test_cases):
    results = []
    for test_case in test_cases:
        print(f"Running test case: {test_case}")
        result = run_test(test_case)
        results.append(result)
        print(f"Test Results for {test_case}:\n{result}\n")

    return results

if __name__ == '__main__':
    test_case1 = [
        "C:/Users/Arshad Mehmood/OneDrive - Riphah International University/Desktop/ArshadMgr/MPOPlayWright/tests/test_example.py",  # Adjust paths as needed

    ]
    test_case2 = [
        "C:/Users/Arshad Mehmood/OneDrive - Riphah International University/Desktop/ArshadMgr/MPOPlayWright/tests/test_EE.py",

    ]

    while True:
        user_message = input("You: ")

        if user_message.lower() in ['exit', 'quit']:
            break

        # Get response from ChatGPT
        gpt_response = chat_with_gpt(user_message)
        print(f"ChatGPT: {gpt_response}")

        # Check if the message asks to run tests
        if "run example test" in user_message.lower():
            test_results = run_multiple_tests(test_case1)
            print(f"Overall Test Results:\n{test_results}")
        # Check if the message asks to run tests
        if "run employee test" in user_message.lower():
            test_results = run_multiple_tests(test_case2)
            print(f"Overall Test Results:\n{test_results}")
