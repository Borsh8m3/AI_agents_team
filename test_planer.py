from agents.planer import Planer

dev = Planer(name="Planer")
while True:
    polecenie = input("\nPolecenie (pusta linia kończy): ").strip()
    if not polecenie:
        break
    kod = dev.getResponse("wynik.py", polecenie)
    print("\n=== Odpowiedź Planera ===\n", kod)