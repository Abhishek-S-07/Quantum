# QuantumSecureNet

QuantumSecureNet is a Python-based project skeleton for simulating quantum key distribution (QKD) workflows, including BB84 protocol components, visualization helpers, and a simple application entry point.

## Overview

This repository provides a modular foundation for exploring quantum communication concepts such as:
- BB84 protocol structure
- Alice/Bob/Eve simulation roles
- Noise, QBER, reconciliation, and privacy amplification helpers
- Basic visualization utilities for charts and network diagrams

## Features

- Modular package structure for protocol components
- Reusable modules for simulation logic and analysis
- Visualization support for charts and network layouts
- Simple app launcher entry point for local experimentation

## Technologies Used

- Python 3.x
- Standard library modules
- Optional visualization libraries (to be added in requirements)

## Folder Structure

```text
QuantumSecureNet/
├── app.py
├── requirements.txt
├── README.md
├── bb84/
│   ├── __init__.py
│   ├── alice.py
│   ├── bob.py
│   ├── protocol.py
│   ├── noise.py
│   ├── eve.py
│   ├── reconciliation.py
│   ├── privacy.py
│   ├── qber.py
│   └── qchm.py
├── visualization/
│   ├── charts.py
│   └── network.py
├── assets/
│   ├── images/
│   └── icons/
└── data/
```

## How to Run the Project

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows PowerShell:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Notes

This project is currently a starter structure and can be expanded with more advanced simulation logic, networking visualizations, and dependencies as the project evolves.
