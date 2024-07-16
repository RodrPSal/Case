import sys
import os

import pytest

# Adiciona o diretório pai ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../flask_app')))

from flask_app.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()