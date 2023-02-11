from config import openai


def create_code(Prompt, Temperature: float = 0.0, MaxLength: int = 100):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=Prompt,
        temperature=Temperature,
        max_tokens=MaxLength,
        top_p=1,
    )
    return response["choices"][0]["text"]
