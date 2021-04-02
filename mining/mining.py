import shlex
import os
import subprocess
from params import LOGS_DIR
from play_games import play_games

def verification_logs_dir():

    for f in os.listdir(LOGS_DIR):
        if f.endswith(".rcg"):
            return True
    
    return False

def answer_user():
    
    answer = input("Do you want to play games again?(y/n) \n")
    while answer not in ["y", "Y", "n", "N"]:
        answer = input("Do you want to play games again?(y/n) \n")
    if answer in ["y", "Y"]:
        return True
    return False

if __name__ == "__main__":

    if verification_logs_dir():
        if answer_user():
            play_games()
    else:
        play_games()
