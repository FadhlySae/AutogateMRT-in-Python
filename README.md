# Autogate MRT Simulation

## Introduction

Autogate MRT Simulation is a Python terminal-based project that models the entry and exit flow of an MRT commuter gate system. It demonstrates how an autogate can process two payment methods, QRIS and ticket balance, while guiding the user through Tap-In and Tap-Out interactions in a simple command-line interface.

This project was originally developed as a procedural systems project and later refactored into smaller modules for better readability, maintainability, and portfolio presentation.


### Tech stack
- Python 3
- Standard Library only
- Command-line interface (CLI)
- Modular Python package structure

## Features

- Simulates **Tap-In** and **Tap-Out** gate flow
- Supports two payment methods:
  - **QRIS**
  - **Ticket / stored balance**
- Calculates fare based on destination station
- Displays gate direction using ASCII arrow visualization
- Separates user interaction, display logic, and fare logic into different modules

## Usage

Run the project from the root folder:

```bash
python -m src.cli
```

### Example flow

```text
Payment (A=QRIS, B=Ticket): B
Masukkan saldo yang ingin di top-up: 15000
Tap Your Card
TRANSACTION SUCCES
PLEASE ENTER

Payment (A=QRIS, B=Ticket): B
Choose your stations (1-7): 3
THANK YOU!
Credits left: 6000
```

## Project Structure

```text
autogate-mrt-simulation/
├─ README.md
└─ src/
   └─ autogate/
      ├─ cli.py
      ├─ display.py
      └─ costlogic.py
```

### Module overview
- `cli.py` — handles user input, payment flow, and main program execution
- `display.py` — renders ASCII arrows for gate entry/exit visualization
- `costlogic.py` — contains fare-building and cost calculation logic

## License
This project does not currently define a license.


If you want a simple permissive option, **MIT License** is usually a good default for student and portfolio projects.
