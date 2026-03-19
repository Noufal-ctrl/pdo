import random

dataset = [
    {"hours_studied": random.randint(1, 10), "score": random.randint(40, 100)} 
    for _ in range(30)
]

total_hours = sum(student["hours_studied"] for student in dataset)
total_score = sum(student["score"] for student in dataset)

avg_hours = total_hours / len(dataset)
avg_score = total_score / len(dataset)

print(f"Dataset Sample: {dataset[:5]}...")
print(f"Average hours studied: {avg_hours:.2f} hours")
print(f"Average score: {avg_score:.2f}")

##########              OUTPUT              ##########
Dataset Sample: [{'hours_studied': 6, 'score': 55}, {'hours_studied': 6, 'score': 78}, {'hours_studied': 1, 'score': 98}, {'hours_studied': 5, 'score': 77}, {'hours_studied': 5, 'score': 54}]...
Average hours studied: 5.30 hours
Average score: 69.07
