import asyncio
import websockets
import json
from endpoint import Endpoint
import os
import google.generativeai as genai
from dotenv import load_dotenv

class BaseAgent(Endpoint):
    KLUCZE_API = []
    licznik_rotacji = 0
        
    def __init__(self, name, server_url="ws://localhost:8765"):
        load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
        self.KLUCZE_API.append(str(os.getenv("API_KEY_1")).strip())
        self.KLUCZE_API.append(str(os.getenv("API_KEY_2")).strip())
        self.model = self.get_model()
        
        super().__init__(name, server_url)

    def get_model(self):
        indeks = self.licznik_rotacji % 2
        obecny_klucz = self.KLUCZE_API[indeks]
        self.licznik_rotacji += 1
        
        genai.configure(api_key=obecny_klucz)
        
        print(f"Używa Klucza nr {indeks + 1}")
        return genai.GenerativeModel('gemini-2.5-flash')