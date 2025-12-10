import asyncio
import websockets
import json
from agents.base_agent import BaseAgent 

class Tester(BaseAgent):
    def getResponse(self, message1, message2):
        print("Odebrałem kod. Rozpoczynam analizę pod kątem błędów.")
        
        prompt = (
            "Przeanalizuj poniższy kod Python. Napisz testy jednostkowe (Unittest), aby sprawdzić jego poprawność. Tylko kod, bez bloków markdown.\n"
            f"KOD:\n{message1}"
        )
        response = self.model.generate_content(prompt)
        response = response.text.replace("```python", "").replace("```", "").strip()

        print(f"Testy zakończone. Wysyłam testy jednostkowe do Reviewera.")
        return response


if __name__ == "__main__":
    tester = Tester(name="Tester")
    asyncio.run(tester.run())
