from agents.developer import Developer

dev = Developer(name="Developer")
while True:
    polecenie = input("\nPolecenie (pusta linia kończy): ").strip()
    if not polecenie:
        break
    kod = dev.getResponse("wynik.py", polecenie)
    print("\n=== Odpowiedź Developera ===\n", kod)