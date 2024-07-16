import responses

def test_daily_suggestion(client):
    response = client.get("/dailySuggestion")

    assert b"Sugestao" in response.data

def test_request_without_login(client):
    response = client.post("/suggestionFromPrompt", json = {"data": "Qual ração dara para Golden?"})

    assert response.status_code == 401

@responses.activate
def test_suggestion_api(client):
    responses.add(
        responses.GET,
        "https://platform.openai.com/",
        json={"response":"String de resposta"},
        status=200
    )

    newUserName = "Usuario"
    newUserPassword = 1234

    client.post("/user/create", json = {"name": newUserName, "password": newUserPassword})
    client.post("/user/login", json = {"name": newUserName, "password": newUserPassword})
    response = client.post("/suggestionFromPrompt", json = {"data": "Qual ração dara para Golden?"})

    assert response.status_code == 200