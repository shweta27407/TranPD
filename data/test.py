import pandas as pd

csv_path = "/Users/shwetabambal/Documents/myrepos/TranPD/data/DMC2_S_CP2_52.csv"
target = "CURRENT|6"


df = pd.read_csv(csv_path)


print("Original CSV shape:", df.shape)
# print("Shape of y_scaled:", y_scaled.shape)
# print("Sliding window output:", X_all.shape)
# print("X_all_df shape:", X_all_df.shape)