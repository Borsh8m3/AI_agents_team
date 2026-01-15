import asyncio
import websockets
import json
from base_agent import BaseAgent 

class Tester(BaseAgent):
    def getResponse(self, message, message1):
        self.model = self.get_model()
        
        print("Odebrałem kod.\nRozpoczynam analizę pod kątem błędów.\n\n")

        prompt = f"""
        Jesteś Ekspertem QA i Automatyzacji Testów (Senior QA Automation Engineer).

        ### TWOJE ZADANIE:
        Przeanalizuj poniższy kod Python i napisz testy jednostkowe w bibliotece unittest,
        które weryfikują poprawność jego działania.

        ### ZASADY OGÓLNE:
        1. Generuj WYŁĄCZNIE kod Python.
        2. Nie dodawaj żadnych opisów, komentarzy wyjaśniających ani bloków Markdown.
        3. Testy mają być możliwie proste, czytelne i bez nadmiernej komplikacji.
        4. Nie używaj mocków, jeśli nie są absolutnie konieczne.

        ### WYMAGANIA DOTYCZĄCE TESTÓW:
        1. Dla KAŻDEJ klasy zdefiniowanej w kodzie utwórz osobny zestaw testów.
        2. Każdy zestaw testów traktuj jako osobny plik testowy.
        3. Testy powinny obejmować:
        - przypadki poprawne,
        - przypadki brzegowe,
        - typowe błędy użycia.

        ### WYMAGANIA DOTYCZĄCE FORMATOWANIA (BARDZO WAŻNE):
        1. Pierwsza linia odpowiedzi MUSI wyglądać dokładnie tak: ### test_{message}
        2. Bezpośrednio pod nią umieść kod.
        3. NIE używaj bloków Markdown (nie stosuj ```).
        4. Zwróć WYŁĄCZNIE kod – bez wyjaśnień, opisów ani komentarzy poza kodem.

        ### KOD DO PRZETESTOWANIA:
        {message}
        """


        response = self.model.generate_content(prompt)
        response = response.text.replace("```python", "").replace("```", "").strip()
        
        print(f"\n")
        print(f"Testy zakończone. Wysyłam testy jednostkowe do Reviewera.")
        return response


if __name__ == "__main__":
    tester = Tester(name="Tester")
    asyncio.run(tester.run())
