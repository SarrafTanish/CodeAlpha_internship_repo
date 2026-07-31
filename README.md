[README.md](https://github.com/user-attachments/files/30596697/README.md)
# CodeAlpha Internship Projects

This repository contains the Python projects completed as part of the **CodeAlpha Internship**. Each task is a standalone script demonstrating a different Python concept — from simple games and automation scripts to file/data handling.

## 📁 Repository Structure

```
Internship project/
├── Task-1.py           # Hangman Game
├── Task-2.py            # Stock Portfolio Tracker
├── Task-3/
│   ├── extract_emails.py    # Extracts email addresses from text/files
│   ├── move_jpg_files.py    # Automates sorting/moving of .jpg files
│   └── scrape_title.py      # Scrapes webpage titles
├── Task-4.py             # Rule-Based Chatbot
└── README.md
```

## 🧩 Tasks Overview

### Task 1 — Hangman Game
A classic command-line Hangman game. The program randomly picks a word from a predefined word list, and the player has to guess it letter by letter within a limited number of incorrect attempts.

**Features:**
- Random word selection
- Tracks guessed letters and remaining attempts
- Win/loss detection with replay option

**Run it:**
```bash
python Task-1.py
```

---

### Task 2 — Stock Portfolio Tracker
A console-based tool to track a simple stock portfolio. Users select stocks from a predefined price list, enter quantities, and get a calculated investment summary — with the option to export it as a `.txt` or `.csv` file.

**Features:**
- Interactive stock/quantity input with validation
- Automatic total investment calculation
- Export summary to `.txt` or `.csv`

**Run it:**
```bash
python Task-2.py
```

---

### Task 3 — Automation Scripts
A collection of small Python automation utilities:

| Script | Purpose |
|---|---|
| `extract_emails.py` | Extracts and lists email addresses found in a given text or file |
| `move_jpg_files.py` | Automatically finds and moves `.jpg` files into a target folder |
| `scrape_title.py` | Fetches a webpage and extracts/prints its title |

**Run any script:**
```bash
python Task-3/extract_emails.py
python Task-3/move_jpg_files.py
python Task-3/scrape_title.py
```

---

### Task 4 — Rule-Based Chatbot
A simple keyword/rule-based chatbot that responds to greetings, small talk, and basic queries using predefined logic (no ML/NLP model involved).

**Features:**
- Keyword-based response matching (case-insensitive)
- Handles greetings, help requests, and exit commands
- Runs in a continuous loop until the user says "bye"

**Run it:**
```bash
python Task-4.py
```

## ⚙️ Requirements

- Python 3.x
- No external libraries required for Task-1, Task-2, and Task-4 (uses only Python standard library: `random`, `csv`)
- Task-3 scripts may require additional libraries depending on implementation (e.g. `requests`, `beautifulsoup4` for web scraping, `shutil`/`os` for file operations)

Install any needed dependencies with:
```bash
pip install requests beautifulsoup4
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/SarrafTanish/CodeAlpha_internship_repo.git
   cd CodeAlpha_internship_repo
   ```
2. Run any task file with Python:
   ```bash
   python Task-1.py
   ```

## 👤 Author

**Tanish Sarraf**
B.Tech CSE, Uttaranchal University
GitHub: [SarrafTanish](https://github.com/SarrafTanish)
LinkedIn: [tanishsarraf](https://linkedin.com/in/tanishsarraf-520144346)

## 📝 License

This project is for educational purposes as part of the CodeAlpha internship program.
