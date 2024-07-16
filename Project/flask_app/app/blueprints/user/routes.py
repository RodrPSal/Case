from flask import make_response, request, session
from app.blueprints.user import bp
from app.services.userService import UserService

@bp.route('/login', methods=["POST"])
def login():
    if 'name' not in request.json:
        return make_response("Nome não informado", 400)

    if 'password' not in request.json:
        return make_response("Senha não informada", 400)

    name = request.json['name']
    password = request.json['password']

    userService = UserService()

    try:
        operationResult = userService.loginUser(name, password)

        if(operationResult.success):
            session["userId"] = operationResult.returnValue
            return make_response("Usuário logado com sucesso!", 200)
        else:
            return make_response("Usuário não encontrado", 401)
    except:
        return make_response("Erro ao realizar o login", 500)

@bp.route('/create', methods=["POST"])
def createUser():

    if 'name' not in request.json:
        return make_response("Nome não informado", 400)

    if 'password' not in request.json:
        return make_response("Senha não informada", 400)

    name = request.json['name']
    password = request.json['password']

    userService = UserService()

    # try:
    operationResult = userService.insertUser(name, password)

    if(operationResult.success):
        return make_response(str(operationResult.returnValue), 200)
    else:
        return make_response(operationResult.message, 400)
    # except:
    #     return make_response("Erro ao criar usuário", 500)