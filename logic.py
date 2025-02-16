import requests
from collections import defaultdict
from translate import Translator

questions = {
    'как тебя зовут': "Я супер-крутой-бот и мое предназначение помогать тебе!",
    "сколько тебе лет": "Это слишком философский вопрос"
}

class TextAnalysis:
    memory = defaultdict(list)
    
    def __init__(self, text, owner):
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")
        self.response = self.get_answer()
        
        if self.text.lower() in questions.keys():
            self.response = questions[self.text.lower()]
        else:
            self.response = self.get_answer()
        
        TextAnalysis.memory[owner].append(self)

    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang, to_lang)
            translated_text = translator.translate(text)
            return translated_text
        except Exception as e:
            return f"Перевод не удался: {e}"
