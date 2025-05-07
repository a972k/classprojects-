import json
import os

file_path = "students.json"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)  
else:
    data = {"students": []} 
    
students = data.get("students", [])
print("current students:")

for student in students:
    scores = student.get("scores", [])
    student["avg_score"] = sum(scores) / len(scores) if scores else 0

max_avg = max((s["avg_score"] for s in students), default=0)

for student in students:
    student["status"] = "Winner" if student["avg_score"] == max_avg else "Participant"

for student in students:
    avg_score = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0
    student["avg_score"] = avg_score
    print(f"{student['name']} - average score: {avg_score:.2f}")

max_avg = max(student["avg_score"] for student in students) if students else 0

if students:
    max_avg = max(student.get("avg_score", 0) for student in students)
    
    print("\nWinner(s):")
    for student in students:
        if student.get("avg_score", 0) == max_avg:
            print(f"{student['name']} with average score: {student['avg_score']:.2f}") 
            
def add_student(name, scores):
    if any(s["name"].lower() == name.lower() for s in students):
        print(f"Student '{name}' already exists. Not adding.")
        return
    new_id = max((s["id"] for s in students), default=0) + 1
    avg_score = sum(scores) / len(scores) if scores else 0
    status = "winner" if avg_score == max_avg else "participant"
    students.append({
        "id": new_id,
        "name": name,
        "scores": scores,
        "avg_score": avg_score,
        "status": status
    })
    print(f"added student: {name}")

add_student("Elan", [9, 8, 9])

with open(file_path, "w") as file:
    json.dump({"students": students}, file, indent=4)

print("\nupdated student list saved to students.json.")    
          
print("\nleaderboard:")
leaderboard = sorted(students, key=lambda s: s["avg_score"], reverse=True)

for rank, student in enumerate(leaderboard, start=1):
    print(f"{rank}. {student['name']} - Avg: {student['avg_score']:.2f} - {student['status']}")  
