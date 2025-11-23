# AI Agents Team (Multi-Agent System)

An engineering project implementing a team of autonomous AI agents collaborating to create software automatically. The system is based on the Google Gemini 1.5 Flash model and utilizes a pipeline architecture.

## 👥 Agents

Planner - Analyzes the user's prompt and creates a list of necessary Python files (System Architecture).

Developer - Writes the initial source code for each task defined by the Planner.

Tester - Analyzes the code for errors and suggests improvements.

Reviewer - Implements fixes based on the Tester's report and approves the final version of the file.

## 🛠️ Requirements

Python 3.10+

Google AI Studio Account (API Keys)

## 🚀 Installation

Clone the repository:

git clone [https://github.com/Borsh8m3/AI_agents_team.git](https://github.com/Borsh8m3/AI_agents_team.git)
cd AI_agents_team


Install dependencies:

pip install -r requirements.txt


Configure API Keys:

Create a .env file in the main directory.

Paste your Google Gemini API keys following this pattern:

API_KEY_1=...
API_KEY_2=...
API_KEY_3=...
API_KEY_4=...


(The system supports API Key Rotation to increase rate limits and distribute load across multiple keys).

## ▶️ Usage

Run the main orchestrator script:

python main.py

The system will start the pipeline (Planning -> Coding -> Testing -> Reviewing). The generated code will be saved in the /workspace directory.
