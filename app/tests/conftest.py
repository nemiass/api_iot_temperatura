import pytest
from app import create_app
from app.db import db


class TestCofig:
    # local
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:@localhost:3306/iot_temperatura_test"
    )

    SQLALCHEMY_ECHO = False
    HOW_SQLALCHEMY_LOG_MESSAGES = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    ERROR_404_HELP = False


config = {"testConfig": TestCofig}


# @pytest.fixture(scope="module")
# def app():
#     app = create_app(config)
#     yield app


@pytest.fixture(scope="module")
def test_client():
    app = create_app(config["testConfig"])

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.session.remove()
            db.drop_all()


# @pytest.fixture(scope="module")
# def init_database():
#     db.create_all()
#     yield
#     db.drop_all()
