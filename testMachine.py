import asyncio
import websockets
import json
import ast
from agents.endpoint import Endpoint

class TestMachine(Endpoint):
    '''
    Funkcja zwraca następujące wartości:
    0- Kod jest poprawny składniowo, testy jednostkowe przeszły pomyślnie.
    1- Kod zawiera błędy składniowe, nie można uruchomić testów.
    2- Testy jednostkowe zawierają błędy składniowe.
    3- Testy jednostkowe nie przeszły pomyślnie.
    '''
    def getResponse(self, code, test_code):
        try:
            ast.parse(code)
        except SyntaxError as e:
            print(f"Błąd składni w kodzie: {e}")
            return 1
        
        try:
            ast.parse(test_code)
        except SyntaxError as e:
            print(f"Błąd składni w testach jednostkowych: {e}")
            return 2
        
        
        return 0

if __name__ == "__main__":
    tester = TestMachine(name="TestMachine")
    asyncio.run(tester.run())
