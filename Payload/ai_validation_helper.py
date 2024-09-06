import openai

openai.api_key = 'sk-proj-HWRMZntMLEoEhJDpFUwxT3BlbkFJ5SR7RCq17HPrlRGaaqJ8'


def validate_with_openai(data_type, data_value):
    prompt = f"Validate the following {data_type}: {data_value}.\nIs this a valid {data_type}? Reply with 'valid' or 'invalid'."

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=10
    )

    validation_result = response.choices[0].text.strip().lower()
    return validation_result == 'valid'
