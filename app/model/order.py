from datetime import date, datetime
from flask import jsonify
from app.database import Database


class Orders(Database):
    """Initialize order attributes"""

    def __init__(self):
        """initializing constructor"""
        super().__init__(self)