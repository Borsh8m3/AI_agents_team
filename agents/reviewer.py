import asyncio
import websockets
import json
from base_agent import BaseAgent 

class Reviewer(BaseAgent):
    def getResponse(self, message, message1):
        self.model = self.get_model()
        
        print(f"Odebrałem raport Testera. Wdrażam poprawki.")

        prompt = f"""
                Jesteś doświadczonym Senior Python Developerem odpowiedzialnym za Code Review i poprawki błędów.
                Twoim zadaniem jest refaktoryzacja i naprawa dostarczonego kodu na podstawie wyników testów.

                ### INSTRUKCJE:
                1. Przeanalizuj poniższe uwagi z testów/feedbacku.
                2. Zastosuj wszystkie niezbędne poprawki w kodzie źródłowym.
                3. Upewnij się, że kod jest zgodny ze standardami PEP8, czysty i czytelny.
                4. Zwróć **kompletny**, poprawiony kod (nie używaj skrótów typu "...", wypisz całość).

                ### UWAGI Z TESTÓW:
                {message}

                ### KOD ŹRÓDŁOWY:
                {message1}

                Twoja odpowiedź powinna zawierać WYŁĄCZNIE blok kodu z ostateczną wersją.
                """

        response = self.model.generate_content(prompt)
        
        kod_finalny = response.text.replace("```python", "").replace("```", "").strip()
        
        print("Poprawki naniesione. Kod gotowy do zapisu.")
        return kod_finalny

if __name__ == "__main__":
    reviewer = Reviewer(name="Reviewer")
    asyncio.run(reviewer.run())
