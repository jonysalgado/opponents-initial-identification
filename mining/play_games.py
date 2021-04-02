import os
from params import *
from tqdm import trange

def play_games():
    left_name = "ITAndroids"

    # Check if folder teams are here
    if "teams" not in os.listdir(os.getcwd()+"/../"):
        print("Binaries are not found, please add folder")
        print("\"teams\" in the root of this project.")
        return       

    # Check if not exist logs and csv folder
    if "logs" not in os.listdir(os.getcwd()+"/../"):
        os.system("cd .. && mkdir logs")
        os.system("cd mining")
    
    if "csv" not in os.listdir(os.getcwd()+"/../"):
        os.system("cd .. && mkdir csv")
        os.system("cd mining")

    # remove old games
    for f in os.listdir(os.getcwd()+"/../logs"):
            os.system("rm " + os.getcwd() + "/../logs/" + f + "\n")
        
    # Load teams
    load_left = LEFT_DIR + ' -t ' + left_name
    for match in trange(NUMBER_MATCHES):
        for team in TEAM_NAMES:
            load_right = os.getcwd() + "/../teams/" + team + "/start.sh"
            os.system(SERVER_FAST + '\n')
            os.system('sleep 5 \n')
            os.system(load_left + '\n')
            os.system(load_right + '\n')    
            os.system('sleep 5 \n')
            os.system(ROBOCUP_MONITOR_DIR + ' --auto-quit-mode on' + '\n')
            os.system('killall rcssserver\n')
        
        
    os.system("rm " + LOGS_DIR + "*.rcl" + "\n")
    list_of_logs = os.listdir(LOGS_DIR)
    list_of_logs = sorted(list_of_logs)
    for match in range(NUMBER_MATCHES):
        for i in range(len(TEAM_NAMES)):
            index = i + match * len(TEAM_NAMES)
            os.rename(LOGS_DIR + list_of_logs[index], LOGS_DIR + 
                TEAM_NAMES[i] + "_" + str(match + 1) + ".rcg")


        





    