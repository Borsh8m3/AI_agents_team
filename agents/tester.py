import asyncio
import websockets
import json
from base_agent import BaseAgent

class Tester(BaseAgent):
    def getResponse(self, message1, message2):
        print("Odebrałem kod. Rozpoczynam analizę pod kątem błędów.")
        
        prompt = (
            "Przeanalizuj poniższy kod Python. Napisz testy jednostkowe (Unittest), aby sprawdzić jego poprawność. Tylko kod, bez bloków markdown.\n"            f"Zadanie do wykonania: {message2}\n"
            f"KOD:\n{message1}"
        )
        response = self.model.generate_content(prompt)
        
        print(f"Testy zakończone. Wysyłam testy jednostkowe do Reviewera.")
        return response.text


if __name__ == "__main__":
    tester = Tester(name="Tester")
    asyncio.run(tester.run())
