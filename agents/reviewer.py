from agents.base_agent import BaseAgent

class AgentReviewer(BaseAgent):
    def dzialaj(self, uwagi_testera, model):
        self.komunikuj(f"Odebrałem raport Testera. Wdrażam poprawki: {uwagi_testera[:50]}...")
        
        prompt = f"Biorąc pod uwagę te uwagi: {uwagi_testera}, napisz ostateczną, czystą wersję kodu."
        response = model.generate_content(prompt)
        
        kod_finalny = response.text.replace("```python", "").replace("```", "").strip()
        
        self.komunikuj("Poprawki naniesione. Kod gotowy do zapisu.")
        return kod_finalny