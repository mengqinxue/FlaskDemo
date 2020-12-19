class Config:
    ENV = 'env'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class TestConfig(Config):
    ENV = 'test'
    DEBUG = False

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False