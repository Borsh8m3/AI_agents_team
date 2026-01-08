import asyncio
import websockets
import json

from base_agent import BaseAgent 

class Tester(BaseAgent):
    def getResponse(self, message1, message2):
        print("Odebrałem kod.\nRozpoczynam analizę pod kątem błędów.\n\n")
        
        prompt = (
            "Jesteś Ekspertem QA i Automatyzacji Testów (Senior QA Automation Engineer)."
            "Przeanalizuj poniższy kod Python. Napisz testy jednostkowe (Unittest), aby sprawdzić jego poprawność. Tylko kod, bez bloków markdown."
            f"KOD:\n{message1}"
            "Dla każdej z klas stwórz osobne testy"
            "Tworząc testy na samym początku pliku wstaw trzy znaki hasz i nazwe pliku według wzoru '### test_nazwa.py' odpowiadające nazwie klasy, która będzie testowana"
        )
        response = self.model.generate_content(prompt)
        response = response.text.replace("```python", "").replace("```", "").strip()
        
        print(f"\n")
        print(f"Testy zakończone. Wysyłam testy jednostkowe do Reviewera.")
        return response


if __name__ == "__main__":
    tester = Tester(name="Tester")
    asyncio.run(tester.run())
