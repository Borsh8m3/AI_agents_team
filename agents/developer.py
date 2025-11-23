from agents.base_agent import BaseAgent

class AgentDeveloper(BaseAgent):
    def dzialaj(self, nazwa_pliku, model):
        self.komunikuj(f"Przyjąłem zadanie: {nazwa_pliku}. Rozpoczynam kodowanie.")
        
        prompt = f"Napisz kompletny, działający kod w Pythonie dla pliku: {nazwa_pliku}. Tylko kod, bez bloków markdown."
        response = model.generate_content(prompt)
        
        kod = response.text.replace("```python", "").replace("```", "").strip()
        
        self.komunikuj("Kod napisany. Przekazuję do Testera.")
        return kod