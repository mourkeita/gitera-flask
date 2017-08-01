#! /usr/bin/python
# coding: utf8

import os

class Config(object):
	DEBUG = False
	CSRF_ENABLED = True
	SECRET = os.getenv('SECRET')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	DEBUG = True

class StagingConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	DEBUG = False

app_config = {
	'testing' : TestingConfig,
	'production' : ProductionConfig,
	'staging' : StagingConfig,
	'development' : DevelopmentConfig
}