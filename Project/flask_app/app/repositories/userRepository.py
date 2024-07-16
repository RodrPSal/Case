from app.models.result import Result
from app.models.user import User

class UserRepository():

    def __init__(self, db):
        self.db = db

    def getUserFromId(self, id):
        foundUser = User.query.filter_by(id = id).first()

        if(foundUser):
            return Result(True, foundUser.isPremium)
        else:
            return Result(False)

    def getUserFromCredentials(self, name, password):
        foundUser = User.query.filter_by(name=name, password = password).first()

        if(foundUser):
            return Result(True, foundUser.id)
        else:
            return Result(False)
        
    def createUser(self, name, password):
        newUser = User(name, password)
        
        if(newUser.isValid()):
            self.db.session.add(newUser)
            self.db.session.commit()
            return Result(True, newUser.id)
        else:
            return Result(False, message = "Parâmetros informados não são válidos")