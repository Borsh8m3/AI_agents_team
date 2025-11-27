import asyncio
import websockets
import json
from base_agent import BaseAgent
import ast

class Planer(BaseAgent):

    def getResponse(self, message1, message2):
        prompt = (
            f"Jesteś Senior Architectem. Twoim celem jest: {message2}. "
            "Wypisz TYLKO listę nazw plików Python, które są potrzebne do zrealizowania tego celu. "
            "Format: ['plik1.py', 'plik2.py']. Nie dodawaj żadnego innego tekstu."
        )

        response = self.model.generate_content(prompt)
        tekst_odpowiedzi = response.text.strip()
        print("Tekst odpowiedzi:::::::::::::::::::::::::::::::::::")
        print(tekst_odpowiedzi)
        try:
            start = tekst_odpowiedzi.find('[')
            end = tekst_odpowiedzi.rfind(']') + 1
            if start != -1 and end != 0:
                czysta_lista = tekst_odpowiedzi[start:end]
                lista_zadan = ast.literal_eval(czysta_lista)
            else:
                lista_zadan = ["main_script.py"]
                
            print(f"Plan gotowy. Przekazuję {len(lista_zadan)} zadań do zespołu.")
            return lista_zadan
            
        except Exception as e:
            print(f"Błąd parsowania planu: {e}. Zwracam domyślne zadanie.")
            return ["app.py"]

if __name__ == "__main__":
    planner = Planer(name="Planner")
    asyncio.run(planner.run())
 