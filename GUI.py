import asyncio
import websockets
import json

class GUI:
    def __init__(self, server_url="ws://localhost:8765"):
        self.server_url = server_url

    async def sender(self, ws):
        """Wysyłanie wiadomości wpisanych w terminalu."""
        loop = asyncio.get_event_loop()
        while True:
            message = await loop.run_in_executor(None, input, "\nWpisz wiadomość:\n")
            await ws.send(json.dumps({"message": message}))

    async def receiver(self, ws):
        """Odbieranie wiadomości od HQ."""
        async for msg in ws:
            data = json.loads(msg)
            print(data["role"] + ": " + data["message"])

    async def run(self):
        """Główna logika połączenia."""
        async with websockets.connect(self.server_url) as ws:
            # Rejestracja jako GUI
            await ws.send(json.dumps({"role": "GUI"}))
            print("GUI połączony z serwerem.")

            # Uruchom wysyłanie i odbieranie równolegle
            send_task = asyncio.create_task(self.sender(ws))
            recv_task = asyncio.create_task(self.receiver(ws))

            await asyncio.gather(send_task, recv_task)


if __name__ == "__main__":
    client = GUI()
    asyncio.run(client.run())
