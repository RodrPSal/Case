from app.repositories.userRepository import UserRepository
from app.extensions import db
from enums.userPermissions import UserPermission

class UserService():

    def __init__(self):
        self.userRepository = UserRepository(db)

    def loginUser(self, name, password): 
        return self.userRepository.getUserFromCredentials(name, password)
    
    def userIsPremium(self, userId):
        result = self.userRepository.getUserFromId(userId)    
        return result.returnValue == UserPermission.Premium.value
    
    def insertUser(self, name, password): 
        return self.userRepository.createUser(name, password)