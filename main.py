import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

from agents.planer import AgentPlaner
from agents.developer import AgentDeveloper
from agents.tester import AgentTester
from agents.reviewer import AgentReviewer

load_dotenv()

KLUCZE_API = [
    str(os.getenv("API_KEY_1")).strip(),
    str(os.getenv("API_KEY_2")).strip()
]

valid_keys = [k for k in KLUCZE_API if len(k) > 10]
if len(valid_keys) < 2:
    print(f"Załadowano tylko {len(valid_keys)} poprawnych kluczy z 2 wymaganych!")

licznik_rotacji = 0

def daj_mi_model(agent_name="System"):
    global licznik_rotacji
    
    indeks = licznik_rotacji % 2
    obecny_klucz = KLUCZE_API[indeks]
    licznik_rotacji += 1
    
    genai.configure(api_key=obecny_klucz)
    
    print(f"{agent_name} używa Klucza nr {indeks + 1}")
    return genai.GenerativeModel('gemini-2.5-flash')


planer = AgentPlaner("PLANER")
developer = AgentDeveloper("DEV")
tester = AgentTester("TESTER")
reviewer = AgentReviewer("REVIEWER")

def main():
    if not os.path.exists("workspace"):
        os.makedirs("workspace")

    cel = "Napisz prosty kalkulator w Pythonie"     #prompt wejsciowy

    model_p = daj_mi_model("PLANER")
    lista_zadan = planer.dzialaj(cel, model_p)
    
    print("-" * 40)

    for zadanie in lista_zadan:
        print(f"\nRozpoczynam cykl dla pliku: {zadanie}")
        
        model_d = daj_mi_model("DEV")
        kod_draft = developer.dzialaj(zadanie, model_d)
        
        model_t = daj_mi_model("TESTER")
        uwagi = tester.dzialaj(kod_draft, model_t)
        
        model_r = daj_mi_model("REVIEWER")
        kod_gotowy = reviewer.dzialaj(uwagi, model_r)
        
        sciezka = os.path.join("workspace", zadanie)
        open(sciezka, "w", encoding="utf-8").write(kod_gotowy)
        
        print(f"Plik {zadanie} zapisany.")
        print("-" * 40)
        
        time.sleep(1)

    print("\n=== KONIEC PRACY ===")

if __name__ == "__main__":
    main()