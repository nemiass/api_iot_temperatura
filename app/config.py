class DevCofig:
    # local
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/iot_temperatura"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    ERROR_404_HELP = False


config = {"devConfig": DevCofig}
