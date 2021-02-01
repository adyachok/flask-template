import os


class DefaultConfig:
    APPLICATION_ROOT = '/'


class ProductionConfig(DefaultConfig):
    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


def get_config_object():
    if os.getenv('PRODUCTION_ENV') in ['True', 'true']:
        return 'config.ProductionConfig'
    return 'config.DevelopmentConfig'
