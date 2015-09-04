import os

def is_development() :
	mode = os.getenv("MODE", "prod")
	return mode == "dev"

DEBUG = is_development()
