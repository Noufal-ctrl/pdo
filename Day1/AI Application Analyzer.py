ai_systems = {
    "ChatGPT": "NLP",
    "Google Translate": "NLP",
    "Siri": "NLP",
    "Alexa": "NLP",
    "Grammarly": "NLP",

    "Tesla Autopilot": "Computer Vision",
    "Face ID": "Computer Vision",
    "Google Lens": "Computer Vision",
    "Self Driving Car": "Computer Vision",
    "Security Camera AI": "Computer Vision",

    "Netflix": "Recommendation System",
    "Amazon": "Recommendation System",
    "YouTube": "Recommendation System",
    "Spotify": "Recommendation System",
    "Instagram Feed": "Recommendation System",

    "Fraud Detection": "Machine Learning",
    "Spam Filter": "Machine Learning",
    "Stock Predictor": "Machine Learning",
    "Medical Diagnosis AI": "Machine Learning",
    "Weather Prediction AI": "Machine Learning"
}


category_count = {}

for system, category in ai_systems.items():
    category_count[category] = category_count.get(category, 0) + 1


sorted_categories = sorted(category_count.items(), key=lambda x: x[1])


for category, count in sorted_categories:
    print(category, ":", count)


###           Output         ###
NLP : 5
Computer Vision : 5
Recommendation System : 5
Machine Learning : 5
