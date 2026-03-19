import random
import matplotlib.pyplot as plt

dataset = [
    {"hours_studied": random.randint(1, 10), "score": random.randint(40, 100)} 
    for _ in range(30) 
]


avg_hours = sum(s["hours_studied"] for s in dataset) / len(dataset)
avg_score = sum(s["score"] for s in dataset) / len(dataset)

top_student = max(dataset, key=lambda x: x["score"])

print(f"Average hours studied: {avg_hours:.2f}")
print(f"Average score: {avg_score:.2f}")
print(f"Highest Score: {top_student['score']} (Hours: {top_student['hours_studied']})")


hours = [s["hours_studied"] for s in dataset]
scores = [s["score"] for s in dataset]

plt.scatter(hours, scores, color='blue', label='Students')
plt.axvline(avg_hours, color='green', linestyle='--', label='Avg Hours')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Student Performance Analysis')
plt.legend()
plt.show()

##########              OUTPUT              ##########
Average hours studied: 4.53
Average score: 68.60
Highest Score: 98 (Hours: 6)
