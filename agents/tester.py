from agents.base_agent import BaseAgent

class AgentTester(BaseAgent):
    def dzialaj(self, kod, model):
        self.komunikuj("Odebrałem kod. Rozpoczynam analizę pod kątem błędów.")
        
        prompt = (
            "Przeanalizuj poniższy kod Python. Wypisz krótko 2 najważniejsze sugestie poprawek "
            "lub napisz 'BRAK_UWAG' jeśli kod jest dobry.\n\n"
            f"KOD:\n{kod}"
        )
        response = model.generate_content(prompt)
        
        self.komunikuj(f"Testy zakończone. Wysyłam raport do Reviewera.")
        return response.text