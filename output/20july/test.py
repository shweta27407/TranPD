import pandas as pd

# Load your dataset
df = pd.read_csv("/Users/shwetabambal/Documents/myrepos/TranPD/output/20july/Peaks_Ws60_Dim32.csv")  # replace with your actual file name

# Count the number of 0s and 1s in the 'Peak' column
peak_counts = df['Peak'].value_counts()

print("Peak = 0:", peak_counts.get(0, 0))
print("Peak = 1:", peak_counts.get(1, 0))