import os


class Config:
    DEBUG = os.getenv("FLASK_DEBUG", True)
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
