import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    two_dim_list = []  # snake case ftw (PEP8)
    with open(csv_file_path, 'r') as f:
        r = csv.reader(f, delimiter=',')
        # next(r)  # skip header line if necessary
        for row in r:
            two_dim_list.append(row)
    return two_dim_list
