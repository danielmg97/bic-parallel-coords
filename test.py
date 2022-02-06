import os
from bic_parallel_coords import BiclusterVisualizer

"""
Usage instructions:
    1. Place your dataset files in the data/input/ directory.
        - The file's name should be suffixed with either "_categories" or "_coordinates", according to the plot type.
        - Currently, only .arff, .csv, and .txt data files are supported (see the examples provided).
    2. Place your bicluster files in the data/output/ directory.
        - The file's name should be the same as the input file without the suffix, for correspondence reasons.
        - Currently, only BicPAMS output result files are supported (feel free to override the load_biclusters() in the BiclusterVisualizer class).
    3. Run the script with the following command:
        - python3 test.py
"""

data_folder = './data/input/'
bic_folder = "./data/output/"
for data_filename in os.listdir(data_folder):
    print("Now processing",data_filename,"...")
    viz = BiclusterVisualizer()
    df, main_var = viz.load_data(data_folder+data_filename)
    results = viz.load_biclusters(bic_folder+data_filename.split(".")[0].split("_")[0]+".txt")
    for bic in results[0]:
        viz.plot_bicluster(bic,df,main_var,folder_name=data_filename.split(".")[0],mode=data_filename.split(".")[0].split("_")[1])
print("Done!")  