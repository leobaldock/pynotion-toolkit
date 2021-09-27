from os import getenv
import json
from typing import Any, List
import requests
from .constants import BASE_URL

class Notion():
    def __init__(self, secret:str=None):
        self._secret = secret if secret is not None else getenv("NOTION_SECRET")
        self.headers = {
            "Authorization": f"Bearer {self.secret}", 
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }