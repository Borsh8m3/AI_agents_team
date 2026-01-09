import asyncio
import websockets
import json

from base_agent import BaseAgent 


class Developer(BaseAgent):
    def getResponse(self, message1, message2):
         
        print(f"\nPrzyjąłem zadanie: {message2}.\nMam zrobić plik: {message1}.\n\nRozpoczynam kodowanie...\n\n")
        
        prompt = (
            "Jesteś Senior Python Developerem. Zajmujesz się pisaniem klas na podstawie kompletnych instrukcji."
            f"Napisz kompletny, działający kod w Pythonie dla pliku: {message1}."
            "Na samym początku pliku wstaw trzy znaki hasz i nazwe pliku według wzoru '### nazwa.py'"
            "Następnie przygotuj tylko kod, bez innych bloków markdown pośród kodu." 
            f"Tu jest treśc zadania: {message2}"
        )
        response = self.model.generate_content(prompt)
        # print(response.text)
        response = response.text.replace("```python", "").replace("```", "").strip()
        
        # print("Kod napisany. Przekazuję do Testera.")
        return response

if __name__ == "__main__":
    developer = Developer(name="Developer")
    asyncio.run(developer.run())
