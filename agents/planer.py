import asyncio
import websockets
import json
from base_agent import BaseAgent
import ast

class Planer(BaseAgent):

    def getResponse(self, message, message1):
        self.model = self.get_model()
        
        prompt = f"""
        Jesteś Plannerem systemu współpracujących agentów AI.

        ### TWOJE ZADANIE:
        Zaplanuj strukturę rozwiązania dla następującego celu biznesowego lub technicznego:
        {message1}

        ### ZASADY PROJEKTOWE:
        1. Stosuj zasadę maksymalnej prostoty – wybieraj najprostsze możliwe rozwiązania.
        2. Unikaj nadmiernej abstrakcji, wzorców projektowych i zbędnych warstw pośrednich.
        3. Nie planuj elementów na przyszłość – tylko to, co jest niezbędne do realizacji celu.
        4. Jeśli coś da się zrobić w jednym pliku, nie dziel tego na kilka.

        ### WYMAGANIA DOTYCZĄCE STRUKTURY:
        1. Zaproponuj podział na moduły/komponenty możliwe do zaimplementowania jako osobne pliki Python.
        2. Każdy plik musi mieć jasno określoną, unikalną odpowiedzialność.
        3. Nie dubluj ról pomiędzy plikami.
        4. Zakładaj minimalną, ale wystarczającą liczbę plików.
        5. Pisz po polsku.

        ### WYMAGANIA DOTYCZĄCE ODPOWIEDZI (BARDZO WAŻNE):
        1. Zwróć TYLKO listę w poniższym formacie:
        ['plik1.py - krótki opis odpowiedzialności', 'plik2.py - krótki opis odpowiedzialności']
        2. Nie opisuj implementacji wewnętrznej, algorytmów ani szczegółów technicznych.
        3. Nie dodawaj żadnego innego tekstu, komentarzy ani formatowania.
        """

        response = self.model.generate_content(prompt)
        tekst_odpowiedzi = response.text.strip()
        print("\nTekst odpowiedzi:::::::::::::::::::::::::::::::::::")
        print(tekst_odpowiedzi)
        try:
            start = tekst_odpowiedzi.find('[')
            end = tekst_odpowiedzi.rfind(']') + 1
            if start != -1 and end != 0:
                czysta_lista = tekst_odpowiedzi[start:end]
                lista_zadan = ast.literal_eval(czysta_lista)
            else:
                lista_zadan = ["main_script.py - stwórz pełny i kompatybilny kod realizujący następujące zadanie: {message}"]
                
            print(f"\n\nPlan gotowy.\nPrzekazuję {len(lista_zadan)} zadań do zespołu.")
            return lista_zadan
            
        except Exception as e:
            print(f"Błąd parsowania planu: {e}. Zwracam domyślne zadanie.")
            return [f"app.py - stwórz pełny i kompatybilny kod realizujący następujące zadanie: {message}"]

if __name__ == "__main__":
    planner = Planer(name="Planner")
    asyncio.run(planner.run())
 