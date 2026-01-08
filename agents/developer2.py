import asyncio
import websockets
import json
from base_agent import BaseAgent 

class Developer2(BaseAgent):
    def getResponse(self, message1, message2):
        return "Hejjjj tu rewiuer"

if __name__ == "__main__":
    developer2 = Developer2(name="Developer2")
    asyncio.run(developer2.run())
