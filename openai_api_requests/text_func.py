from config import openai


def create_text(Prompt, Temperature: float = 0.5, MaxLength: int = 100):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=Prompt,
        temperature=Temperature,
        max_tokens=MaxLength
    )
    return response["choices"][0]["text"]
