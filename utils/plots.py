import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_cluster_comp(clusters, col_name):
    cluster_norms = list()
    for idx, cluster in enumerate(clusters):
        cluster_norm = (cluster[col_name].value_counts().sort_index() / cluster[col_name].value_counts().sum()) * 100
        cluster_norms.append(cluster_norm)
        cluster_norm.plot(kind="bar")
        plt.title("Cluster "+str(idx))
        plt.xlabel(col_name)
        plt.show()
    fig, axes = plt.subplots(1, 1, figsize=(15, 9), sharey=True)

    clusters_stacked = pd.DataFrame({'cluster_'+str(idx): cluster for idx, cluster in enumerate(cluster_norms)})
    clusters_stacked.plot.bar(ax=axes)
    plt.title(f"Bar Graph of Stacked Clusters")
    plt.xlabel(col_name)
    plt.show()
    


def plot_count_of_columns(df, col_name):
    group_df = df.groupby(col_name).count()["origin"]
    group_df_perc = np.round(group_df / group_df.sum() * 100, 2)
    print(f"Number of classes:\n{group_df}")
    print(f"Percentage of classes:\n{group_df_perc}")
    print(group_df.describe())
    group_df_perc.plot(kind="bar")
    plt.ylabel("Percentage")
    plt.show()

def plot_IQR(df, col_name):
    df.plot.box(column=col_name, by="gender", figsize=(10,8))
    plt.show()

def plot_categories_spread(df, col_name):
    df[col_name].value_counts().plot(kind="bar", figsize=(14,8))
    plt.title(col_name)
    plt.show()

