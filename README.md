# Agentic Essay Writer

An interactive Agentic AI system for essay generation and management, featuring modular state tracking and multi-thread support with a user-friendly Gradio web interface.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Code Structure](#code-structure)  
- [How It Works](#how-it-works)  


---

## Project Overview

This project implements an agentic AI-powered essay writer that uses a state graph to track multiple threads and revisions. It provides a modular, extensible backend and a clean web interface built with Gradio to generate, continue, and manage essays and related content.

---

## Features

- Stateful graph-based agent architecture with support for multiple threads and revision tracking.
- Interactive Gradio UI with tabs for generating essays, planning, drafting, critiquing, and viewing state snapshots.
- Thread and step switching to revisit and modify previous states easily.
- State history management allowing rollback and copying of previous states.
- Modular functions for state retrieval, updating, and display.
- Flexible agent control with interruptible execution checkpoints.

---

## Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/agentic-essay-writer.git
cd agentic-essay-writer
````

Create and activate a Python virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> **Note:** Make sure you have Python 3.8+ installed.

---

## Usage

Run the app with:

```bash
python app.py
```

This launches a Gradio web UI accessible at `http://localhost:7860` (or as printed in the terminal).

From the interface, you can:

* Generate new essays based on a topic.
* Continue essay drafts.
* Manage multiple threads and revision states.
* Modify plans, drafts, critiques.
* View state snapshots and histories.

---

## Code Structure

* `essay_writer.py`: Core agent logic and graph-based state management.
* `gui.py`: Gradio interface definitions and callbacks.
* `main.py`: Main entry point to start the application.
* `requirements.txt`: Python dependencies.
* `README.md`: This file.

---

## How It Works

The system maintains a directed graph of states representing the agent’s thought process, draft versions, and other metadata. Each state includes nodes with details such as revision number, thread ID, and content.

The Gradio frontend allows interacting with this graph:

* Viewing current state metadata (last node, next node, thread info).
* Switching threads and steps to load previous states.
* Modifying specific state keys like plan, draft, and critique.
* Generating new or continued essays via agent callbacks.

The modular design supports easy extension with new state keys and agent actions.

---
