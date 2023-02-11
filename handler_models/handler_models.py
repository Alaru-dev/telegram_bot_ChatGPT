from dataclasses import dataclass

from aiogram import types


@dataclass
class ImageSettings:
    Prompt: str = ""
    Size: str = "1024x1024"
    Quantity: int = 1

    def to_dict(self):
        return {"Prompt": self.Prompt, "Size": self.Size, "Quantity": self.Quantity}

    def str_get_settings(self):
        return f"\n\nPre-set image settings:\n- image quantity: {self.Quantity}\n- size: {self.Size}"


@dataclass
class TextSettings:
    Prompt: str = ""
    Temperature: float = 0.5
    MaxLength: int = 200

    def to_dict(self):
        return {"Prompt": self.Prompt, "Temperature": self.Temperature, "MaxLength": self.MaxLength}

    def str_get_settings(self):
        return f"\n\nPre-set text settings:\n- max length: {self.MaxLength}\n- temperature: {self.Temperature}"


@dataclass
class CodeSettings:
    Prompt: str = ""
    Temperature: float = 0.0
    MaxLength: int = 100

    def to_dict(self):
        return {"Prompt": self.Prompt, "Temperature": self.Temperature, "MaxLength": self.MaxLength}

    def str_get_settings(self):
        return f"\n\nPre-set code settings:\n- max length: {self.MaxLength}\n- temperature: {self.Temperature}"


@dataclass
class User:
    image_settings = ImageSettings()
    text_settings = TextSettings()
    code_settings = CodeSettings()
    message: types.Message
    inline_mess_id: int

    def to_dict(self):
        return {
            "image_settings": self.image_settings.to_dict(),
            "text_settings": self.text_settings.to_dict(),
            "code_settings": self.text_settings.to_dict()
        }


Users = dict()


@dataclass
class Flags:
    image_set_size = 0
    image_set_quantity = 0
    text_set_temperature = 0
    text_set_max_length = 0
    code_set_temperature = 0
    code_set_max_length = 0
    set_image_prompt = 0
    set_text_prompt = 0
    set_code_prompt = 0


#{"message_id": 77,
# "from": {
    # "id": 489195902,
    # "is_bot": false,
    # "first_name": "Roman",
    # "last_name": "Poberezhnyi",
    # "username": "Alaru",
    # "language_code": "en"},
# "chat": {
    # "id": 489195902,
    # "first_name": "Roman",
    # "last_name": "Poberezhnyi",
    # "username": "Alaru",
    # "type": "private"},
# "date": 1675881180,
# "text": "/start",
# "entities": [{
    # "type": "bot_command",
    # "offset": 0,
    # "length": 6}
# ]}

