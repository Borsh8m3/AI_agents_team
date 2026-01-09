
import subprocess
import os
import time
import signal

AGENTS = [
    ("HQ", "hq.py"),
    ("Developer", "agents/developer.py"),
    ("Developer2", "agents/developer2.py"),
    ("Planner", "agents/planer.py"),
    ("Reviewer", "agents/reviewer.py"),
    ("Tester", "agents/tester.py"),
    ("TestMachine", "testMachine.py"),
    ("GUI", "GUI.py"),
]

processes = []

def run_in_terminal(title, script):
    # /c = okno zamknie się automatycznie, kiedy proces się zakończy
    # start = otwórz nowe okno
    cmd = f'start "{title}" cmd /c python "{script}"'
    return subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
    try:
        for name, path in AGENTS:
            if os.path.exists(path):
                print(f"Uruchamiam {name} …")
                p = run_in_terminal(name, path)
                processes.append(p)
                time.sleep(0.2)
            else:
                print(f"Plik nie istnieje: {path}")

        print("\nWszystkie procesy uruchomione. CTRL+C aby je zakończyć.\n")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nZatrzymuję wszystkie procesy...\n")
        # Zabij całe drzewa procesów + okna terminala
        for p in processes:
            try:
                subprocess.call(f"taskkill /PID {p.pid} /T /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                pass

        print("Wszystkie procesy zakończone.")
