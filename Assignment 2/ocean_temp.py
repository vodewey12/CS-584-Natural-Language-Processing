import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def graph_ocean(file_name: str):
    df = pd.read_csv(file_name)
    print(df.head())
    
if __name__ == '__main__':
    graph_ocean('A2ocean_temp.csv')