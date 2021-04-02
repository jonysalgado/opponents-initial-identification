import os
from params import TEAM_NAMES, LOGS_DIR, CSV_DIR, NUMBER_MATCHES
from utils import Dataset, create_final_dataset

def find_playmode(frame, old_playmode):
    if frame.split()[0] == '(playmode':
        return frame.split()[2]
    else:
        return old_playmode


if __name__ == "__main__":
    datasets = []
    for match in range(NUMBER_MATCHES):
        for i in range(len(TEAM_NAMES)):
            dataset = Dataset()
            log = open(LOGS_DIR + TEAM_NAMES[i] + "_" + str(match + 1) + ".rcg", "r")
            last = 0
            playmode = 'kick_off_l)'
            for frame in log:
                # analyze the playmode
                playmode = find_playmode(frame, playmode)
                if playmode == 'play_on)':
                    # analyze the positions
                    frame = frame.split('((')
                    begin = frame[0].split()
                    if begin[0] == '(show' and int(begin[1]) > last:  
                        dataset.add_position(frame, i)
                    last += 1
            dataset_csv = dataset.create_dataset()
            dataset_csv.to_csv(CSV_DIR + TEAM_NAMES[i] + '_' + str(match + 1) + ".csv")

    
    create_final_dataset()
    