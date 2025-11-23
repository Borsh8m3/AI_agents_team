import google.generativeai as genai
import os
from dotenv import load_dotenv
import sys

print(f"System Python: {sys.version}")
print(f"Wersja biblioteki google-generativeai: {genai.__version__}")
print("-" * 30)

load_dotenv()
api_key = os.getenv("API_KEY") 

try:
    genai.configure(api_key=api_key)
    
    print("Dostępne modele dla Twojego klucza:")
    print("(Kopiuj nazwę dokładnie tak, jak poniżej!)")
    print("-" * 30)
    
    found_flash = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"{m.name}")
            if "flash" in m.name:
                found_flash = True
    
    print("-" * 30)
    if not found_flash:
        print("❌ UWAGA: Twój klucz/biblioteka NIE WIDZI modelu Flash!")
        print("Spróbuj użyć modelu 'gemini-pro' (jest starszy, ale zazwyczaj działa).")

except Exception as e:
    print(f"Błąd krytyczny: {e}")