from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# create function that receive text string try to use one of imported module to translate text return transleted text
# def translate(text):
#     # check if text is empty
#     if not text:
#         return "Please enter a valid text"
#     # check if text is in arabic or not
#     if single_detection(text) == "ar":
#         # if text is in arabic use google translator to translate it to english
#         translator = GoogleTranslator()
#         translation = translator.translate(text, dest='en')
#         return translation
#     else:
#         # if text is not in arabic use google translator to translate it to arabic
#         translator = GoogleTranslator()
#         translation = translator.translate(text, dest='ar')
#         return translation
#
# # create function that receive text string try to use one of imported module to detect language of text return language name
# def detect(text):
#     # check if text is empty
#     if not text:
#         return "Please enter a valid text"
#     # use single_detection function from deep_translator to detect language of text
#     language = single_detection(text)
#     return language
