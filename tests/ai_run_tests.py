import openai
import subprocess

# Set your OpenAI API key
openai.api_key = 'sk-proj-HWRMZntMLEoEhJDpFUwxT3BlbkFJ5SR7RCq17HPrlRGaaqJ8'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # or the model you are using
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_tests():
    test_path = "/MPOPlayWright/tests/test_example.py"
    result = subprocess.run(['pytest', test_path, '-v'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    while True:
        user_message = input("You: ")

        if user_message.lower() in ['exit', 'quit']:
            break

        # Get response from ChatGPT
        gpt_response = chat_with_gpt(user_message)
        print(f"ChatGPT: {gpt_response}")

        # Check if the message asks to run tests
        if "run my tests" in user_message.lower():
            test_results = run_tests()
            print(f"Test Results:\n{test_results}")

