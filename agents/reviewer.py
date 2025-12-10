import asyncio
import websockets
import json
<<<<<<< Updated upstream
from agents.base_agent import BaseAgent 
=======
from base_agent import BaseAgent 
>>>>>>> Stashed changes

class Reviewer(BaseAgent):
    def getResponse(self, message1, message2):
        print(f"Odebrałem raport Testera. Wdrażam poprawki.")
        
        prompt = f"Biorąc pod uwagę te uwagi: {message1}, napisz ostateczną, czystą wersję poniższego kodu:\n{message2}"
        response = self.model.generate_content(prompt)
        
        kod_finalny = response.text.replace("```python", "").replace("```", "").strip()
        
        print("Poprawki naniesione. Kod gotowy do zapisu.")
        return kod_finalny

if __name__ == "__main__":
    reviewer = Reviewer(name="Reviewer")
    asyncio.run(reviewer.run())
