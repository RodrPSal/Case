from app.extensions import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    userMessage = db.Column(db.String(300))
    systemMessage = db.Column(db.String(1000))

    __table_args__ = {'extend_existing': True}

    def __init__(self, userId, userMessage, systemMessage):
        self.userId = userId
        self.userMessage = userMessage
        self.systemMessage = systemMessage
    
    def isValid(self):
        if(len(self.userMessage) > 300):
            return False
        
        if(len(self.systemMessage) > 1000):
            return False
        
        return True