import pytest

from app import create_app, db
from config import TestConfig


@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig())
    with app.app_context():
        yield app


@pytest.fixture
def _db(app):
    # Make sure this is actually the testing database
    assert db.engine.url.drivername == "sqlite"
    assert db.engine.url.database.endswith("/testing.sqlite")
    db.drop_all()

    db.create_all()

    return db


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument("--headless")
    return firefox_options


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless")
    return chrome_options
