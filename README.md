BMI Calculator (Python Script Documentation)

Overview

This script is a command-line Body Mass Index (BMI) calculator that computes a user’s BMI based on height and weight, classifies the result into standard health categories, and saves the output to a user-defined directory.

It includes input validation, formatting, and file saving functionality.


---

Features

Interactive BMI calculation (height and weight input)

Input validation (ensures numeric and positive values)

Automatic BMI classification

Formatted result output

Saves results to a file

User-defined output directory

Error handling for invalid inputs and file operations



---

Requirements

Python Version

Python 3.7+


Dependencies

No external libraries required


Only standard Python libraries are used:

os

pathlib



---

How It Works

1. User Input Validation

Function: get_float_input

This function ensures that user input is valid:

Rules:

Input must be a number

Input must be greater than 0


If invalid:

The user is prompted again

Error message is displayed


Example:

Enter height (meters): -2
Invalid input: Value must be positive.


---

2. BMI Calculation

Function: calculate_bmi_value

Formula used:

BMI = weight / (height²)

Example:

Height = 1.75 m
Weight = 70 kg

BMI = 70 / (1.75 * 1.75) = 22.86


---

3. BMI Classification

Function: classify_bmi

The BMI result is categorized as:

BMI Range	Category

< 18.5	Underweight
18.5–24.9	Normal weight
25–29.9	Overweight
≥ 30	Obese


Example:

BMI: 22.86 → Normal weight


---

4. Result Formatting

Function: format_result

Creates a readable output string:

Example output:

Height: 1.75 m
Weight: 70 kg
BMI: 22.86
Category: Normal weight


---

5. Directory Validation

Function: get_valid_directory

This function ensures the save location exists.

Process:

User enters directory path

Script checks if it is valid

If invalid, user is prompted again


Example:

Enter directory to save results: /invalid/path
Invalid directory path. Try again.


---

6. Saving Results to File

Function: save_to_file

Saves BMI result into a .txt file

Default filename: bmi_result.txt

Uses Path.write_text()


Output example:

Result saved at: /home/user/bmi_result.txt

If an error occurs:

Error saving file: [error message]
Failed to save result.


---

7. Main Program Flow

Function: main

Execution steps:

1. Display program title


2. Get height input


3. Get weight input


4. Calculate BMI


5. Classify BMI


6. Format result


7. Ask for save directory


8. Save output file


9. Display final status




---

Example Usage

Run Script

python script.py


---

Input Session

=== BMI Calculator ===
Enter height (meters): 1.75
Enter weight (kg): 70
Enter directory to save results: /home/user/results


---

Output

Result saved at: /home/user/results/bmi_result.txt


---

Code Structure

Core Functions

Function	Purpose

get_float_input()	Validates numeric input
calculate_bmi_value()	Computes BMI
classify_bmi()	Categorizes BMI result
format_result()	Formats output text
get_valid_directory()	Validates save path
save_to_file()	Writes result to file
main()	Controls program flow



---

Design Decisions

1. Strong Input Validation

Prevents invalid BMI calculations by enforcing:

Numeric input only

Positive values only



---

2. Separation of Concerns

Each function handles a single responsibility:

Calculation

Classification

Formatting

File handling



---

3. Safe File Writing

Uses Path.write_text() with error handling to avoid crashes.


---

4. User-Controlled Output Location

Users choose where results are saved instead of fixed paths.


---

Limitations

No GUI interface

No unit conversion (e.g., cm to meters)

No historical tracking of BMI results

No health recommendations beyond classification

No database storage



---

Possible Improvements

Feature Enhancements

Add metric/imperial unit support

Add BMI history tracking

Add health advice based on BMI

Export results as PDF or CSV


UX Improvements

Add GUI (Tkinter / web app)

Add charts for BMI trends

Add voice input/output support


Technical Improvements

Add logging system

Add configuration file support

Add test coverage (unit tests)



---

Formula Reference

BMI = weight (kg) / height (m)^2


---

License

This script is free to use, modify, and distribute for personal or commercial purposes.
