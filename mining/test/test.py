import os
import numpy as np
from params import *
import pandas as pd
from utils import *
# def get_position(line):






if __name__ == "__main__":
    # for team in TEAM_NAMES:

        # log = open(LOGS_DIR + team + '.rcg', "r")
        # i = 0
        # playmode = "kick_off_l"
        # for frame in log:
        #     if frame.split()[0] == '(playmode':
        #         playmode = frame.split()[2]
        #     # print(playmode)
        #     frame = frame.split("((")
        #     frame = frame[0].split()
        #     i += 1
        #     if i > 294:
        #         print(int(frame[1]))
        #         break
        
        # break
    # data = np.zeros()
    # print(data)
    # for name in TEAM_NAMES:
    #     data = pd.read_csv(CVS_DIR + name + ".csv").values
    #     print(data[0,:])

    # name_columns = Dataset().name_columns
    # data = np.ndarray((CYCLES*len(TEAM_NAMES), len(name_columns)))
    # for i in range(len(TEAM_NAMES)):
    #     df = pd.read_csv(CVS_DIR + TEAM_NAMES[i] + ".csv")
    #     # print(df.index)
    #     select = df.loc[df.index < 10]
    #     print(type(select))

    name_columns = Dataset().name_columns
    for i in range(len(TEAM_NAMES)):
        df = pd.read_csv(CVS_DIR + TEAM_NAMES[i] + ".csv")
        select = df.loc[df.index < 10]
        print(len(select))
        if i == 0:
            data = select
        else:
            data = pd.concat([data, select])

    dataset = pd.DataFrame(data, columns=name_columns)
    print(dataset)   
    
  
            