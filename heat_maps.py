import pandas as pd
import numpy as np
import seaborn as sns

fig_length = 11.7
fig_width = 8.27

def heatmap(df):
    df = df[['x', 'y', 'ppscore']].pivot(columns='x', index='y', values='ppscore')
    ax = sns.heatmap(df, vmin=0, vmax=1, cmap="Blues", linewidths=0.5, annot=True)
    ax.set_title("PPS matrix")
    ax.set_xlabel("feature")
    ax.set_ylabel("target")
    ax = sns.set(rc={'figure.figsize':(fig_length,fig_width)})
    return ax


def corr_heatmap(df):
    ax = sns.heatmap(df, vmin=-1, vmax=1, cmap="BrBG", linewidths=0.5, annot=True)
    ax.set_title("Correlation matrix")
    ax = sns.set(rc={'figure.figsize':(fig_length,fig_width)})
    return ax



