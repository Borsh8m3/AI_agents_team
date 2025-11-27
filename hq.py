import asyncio
import websockets
import json
import os
# import ast

connected_clients = {}  # {'gui': ws, 'tester': ws}
def clear_variables():
    global task, files, code, test_code
    task = ""
    files=[]
    code=""
    test_code=""

# def send_to_gui(role, data):
#     gui_ws = connected_clients.get("GUI")
#     if gui_ws:
#         asyncio.create_task(gui_ws.send(json.dumps({
#             "role": role,
#             "message": data
#         })))

def save_code_to_file(filename, code):
    os.makedirs("workspace", exist_ok=True)
    path = os.path.join("workspace", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)



async def handler(ws, path):
    # Pierwsza wiadomość to rejestracja roli
    register_msg = await ws.recv()
    data = json.loads(register_msg)
    role = data.get("role")
    connected_clients[role] = ws
    print(f"{role} połączony")


    try:
        async for message in ws:
            data = json.loads(message)
            print(f"\n\nOtrzymano od {role}: {data}")

            if "message1" in data:
                global task, files, code, test_code
                
                if role == "GUI":
                    clear_variables()
                    task = data["message1"] #Polecenie z GUI
                    planer_ws = connected_clients.get("Planner")
                    if planer_ws:
                        await planer_ws.send(json.dumps({
                            "message1": "",
                            "message2": task
                            }))
                
                elif role == "Planner":
                    files = data["message1"] #lista plików z Planera
                    
                    developer_ws = connected_clients.get("Developer")

                    if developer_ws:
                        await developer_ws.send(json.dumps({
                            "message1": files, #wysyłanie listy plików do Developera
                            "message2": task    #wysyłanie polecenia do Developera
                        }))

                
                elif role == "Developer":
                    tester_ws = connected_clients.get("Tester")
                    code = data["message1"] #kod z Developera
                    if tester_ws:
                        await tester_ws.send(json.dumps({
                            "message1": code, #przesyłanie kodu do Testera
                            "message2": task    #wysyłanie oryginalnego polecenia do Testera 
                        }))
                
                elif role == "Tester":
                    test_machine_ws = connected_clients.get("TestMachine")
                    test_code = data["message1"] #testy z Testera
                    if test_machine_ws:
                        await test_machine_ws.send(json.dumps({
                            "message1": code,   #wysyłanie kodu
                            "message2": test_code            #wysyłanie testów
                        }))
                

                elif role == "TestMachine":
                    if data["message1"] == 0:
                        save_code_to_file(files[0], code)
                        print("Kod zapisany do final_code.py")
                        save_code_to_file(files[0][:-3] + "_test.py", test_code)
                        print("Testy zapisane do final_tests.py")



                

    except websockets.ConnectionClosed:
        print(f"{role} rozłączony")
        del connected_clients[role]

async def main():
    async with websockets.serve(handler, "localhost", 8765, ping_timeout=None):
        print("HQ running on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())