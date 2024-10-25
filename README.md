# Python Weather Service Project - Example for Setting Up Pytest and Pipenv

![Coverage Badge](https://img.shields.io/badge/coverage-95%25-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This repository is an example project designed to demonstrate how to set up and use `pipenv` for dependency management and `pytest` for testing in Python. It includes configuration for code coverage, linting, and formatting, making it an ideal starting point for Python projects with best practices.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Setup and Installation](#setup-and-installation)
5. [Running Tests](#running-tests)
6. [Code Coverage](#code-coverage)
7. [Linting and Formatting](#linting-and-formatting)
8. [Example Usage](#example-usage)
9. [Troubleshooting](#troubleshooting)

---

## Introduction

This repository is intended as a **tutorial and starting point** for those looking to implement `pytest` and `pipenv` in Python projects. By following this guide, you'll learn:

- How to use `pipenv` to manage dependencies and virtual environments.
- How to set up and configure `pytest` for running tests.
- How to configure code coverage using `pytest-cov`.
- How to use `flake8` and `black` for linting and formatting, ensuring code quality.

This project includes an example weather service API function (`weather_service.py`) and corresponding unit tests with mocked responses, showing how to handle external API dependencies in tests.

---

## Project Structure

The project is organized as follows:

```plaintext
python-test/
├── src/
│   └── weather_service.py          # Main module for fetching weather data
├── tests/
│   └── test_weather_service.py      # Unit tests for the weather service
├── Pipfile                          # Pipenv configuration for dependencies
└── README.md                        # Project documentation
```

- **src/**: Contains the main module (`weather_service.py`) that simulates fetching weather data from an API.
- **tests/**: Contains unit tests with mocked API responses for testing `weather_service.py`.
- **Pipfile**: Defines project dependencies, dev dependencies, and script commands for pipenv.

---

## Requirements

- Python 3.10 or higher
- Pipenv for dependency management

## Setup and Installation

1. **Install Pipenv**
   If Pipenv is not installed, install it globally using:

   ```bash
   pip install pipenv
   ```

2. **Clone the Repository**
   Clone this project repository to your local machine:

   ```bash
   git clone https://github.com/your-username/python-test.git
   cd python-test
   ```

3. **Install Dependencies**
   Use Pipenv to install all necessary packages:

   ```bash
   pipenv install --dev
   ```

   This installs both regular and development dependencies (such as `pytest`, `flake8`, and `black`).

4. **Activate the Virtual Environment**
   Activate the virtual environment created by Pipenv:
   ```bash
   pipenv shell
   ```

---

## Running Tests

The project uses `pytest` for testing and `pytest-cov` for code coverage. Tests are written with mocks to simulate API responses and handle exceptions.

1. **Run All Tests**
   Run the tests using the following command:

   ```bash
   pipenv run test
   ```

2. **Test Command Explanation**
   The test command in the `Pipfile` is configured as follows:
   ```toml
   [scripts]
   test = "env PYTHONPATH=src pytest --cov=src --cov-report=term-missing --cov-report=html"
   ```
   - `--cov=src`: Specifies the `src` directory for measuring test coverage.
   - `--cov-report=term-missing`: Displays a report in the terminal, showing lines that are not covered.
   - `--cov-report=html`: Generates an HTML report that can be found in the `htmlcov` directory after running the command.

---

## Code Coverage

1. **Run Coverage Report**
   Run the tests with coverage by executing:

   ```bash
   pipenv run test
   ```

2. **View HTML Coverage Report**
   After running the test command, open the coverage report by navigating to `htmlcov/index.html` in your browser to view a detailed, line-by-line report.

---

## Linting and Formatting

This project uses `flake8` for linting and `black` for formatting to maintain code quality and consistency.

1. **Run Linting (flake8)**
   Check the code for PEP 8 compliance and common issues:

   ```bash
   pipenv run lint
   ```

   The lint command in the `Pipfile` is configured as:

   ```toml
   lint = "flake8 ."
   ```

2. **Run Formatting (black)**
   Format the code automatically using `black`:
   ```bash
   pipenv run format
   ```
   The format command in the `Pipfile` is configured as:
   ```toml
   format = "black ."
   ```

---

## Example Usage

To fetch weather data from the API in `weather_service.py`, you can call the `get_weather` function with a city name:

```python
from src.weather_service import get_weather

temperature = get_weather("New York", api_key="your_api_key")
print(f"The temperature in New York is {temperature}°C")
```

This example demonstrates handling external API dependencies by using mock data in the tests, allowing you to understand how to structure tests for functions with external dependencies.

---

## Troubleshooting

- **Module Not Found Error**: Ensure `PYTHONPATH=src` is correctly set in the `Pipfile` test script.
- **Request Timeout**: The API call in `weather_service.py` has a timeout set; adjust this as necessary depending on network conditions.
