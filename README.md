# Grade Evaluator - Lab 1

A small tool that reads assignment scores from a CSV file, validates them, calculates a final grade and GPA, checks pass/fail status, and flags formative assignments eligible for resubmission.

## Files

- grade-evaluator.py -- Reads grades.csv, validates scores/weights, calculates the final grade and GPA, determines pass/fail per category, and lists which formative assignment(s) qualify for resubmission.
- grades.csv -- Sample data: assignment name, group (Formative/Summative), score (0-100), and weight.
- organizer.sh -- Archives the current grades.csv (with a timestamp) into an archive/ folder, creates a fresh empty grades.csv, and logs every run to organizer.log.

## How it works

### grade-evaluator.py

1. Run it and enter the CSV filename when prompted (e.g. grades.csv).
2. It validates that every score is between 0 and 100, and that weights total exactly 100, with Formative = 60 and Summative = 40.
3. It calculates the Total Grade as the sum of score times weight divided by 100 for every assignment, and GPA as (Total Grade / 100) times 5.0.
4. It determines Pass/Fail: the student must score at least 50% in both the Formative and Summative categories.
5. If any formative assignments scored below 50, it lists the one(s) with the highest weight (including ties) as eligible for resubmission.

Run it with: python3 grade-evaluator.py

### organizer.sh

Run this to reset grades.csv for a new grading cycle while keeping a timestamped backup of the old data: ./organizer.sh

This creates archive/grades_<timestamp>.csv, overwrites grades.csv with just the header row, and appends a record of the action to organizer.log.
