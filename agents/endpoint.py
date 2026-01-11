import asyncio
import websockets
import json

class Endpoint:

    def __init__(self, name, server_url="ws://localhost:8765"):
        self.server_url = server_url
        self.name = name

    def getResponse(self, message, message1):
        return "Nie nadpisano funkcji"

    async def handle_messages(self, ws):
        """Obsługuje przychodzące wiadomości."""
        async for message in ws:
            data = json.loads(message)
            print(f"{self.name} otrzymał:", data)

            if "message" in data and "message1" in data:
                response = {"status": "OK"}
                await ws.send(json.dumps(response))

                message = self.getResponse(data['message'], data["message1"])
                response = {"message": message}
                await ws.send(json.dumps(response))


    async def run(self):
        while True:
            try:
                async with websockets.connect(self.server_url) as ws:
                    # Rejestracja w HQ
                    await ws.send(json.dumps({"role": self.name}))
                    print(f"{self.name} połączony z HQ.")

                    # Nasłuchiwanie wiadomości
                    await self.handle_messages(ws)
            except websockets.exceptions.ConnectionClosed:
                print(f"{self.name} rozłączony. Próbuję ponownie za 3 sekundy...")
                await asyncio.sleep(3)
            except Exception as e:
                print(f"{self.name} błąd: {e}. Próbuję ponownie za 3 sekundy...")
                await asyncio.sleep(3)