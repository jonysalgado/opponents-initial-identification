import sys
import os
import subprocess



if __name__ == "__main__":
    command = "cd mining && python mining.py;"
    # a team put formations.bin in the directory
    command += "rm formations.bin;"
    command += " python parse_log.py;"
    command += " cd .. &&"
    command += " rm prediction/datasets/dataset.csv &&"
    command += " rm prediction/datasets/new_dataset.csv;"
    command += " cp --archive csv/dataset.csv prediction/datasets/dataset.csv;"
    command += " cd prediction/Knn && cmake CMakeLists.txt;"
    command += " make;"
    
    os.system(command)


    
