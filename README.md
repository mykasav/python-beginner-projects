# Python Beginner Projects

A collection of small command-line programs I built on my own while learning Python — covering control flow, classes, input validation, file I/O and third-party libraries.

| Project | File | What it practises |
|---|---|---|
| **Password Manager** | [`passmanager.py`](passmanager.py) | Multi-user login, per-user vaults, reading/writing/filtering text files |
| **Expense Tracker** | [`expense.py`](expense.py) | Classes, menu-driven loops, `try/except` input validation |
| **Rock, Paper, Scissors** | [`rps.py`](rps.py) | Classes, class constants, game logic against a random opponent |
| **Number Guessing Game** | [`guessnr.py`](guessnr.py) | Random numbers, comparison logic, input validation |
| **Dice Roller** | [`diceroll.py`](diceroll.py) | Classes, loops, random numbers |
| **QR Code Generator** | [`qrcoding.py`](qrcoding.py) | Using a third-party library (`qrcode`) to generate images |
| **Population Growth** | [`ppl.py`](ppl.py) | Simulation with a `while` loop — years until a population reaches a target |

## Running

Requires Python 3.10+. Every project is a single file:

```bash
python passmanager.py
```

Only the QR code generator has a dependency:

```bash
pip install -r requirements.txt
python qrcoding.py
```

## Notes

- Some programs have their prompts in Portuguese and others in English.
- The password manager is a file-handling exercise: it stores passwords in **plain text** and must not be used for real credentials. A natural next step would be hashing the master password (e.g. `hashlib` / `bcrypt`) and encrypting the vault (e.g. `cryptography.fernet`).
