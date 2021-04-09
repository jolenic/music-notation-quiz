# Defines Question class - prompt (question / picture) and answer
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        self.response = ""
