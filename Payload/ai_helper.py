import openai
print("OpenAI version:", openai.__version__)  # Add this line to check the version
openai.api_key = 'sk-proj-2kbNnKptafPXAOPVutipT3BlbkFJ53R7fkITzK0pj2Pr5I7m'

def generate_test_input(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  # Update from engine to model
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
