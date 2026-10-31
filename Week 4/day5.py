import csv
import io
import json

csv_data = """name,score1,score2,score3
Moses Wachira,85,70,95
Aaron Ochieng,60,83,80 
Joseph Okonkwo,70,60
Mary Wanjru,70,95,60
John Karanja,80,invalid,70"""

# Functions
def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def calculate_avg(scores):
    valid_scores = [score for score in scores if score is not None]
    if not valid_scores:
        return None
    return round(sum(valid_scores) / len(valid_scores), 1)

def letter_grade(avg_score):
    if avg_score is None: return None
    if avg_score >= 90:   return "A"
    elif avg_score >= 80: return "B"
    elif avg_score >= 70: return "C"
    elif avg_score >= 60: return "D"
    else:                 return "F"

# Process CSV
file = io.StringIO(csv_data)
reader = csv.DictReader(file)
results = []

print("=" * 52)
print(f"{'NAME':<18} {'AVG':>5} {'GRADE':>7}   {'NOTES'}")
print("=" * 52)

for row in reader:
    scores = [
        parse_score(row["score1"]),
        parse_score(row["score2"]),
        parse_score(row["score3"])
    ]
    invalid_count = scores.count(None)
    avg_score = calculate_avg(scores)
    grade = letter_grade(avg_score)
    notes = f"{invalid_count} invalid score(s)" if invalid_count else "All scores valid"
    
    print(f"{row['name']:<18} {str(avg_score):>5} {grade:>5}    {notes}")
    
    results.append({
        "name": row["name"],
        "scores": [row["score1"], row["score2"], row["score3"]],
        "avg_score": avg_score,
        "grade": grade        
    })

    print("=" * 52)

# print report summary
valid_avg_scores = [result["avg_score"] for result in results if result["avg_score"] is not None]
class_avg_score = round(sum(valid_avg_scores) / len(valid_avg_scores), 1)
print(f"\nclass average: {class_avg_score}")
print(f"students: {len(results)}")  

#Export as JSON
print("\nJSON export:")
print(json.dumps(results, indent=2))