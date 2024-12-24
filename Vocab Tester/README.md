# Terminal Vocabulary Tester 📚

## Overview
This is a Python-based vocabulary tester designed to quiz you on the meanings of words provided in an Excel file. The program shuffles the words randomly and requires you to input the definitions. It also gives detailed feedback on your answers, highlights missing definitions, and calculates your score at the end.

## Features
- Reads words and definitions from an Excel file (`words.xlsx`).
- Supports words with multiple meanings separated by `/`.
- Provides feedback on incorrect or incomplete answers.
- Displays a final score, percentage, and a list of incorrectly answered words.

## How to Set Up
1. **Requirements**: Ensure you have Python installed along with the following library:
   - Install `openpyxl` for working with Excel: `pip install openpyxl`

2. **Excel File Format**:
   - The program requires an Excel file named `words.xlsx` in the same directory as the script.
   - Words should be in **Column A**, and their corresponding definitions should be in **Column B**.
   - If a word has multiple meanings, separate them using `/` without spaces (e.g., `advance/progress`).

   **Example of Proper Format** (from the provided image):

   | A                          | B                            |
   |----------------------------|------------------------------|
   | progredior, progredi, ...  | advance/progress             |
   | primo                      | at first                     |
   | nec                        | nor/and not/neither          |
   | prope + accusative         | near                         |

   - Any additional columns (C, D, etc.) will **not** be read by the program.
   - Note: do not be confused by the comma separations in some examples. These are just for clarifications in the Latin word.

3. **Run the Program**:
   - Save the provided Python code in a `.py` file (e.g., `vocab_tester.py`).
   - Place the `words.xlsx` file in the same directory as the `.py` file.
   - Run the program using: `python vocab_tester.py`.

4. **Input Definitions**:
   - When prompted, type the definition(s) of the word shown.
   - If there are multiple definitions, separate them with commas (e.g., `advance, progress`).

## How It Works
1. **Data Parsing**:
   - The program reads from the Excel file and extracts word-definition pairs from Columns A and B.
   - Words containing special characters like commas or parentheses are automatically truncated at the first special character.

2. **Quiz Logic**:
   - Words are displayed one at a time.
   - The program checks your input against the correct definitions using similarity matching (using `SequenceMatcher`).

3. **Feedback and Scoring**:
   - Detailed feedback is provided for each answer, indicating:
     - Incorrect or incomplete answers with suggestions.
     - Missing definitions.
   - At the end, a final score and percentage are displayed along with a list of incorrectly answered words (if any).

## Customization
- **Catch Characters**: Modify the `catch` list in the code to include or exclude characters that truncate words.
- **Definitions Format**: Ensure definitions in Column B are separated by `/` without spaces for multiple meanings.

## Example Run
```plaintext
1) What is the definition of: progredior
Your answer (separate multiple answers with commas): progress, advance
Correct!

2) What is the definition of: nec
Your answer (separate multiple answers with commas): neither
Incorrect --> 'neither' is incorrect or incomplete. Best match is 'nor/and not/neither'
The correct definition is: nor/and not/neither
```
## Exiting
To exit, close the terminal or press ``` CTRL C ```
