from app.services.userService import UserService
from enums.modelType import ModelType
from app.repositories.messageRepository import MessageRepository
from app.extensions import db
from singletons.openaiApi import OpenAiApi

class SuggestionService():

    def __init__(self):
        self.api = OpenAiApi() 

    def getSuggestionWithMessage(self, message, userId):
        
        userService = UserService()

        isPremiumUser = userService.userIsPremium(userId)

        model = ModelType.GPT4 if isPremiumUser else ModelType.GPT3

        systemMessage = self.api.requestWithMessage(message, model)

        messageRepository = MessageRepository(db)
        messageRepository.insertMessage(userId, message, systemMessage)

        return systemMessage

    def getDailySugestion(self):
        
        dailySugestionPrompt = "Cite uma sugestao para uma pessoa que tem um cachorro"

        return "Sugestao: " + self.api.requestWithMessage(dailySugestionPrompt)
    
    def getMessageHistory(self, userId):
        
        messageRepository = MessageRepository(db)

        return messageRepository.getMessagesFromUserId(userId)