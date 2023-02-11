from config import openai


def create_image(Prompt, Quantity: int = 1, Size: str = "1024x1024"):
    generation_response = openai.Image.create(
        prompt=Prompt,
        n=Quantity,
        size=Size,
        response_format="url",
    )
    variation_urls = [datum["url"] for datum in generation_response["data"]]
    return variation_urls
