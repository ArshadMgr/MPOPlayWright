from MPOPlayWright.Payload.ai_helper import generate_test_input

prompt = "Generate a realistic username for testing login functionality."
username = generate_test_input(prompt)
print(f"Generated Username: {username}")
