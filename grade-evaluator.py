import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    if not data:
        print("No assignment data found. Add assignments to the CSV and try again.")
        return

    out_of_range = [a for a in data if not (0 <= a['score'] <= 100)]
    if out_of_range:
        print("Error: The following assignments have scores outside the valid 0-100 range:")
        for a in out_of_range:
            print(f"  - {a['assignment']}: {a['score']:g}")
        return

    summative = [a for a in data if a['group'].strip().lower() == 'summative']
    formative = [a for a in data if a['group'].strip().lower() == 'formative']

    total_weight = sum(a['weight'] for a in data)
    summative_weight = sum(a['weight'] for a in summative)
    formative_weight = sum(a['weight'] for a in formative)

    if abs(total_weight - 100) > 0.01:
        print(f"Error: Total weight is {total_weight}, but it must equal exactly 100.")
        return
    if abs(summative_weight - 40) > 0.01:
        print(f"Error: Summative weights total {summative_weight}, but they must equal exactly 40.")
        return
    if abs(formative_weight - 60) > 0.01:
        print(f"Error: Formative weights total {formative_weight}, but they must equal exactly 60.")
        return

    total_grade = sum(a['score'] * a['weight'] / 100 for a in data)
    gpa = (total_grade / 100) * 5.0

    summative_points = sum(a['score'] * a['weight'] / 100 for a in summative)
    formative_points = sum(a['score'] * a['weight'] / 100 for a in formative)
    summative_pct = (summative_points / summative_weight) * 100
    formative_pct = (formative_points / formative_weight) * 100

    passed = summative_pct >= 50 and formative_pct >= 50
    status = "PASSED" if passed else "FAILED"

    failed_formative = [a for a in formative if a['score'] < 50]
    resubmission = []
    if failed_formative:
        highest_weight = max(a['weight'] for a in failed_formative)
        resubmission = [a for a in failed_formative if a['weight'] == highest_weight]

    print(f"Total Grade:         {total_grade:.2f} / 100")
    print(f"GPA:                 {gpa:.2f} / 5.0")
    print(f"Summative Category:  {summative_pct:.2f}%  (weight: {summative_weight:g})")
    print(f"Formative Category:  {formative_pct:.2f}%  (weight: {formative_weight:g})")
    print(f"Final Status:        {status}")

    if resubmission:
        print("\nEligible for Resubmission:")
        for a in resubmission:
            print(f"  - {a['assignment']} (score: {a['score']:g}, weight: {a['weight']:g})")
    else:
        print("\nNo formative assignments are eligible for resubmission.")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
