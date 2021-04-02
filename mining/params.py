import os

LOGS_DIR = os.getcwd()+"/../logs/"

CSV_DIR = os.getcwd()+"/../csv/"

CYCLES = 50

NUMBER_MATCHES = 1	

ROBOCUP_SERVER_DIR = os.getcwd() + "/../../RoboCup_server/rcssserver-16.0.0/src/rcssserver"
ROBOCUP_MONITOR_DIR = os.getcwd() + "/../../RoboCup_server/rcssmonitor-16.0.0/src/rcssmonitor"

LEFT_DIR = os.getcwd() + "/../teams/ITAndroids2020/start.sh"

TEAM_NAMES = ["helios", "hillstone", "rione", "robocin", "RobotBulls"]
# server params

SERVER_FAST = 	ROBOCUP_SERVER_DIR + \
				' server::auto_mode=true ' + \
			    'server::synch_mode=true ' + \
			    'server::game_log_version=5 ' + \
			    "server::text_log_dir='../logs' "+\
			    'server::penalty_shoot_outs=false ' + \
			    'server::nr_extra_halfs=0' + \
			    ' > /dev/null &'

PLAYERS_NUMBER = 11