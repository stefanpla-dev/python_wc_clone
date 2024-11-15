## Summary
'python_wc_clone' is a Python command-line application that mimics the functionality of the Linux 'wc' command. It allows for the counting of bytes, lines, words, and characters in a given file, or from standard input. Additionally, it logs the details of each file or input processed into a SQLite database for further analysis or record-keeping.

## Features
- Count bytes with the `-c` flag.
- Count lines with the `-l` flag.
- Count words with the `-w` flag.
- Count characters with the `-m` flag.
- Supports reading from standard input.
- Displays combined results when no flag is specified (default: lines, words, bytes).
- Logs the following details into an SQLite database:
    - File path (or stdin)
    - Number of bytes, lines, words, and characters
    - Timestamp of processing

## Requirements
- Python 3.6+
- pytest (for unit testing)
- SQLite (included by default in Python)

## Installation
1. Clone this repository:

git clone https://github.com/stefanpla-dev/python_wc_clone.git
cd python_wc_clone

2. Set Up a Virtual Environment
- On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
- On Windows
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Initialize the SQLite Database
- Use the db.py file to set up the database:
python src/db.py

4. Usage 
- From file path:
python src/wc.py (insert flag here) (insert file path here)
- From standard input:
cat | python src/wc.py (insert flag here)

5. Unit Testing
PYTHONPATH=src pytest
pytest

6. License
This project is licensed under the MIT License.

