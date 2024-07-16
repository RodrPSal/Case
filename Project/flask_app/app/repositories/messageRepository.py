from app.models.result import Result
from app.models.message import Message

class MessageRepository():

    def __init__(self, db):
        self.db = db

    def getMessagesFromUserId(self, userId):
        foundMessages = Message.query.filter_by(userId = userId).all()

        if(foundMessages is not None):
            return Result(True, list({"userMessage":foundMessage.userMessage, "systemMessage":foundMessage.systemMessage} for foundMessage in foundMessages))
        else:
            return Result(False)
        
    def insertMessage(self, userId, userMessage, systemMessage):
        newMessage = Message(userId, userMessage, systemMessage)
        
        if(newMessage.isValid()):
            self.db.session.add(newMessage)
            self.db.session.commit()
            return Result(True, newMessage.id)
        else:
            return Result(False, message = "Parâmetros informados não são válidos")