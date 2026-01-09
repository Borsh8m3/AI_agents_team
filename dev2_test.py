from agents.developer2 import Developer2

dev = Developer2(name="Developer2")
while True:
    polecenie = input("\nPolecenie (pusta linia kończy): ").strip()
    if not polecenie:
        break
    kod = dev.getResponse("wynik.py", polecenie)
    print("\n=== Odpowiedź Developera 2 ===\n", kod)