import os
import connexion
import pytest


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("FLASK_DEBUG", "true")
    openapi_spec_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "openapi"))
    app = connexion.FlaskApp(__name__, specification_dir=openapi_spec_path)
    app.add_api("talking_clock_api.yaml", strict_validation=True, validate_responses=True)
    app.app.config["TESTING"] = True
    client = app.app.test_client()
    yield client