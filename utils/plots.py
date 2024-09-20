import matplotlib.pyplot as plt
import numpy as np

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