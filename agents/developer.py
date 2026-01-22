import asyncio
import websockets
import json
from base_agent import BaseAgent 

class Developer(BaseAgent):
    def getResponse(self, message, message1):
        self.model = self.get_model()
         
        print(f"\nPrzyjąłem zadanie: {message1}.\nMam zrobić plik: {message}.\n\nRozpoczynam kodowanie...\n\n")
        
        prompt = f"""
        Jesteś Senior Python Developerem, ekspertem w pisaniu prostego, czytelnego i niezawodnego kodu.
        Twoim priorytetem jest klarowność, minimalizm i poprawność – unikaj zbędnej abstrakcji.

        ### TWOJE ZADANIE:
        Napisz kompletny, działający kod w Pythonie dla pliku: {message}
        na podstawie dostarczonej specyfikacji.

        ### ZASADY PROJEKTOWE:
        1. Wybieraj najprostsze możliwe rozwiązania, które spełniają wymagania.
        2. Nie wprowadzaj wzorców projektowych ani dodatkowych warstw, jeśli nie są konieczne.
        3. Nie przewiduj przyszłych rozszerzeń – implementuj tylko to, co wynika ze specyfikacji.
        4. Jeśli coś da się zrobić w jednej klasie lub funkcji, nie dziel tego na kilka.
        5. Nie twórz kodu, który wymaga użycia żadnych dodatkowych zdjęć, fontów ani inncyh zasobów. 
        6. Pisz po polsku.


        ### WYMAGANIA DOTYCZĄCE KODU:
        1. Kod musi być kompletny i gotowy do uruchomienia (wszystkie importy, klasy, funkcje).
        2. Stosuj type hinting oraz docstringi dla klas i kluczowych metod.
        3. Przestrzegaj standardu PEP8.
        4. Kod powinien być czytelny i łatwy do przetestowania.

        ### WYMAGANIA DOTYCZĄCE FORMATOWANIA (BARDZO WAŻNE):
        1. Na samym początku pliku wstaw trzy znaki hasz i nazwe pliku według wzoru '### nazwa.py'
        2. Bezpośrednio pod nią umieść kod.
        3. NIE używaj bloków Markdown (nie stosuj ```).
        4. Zwróć WYŁĄCZNIE kod – bez wyjaśnień, opisów ani komentarzy poza kodem.

        ### TREŚĆ ZADANIA (SPECYFIKACJA):
        {message1}
        """
        response = self.model.generate_content(prompt)
        # print(response.text)
        response = response.text.replace("```python", "").replace("```", "").strip()
        
        # print("Kod napisany. Przekazuję do Testera.")
        return response

if __name__ == "__main__":
    developer = Developer(name="Developer")
    asyncio.run(developer.run())
