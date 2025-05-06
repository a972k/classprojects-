import json
import os

file_path = "books.json"
 
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
else:
        data = {"books": []}
        
print("current books:")
for book in data["books"]:
    avg_rating = sum(book["ratings"]) / len(book["ratings"]) if book["ratings"] else 0
    print(f"{book['title']} - Average Rating: {avg_rating:.2f}")
            
exists = any(book["title"].lower() == "json basics".lower() for book in data["books"])
if not exists:
    next_id = max((book["id"] for book in data["books"]), default=0) + 1
    new_book = {
        "id": next_id,
        "title": "json basics",
        "author": "Aws9 Team",
        "ratings": [5, 5, 4]
    }
    
    data["books"].append(new_book)
    print(f"\nAdded new book: {new_book['title']}")
    

for book in data["books"]:
    title_name = book["title"].lower()
    if "python" in title_name:
        book["categiory"] = "Python"
    elif "javascript" in title_name:
        book["categiory"] = "JavaScript"
    else:
        book["categiory"] = "Other"
        
        
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)     
    
