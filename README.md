# SEIS 603: Foundations of Python

Course materials and assignments for SEIS 603 Foundations of Python at the University of St. Thomas.

## Course Overview

This repository contains weekly exercises, homework assignments, and practice problems covering fundamental Python programming concepts and data analysis techniques.

## Repository Structure

```
src/
├── week-2/          # Python fundamentals review (Chapters 1-6)
├── week-4/          # Files and Lists (Chapters 7-8)
├── week-5/          # Dictionaries and Tuples (Chapters 9-10)
├── week-6/          # Regex and Networked Programs (Chapters 11-12)
├── week-7/          # XML and JSON data processing (Chapter 13)
└── week-9/          # Data analysis with Jupyter notebooks
```

## Topics Covered

### Week 2: Python Fundamentals
- Review of basic Python concepts (variables, control flow, functions)
- Code exchange exercises
- Testing with pytest

### Week 4: Files and Collections
- File I/O operations (Chapter 7)
- Lists and list processing (Chapter 8)
- Calculator implementation with unit tests

### Week 5: Data Structures
- Dictionaries (Chapter 9)
- Tuples (Chapter 10)
- Text file processing and word counting

### Week 6: Advanced Topics
- Regular expressions (Chapter 11)
- Network programming and HTTP (Chapter 12)
- HTML parsing with Beautiful Soup
- Binary file handling
- Web scraping techniques

### Week 7: Data Formats
- XML parsing and processing (Chapter 13)
- JSON data extraction
- GeoJSON data handling
- Data validation

### Week 9: Data Analysis
- Jupyter notebooks
- Pandas data analysis
- Dataset exploration (Titanic dataset)

## Setup

This project uses Python 3.13+ and is managed with [uv](https://github.com/astral-sh/uv).

### Prerequisites

- Python 3.13 or higher
- uv package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd SEIS-603
```

2. Install dependencies:
```bash
uv sync
```

3. Activate the virtual environment:
```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

## Dependencies

Key libraries used in this course:

- **Data Analysis**: pandas, numpy, matplotlib, seaborn, plotly, altair
- **Web Scraping**: beautifulsoup4, requests
- **Data Formats**: xmlschema
- **Development**: pytest, ruff, jupyterlab
- **Utilities**: rich, tabulate

## Running Code

### Python Scripts
```bash
python src/week-4/calculator.py
```

### Jupyter Notebooks
```bash
jupyter lab
# Navigate to src/week-9/ and open notebooks
```

### Running Tests
```bash
pytest
```

### Code Linting
```bash
ruff check .
ruff format .
```

## Project Configuration

- **Linting**: Configured with Ruff (79 character line length)
- **Testing**: pytest framework
- **Python Version**: 3.13+

## License

Course materials for educational purposes at the University of St. Thomas.
