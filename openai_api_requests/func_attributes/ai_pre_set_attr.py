from enum import Enum

max_image_quantity = 10


class ImageSize(Enum):
    Size_256x256 = "256x256"
    Size_512x512 = "512x512"
    Size_1024x1024 = "1024x1024"


class Temperature(Enum):
    temp_01 = 0.1
    temp_02 = 0.2
    temp_03 = 0.3
    temp_04 = 0.4
    temp_05 = 0.5
    temp_06 = 0.6
    temp_07 = 0.7
    temp_08 = 0.8
    temp_09 = 0.9
    temp_1 = 1


class MaxLength(Enum):
    length_100 = 100
    length_200 = 200
    length_300 = 300
    length_400 = 400
    length_500 = 500
    length_600 = 600
    length_700 = 700
    length_800 = 800
    length_900 = 900
    length_1000 = 1000
