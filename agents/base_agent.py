class BaseAgent:
    def __init__(self, rola):
        self.rola = rola

    def komunikuj(self, wiadomosc):
        print(f"{self.rola}: {wiadomosc}")