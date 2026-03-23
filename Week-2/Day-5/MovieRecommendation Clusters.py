import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("movie_recommendation_dataset.csv")

print(df.head())

# Group by User and take average preference
user_profile = df.groupby("UserID")[["Action","Romance","Comedy"]].mean()

print("\nUser Profiles:\n", user_profile.head())



kmeans = KMeans(n_clusters=3, random_state=42)
user_profile["Cluster"] = kmeans.fit_predict(user_profile)

print("\nClustered Users:\n", user_profile.head())



def recommend_movies(user_id):

    user_cluster = user_profile.loc[user_id, "Cluster"]

    similar_users = user_profile[user_profile["Cluster"] == user_cluster].index

    recommended = df[df["UserID"].isin(similar_users)]

    user_movies = df[df["UserID"] == user_id]["MovieName"]
    recommended = recommended[~recommended["MovieName"].isin(user_movies)]

    recommended = recommended.sort_values(by="Rating", ascending=False)

    return recommended[["MovieName","Rating"]].drop_duplicates().head(5)


user_id = 4
print(f"\nRecommended Movies for User {user_id}:")
print(recommend_movies(user_id))


###########                OUTPUT                ##########
   UserID     MovieName  Action  Romance  Comedy  Rating
0       1      Avengers       3        2       4       3
1       1  Interstellar       4        2       3       3
2       1         Joker       4        3       3       3
3       2  Forrest Gump       3        2       3       3
4       2    Spider-Man       3        1       2       2

User Profiles:
           Action   Romance    Comedy
UserID                              
1       3.666667  2.333333  3.333333
2       2.666667  1.333333  3.000000
3       3.666667  2.333333  2.000000
4       2.400000  2.600000  3.000000
5       2.333333  3.000000  2.666667

Clustered Users:
           Action   Romance    Comedy  Cluster
UserID                                       
1       3.666667  2.333333  3.333333        2
2       2.666667  1.333333  3.000000        2
3       3.666667  2.333333  2.000000        2
4       2.400000  2.600000  3.000000        1
5       2.333333  3.000000  2.666667        1

Recommended Movies for User 4:
        MovieName  Rating
69             Up       4
67          Shrek       4
70      Inception       4
129        Frozen       4
131  Forrest Gump       4
