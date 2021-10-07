import csv
import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    df = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
    return df
