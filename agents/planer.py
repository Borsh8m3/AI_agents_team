import ast
from agents.base_agent import BaseAgent

class AgentPlaner(BaseAgent):
    def dzialaj(self, cel_projektu, model):
        self.komunikuj(f"Otrzymałem cel: '{cel_projektu}'. Analizuję...")
        
        prompt = (
            f"Jesteś Senior Architectem. Twoim celem jest: {cel_projektu}. "
            "Wypisz TYLKO listę nazw plików Python, które są potrzebne do zrealizowania tego celu. "
            "Format: ['plik1.py', 'plik2.py']. Nie dodawaj żadnego innego tekstu."
        )
        
        response = model.generate_content(prompt)
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
                
            self.komunikuj(f"Plan gotowy. Przekazuję {len(lista_zadan)} zadań do zespołu.")
            return lista_zadan
            
        except Exception as e:
            self.komunikuj(f"Błąd parsowania planu: {e}. Zwracam domyślne zadanie.")
            return ["app.py"]