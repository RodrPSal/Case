from flask_app.app.models.user import User

def test_invalid_parameters(client):
    newUserName = "Nome"
    newUserPassword = 12

    response = client.post("/user/create", json = {"name": newUserName, "password": newUserPassword})

    assert response.status_code == 400

def test_missing_parameters(client):
    response = client.post("/user/create", json = {"name": "Nome"})
    assert response.status_code == 400

    response = client.post("/user/create", json = {"password": "Nome"})
    assert response.status_code == 400

def test_signup(client, app):

    newUserName = "Usuario"
    newUserPassword = 1234

    response = client.post("/user/create", json = {"name": newUserName, "password": newUserPassword})

    assert response.status_code == 200

    with app.app_context():
        assert User.query.first().name == newUserName
        assert User.query.first().password == str(newUserPassword)

def test_login(client):
    newUserName = "Usuario"
    newUserPassword = 1234

    client.post("/user/create", json = {"name": newUserName, "password": newUserPassword})

    response = client.post("/user/login", json = {"name": newUserName, "password": newUserPassword})

    assert response.status_code == 200

def test_invalid_login(client, app):
    userName = "Usuario Inexistente"
    password = 123456789

    response = client.post("/user/login", json = {"name": userName, "password": password})

    assert response.status_code == 401