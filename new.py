import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Load the data
df = pd.read_csv("AI_Datasetcsv.csv")

# Select the features for clustering
X = df[['customer_age', 'current_loan_amount']].copy()

# Fit GMM model
n_clusters = 5
gmm_model = GaussianMixture(n_components=n_clusters)
gmm_model.fit(X)

# Assign clusters to the data
cluster_labels = gmm_model.predict(X)
X = pd.DataFrame(X)
X['cluster'] = cluster_labels

# Plot the clusters
for k in range(0,n_clusters):
    data = X[X["cluster"]==k]
    plt.scatter(data['current_loan_amount'], data['customer_age'])
plt.title("Clusters Identified by Guassian Mixture Model")    
plt.xlabel("current_loan_amount")
plt.ylabel("customer_age")
plt.show()
