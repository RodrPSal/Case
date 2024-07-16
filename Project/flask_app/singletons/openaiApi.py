import os
from openai import OpenAI
from enums.modelType import ModelType
from singletons.prompt import prompt
from singletons.singleton import SingletonMeta

class OpenAiApi(metaclass=SingletonMeta):

    modelstr = {
        ModelType.GPT3: "gpt-3.5-turbo",
        ModelType.GPT4: "gpt-4-turbo"
    }

    def __init__(self):
        self.client = OpenAI(
        api_key=os.environ.get("OPEN_AI_KEY")
    )

    def requestWithMessage(self, message, model = ModelType.GPT3):

        model_str = self.modelstr[model]

        completion = self.client.chat.completions.create(
            model = model_str,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message}
            ]
        )

        return completion.choices[0].message.content
    
    def requestWithHistory(self, userMessages, systemMessages, model = ModelType.GPT3):

        #O usuário tem que ter pelo menos uma mensagem a mais do que o sistema
        if(len(userMessages) <= len(systemMessages)):
            return -1 

        model_str = self.modelstr[model]

        requestMessages = []

        for idx in range(len(userMessages)):
            requestMessages.add({"role": "user", "content": userMessages[idx]})

            if(idx < len(requestMessages)):
                requestMessages.add({"role": "system", "content": systemMessages[idx]})

        userMessages

        completion = self.client.chat.completions.create(
            model = model_str,
            messages=requestMessages
        )

        return completion.choices[0].message.content