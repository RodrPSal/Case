from flask import jsonify, make_response, request, session
from app.blueprints.main import bp
from app.services.suggestionService import SuggestionService
from app.services.userService import UserService

@bp.route('/suggestionFromPrompt', methods=["POST"])
def suggestionFromPrompt():
    
    if "userId" not in session:
        return make_response("Usuário não autenticado", 401)

    suggestionService = SuggestionService()

    userId = session["userId"]

    try:
        data = request.json['data']
        try:
            return make_response(
                    jsonify({
                        "response": suggestionService.getSuggestionWithMessage(data, userId),
                        "userId": userId
                    }), 200
                )
        except:
            return make_response("Erro ao tentar gerar uma sugestão", 500)
    except KeyError:
        return make_response("O prompt precisa ser informado", 400)
    except:
        return make_response("Erro desconhecido", 400)
    
@bp.route('/dailySuggestion')
def dailySuggestion():

    suggestionService = SuggestionService()

    try:
        return make_response(jsonify(suggestionService.getDailySugestion()), 200)
    except:
        return make_response("Erro ao tentar gerar uma sugestão", 500)
    
@bp.route('/getHistory/<int:userId>')
def getHistory(userId):

    suggestionService = SuggestionService()

    try:
        response = suggestionService.getMessageHistory(userId)
        return make_response(jsonify({
                "messages": response.returnValue
            }), 200)
    except:
        return make_response("Erro ao buscar histórico", 500)