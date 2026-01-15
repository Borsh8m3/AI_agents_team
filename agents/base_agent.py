import asyncio
import websockets
import json
from endpoint import Endpoint
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Mapowanie nazw agentów na indeksy kluczy
AGENT_KEY_MAP = {
    "Developer": 0,
    "Planner": 1,
    "Reviewer": 2,
    "Tester": 3, 
}

class BaseAgent(Endpoint):
    KLUCZE_API = []
    licznik_rotacji = {}
        
    def __init__(self, name, server_url="ws://localhost:8765"):
        load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
        if not BaseAgent.KLUCZE_API:
            BaseAgent.KLUCZE_API = [
                str(os.getenv("API_KEY_1")).strip(),
                str(os.getenv("API_KEY_2")).strip(),
                str(os.getenv("API_KEY_3")).strip(),
                str(os.getenv("API_KEY_4")).strip(),
            ]
        
        if name not in BaseAgent.licznik_rotacji:
            if name in AGENT_KEY_MAP:
                BaseAgent.licznik_rotacji[name] = AGENT_KEY_MAP[name]
            else:
                BaseAgent.licznik_rotacji[name] = 0
        
        self.name = name
        self.model = self.get_model()
        
        super().__init__(name, server_url)

    def get_model(self):
        indeks = BaseAgent.licznik_rotacji.get(self.name, 0)
        obecny_klucz = BaseAgent.KLUCZE_API[indeks % len(BaseAgent.KLUCZE_API)]
        
        BaseAgent.licznik_rotacji[self.name] = (indeks + 1)
        
        genai.configure(api_key=obecny_klucz)
        
        print(f"[{self.name}] Używa Klucza numer {(indeks % len(BaseAgent.KLUCZE_API)) + 1}")
        return genai.GenerativeModel('gemini-2.5-flash')