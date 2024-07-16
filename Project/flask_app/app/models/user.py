from app.extensions import db
from enums.userPermissions import UserPermission

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    isPremium = db.Column(db.Integer)

    __table_args__ = {'extend_existing': True}

    def __init__(self, name, password):
        self.name = name
        self.password = password

        if(name == "admin"):
            self.isPremium = UserPermission.Premium.value
        else:
            self.isPremium = UserPermission.Free.value
    
    def isValid(self):
        if any(char.isdigit() for char in self.name):
            return False
        
        if len(str(self.password)) < 3:
            return False

        return True