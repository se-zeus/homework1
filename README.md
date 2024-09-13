# HW2 Repository

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![License](https://img.shields.io/github/license/se-zeus/homework1.svg)

![Platform](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

[![Pytest](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml/badge.svg?event=push&name=pytest_check)](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml)
[![AutoPEP8](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml/badge.svg?event=push&name=autopep8_check)](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml)
[![Radon](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml/badge.svg?event=push&name=radon_check)](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml)
[![Bandit](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml/badge.svg?event=push&name=bandit_check)](https://github.com/Anjan50/homework1/actions/workflows/pyflow.yaml)


# Homework 2: Python Debugging, Static Analysis, and Testing

![badge_pylint](https://img.shields.io/badge/Pylint-brightgreen)
![badge_pyright](https://img.shields.io/badge/Pyright-brightgreen)
![badge_total_tests](https://img.shields.io/badge/Total_Tests-20-success)
![badge_code_coverage](https://img.shields.io/badge/Code_Coverage-95%25-brightgreen)
![badge_pytest_status](https://img.shields.io/badge/Pytest-brightgreen)

## Project Overview

This project focuses on debugging, static analysis, and unit testing in Python. You will implement and debug Python scripts using tools like Pytest, Pylint, and Pyright, alongside continuous integration workflows to ensure code quality.

### Files and Directory Structure

```text
.
├── hw2
│   ├── hw2_debugging.py      # Debugging file implementing merge sort
│   ├── rand.py               # Helper function to generate random arrays
│   ├── test_merge.py         # Unit tests for the merge sort function
│   └── __pycache__/          # Ignored Python cache files
├── logs/                     # Logs directory for static analysis and debugging
├── README.md                 # This file
└── .gitignore                # Files and directories to be ignored by Git
