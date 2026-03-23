import pandas as pd
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("spam_email_dataset.csv")
X=df[["email_length", "num_links", "num_spam_words"]]
Y=df["label"]
model=LogisticRegression()
model.fit(X,Y)
new_email = [[100, 3, 0]]

prob = model.predict_proba(new_email)[0][1]
prediction = model.predict(new_email)[0]

print("Spam Probability =", round(prob, 2))
print("Prediction =", "Spam" if prediction == 1 else "Not Spam")

##########                OUTPUT                ##########
Spam Probability = 0.0
Prediction = Not Spam

