import asyncio
import websockets
import json
from base_agent import BaseAgent

class Developer(BaseAgent):
    def getResponse(self, message1, message2):
        print(f"Przyjąłem zadanie: {message2}. Mam zrobić plik: {message1}. Rozpoczynam kodowanie.")
        
        prompt = f"Napisz kompletny, działający kod w Pythonie dla pliku: {message1}. Tylko kod, bez bloków markdown."
        response = self.model.generate_content(prompt)
        # print(response.text)
        # kod = response.text.replace("```python", "").replace("```", "").strip()
        
        # print("Kod napisany. Przekazuję do Testera.")
        return response.text

if __name__ == "__main__":
    developer = Developer(name="Developer")
    asyncio.run(developer.run())
