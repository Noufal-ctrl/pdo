import json

# Convert seconds
def convert_time(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"

# score mapping
def get_score(action):
    if action == "click":
        return 1
    elif action == "purchase":
        return 5
    return 0

with open("input.json", "r") as f:
    data = json.load(f)

output_data = []
for record in data:
    new_record = {
        "user": record["user"],
        "action": record["action"],
        "time_readable": convert_time(record["time"]),
        "score": get_score(record["action"])
    }
    output_data.append(new_record)

# new file
      
with open("output.json", "w") as f:
    json.dump(output_data, f, indent=4)

print("Pipeline executed successfully!")

#########          OUTPUT            ##########
Pipeline executed successfully!
