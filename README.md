# Armies Challenge - Amalgama

A clean, extensible, and production-ready domain model for simulating medieval armies, built using **Python**

This project models:

- Units (Pikeman, Archer, Knight)
- Armies belonging to civilizations
- Training and transformation rules
- Battles between armies
- Battle history tracking
- Fully validated domain objects using Pydantic v2

## 🚀 Features

### ✔️ Unit Modeling

All unit types inherit from `Unit`, which includes:

- Creation date
- Base strength
- `train()` method with validation

### ✔️ Army Modeling

The `Army` model includes:

- Name & Civilization
- Dynamic unit population based on civilization
- Battle logic (`attack()`)
- Training (`train_unit()`)
- Transformation (`transform_unit()`)
- Battle history

### ✔️ Use of Pydantic

- Input & assignment validation (`validate_assignment=True`)
- Flexible mutation (`frozen=False`)
- `model_post_init` for custom initialization (replaces `__init__`)
- Strong typing everywhere

### ✔️ Clean Simulation Rules

Rules are stored in `rules.py`:

- `TRAINING_RULES`
- `TRANSFORMATION_RULES`
- `CIVILIZATION_START`

All rules are type-safe and easy to extend.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vazqueztomas/amalgama-army-challenge.git
cd amalgama-army-challenge
```

### 2. Install dependencies

```bash
uv sync
```

### Running the Demo

```bash
uv run main.py
```

## 🛠️ Development

Important Notes: I decided to use pyproject.toml for dependency management and project configuration - Also I used Pylint for linting with some custom rules to fit the project's needs.
