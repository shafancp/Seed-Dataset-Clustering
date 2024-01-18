import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define column names for the dataset
cols = ["area", "perimeter", "compactness", "length", "width", "asymmetry", "groove", "class"]

# Load the dataset from "seed.txt" using Pandas, specifying column names and separator
df = pd.read_csv('/content/seed.txt', names=cols, sep="\s+")

# Display the first few rows of the DataFrame
df.head()

# Data Visualization: Scatter plots for all pairs of variables (except the last column "class")
for i in range(len(cols) - 1):
    for j in range(i + 1, len(cols) - 1):
        x_label = cols[i]
        y_label = cols[j]
        
        # Scatter plot using Seaborn, color points by the "class" variable
        sns.scatterplot(x=x_label, y=y_label, data=df, hue='class')
        plt.show()

## Clustering

# Choose two columns for clustering: "perimeter" and "asymmetry"
x = "perimeter"
y = "asymmetry"
X = df[[x, y]].values

# Perform KMeans clustering with 3 clusters
kmeans = KMeans(n_clusters=3).fit(X)
clusters = kmeans.labels_

# Display the original "class" values and the assigned cluster labels
print(df["class"].values)
print(clusters)

# Create a new DataFrame with selected features, cluster labels, and the "class" variable
cluster_df = pd.DataFrame(np.hstack((X, clusters.reshape(-1, 1))), columns=[x, y, "class"])

# Visualize the clustered data using a scatter plot, color points by assigned cluster
sns.scatterplot(x=x, y=y, hue='class', data=cluster_df)
plt.plot()
