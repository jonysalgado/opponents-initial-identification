import pandas as pd
import numpy as np
from params import PLAYERS_NUMBER, CSV_DIR, TEAM_NAMES, CYCLES, NUMBER_MATCHES


def create_final_dataset():
    name_columns = Dataset().name_columns
    for match in range(NUMBER_MATCHES):
        for i in range(len(TEAM_NAMES)):
            df = pd.read_csv(CSV_DIR + TEAM_NAMES[i] + "_" + str(match + 1) + ".csv")
            select = df.loc[df.index < CYCLES]
            if i == 0 and match == 0:
                data = select
            else:
                data = pd.concat([data, select])

    dataset = pd.DataFrame(data, columns=name_columns)
    dataset.to_csv(CSV_DIR + "dataset.csv")


class Pose:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, x, y):
        self.x += x
        self.y += y

    def division(self, n):
        self.x /= n
        self.y /= n

class Player:
    def __init__(self):
        self.position = []

class Ball():
    def __init__(self):
        self.position = []

class Dataset:

    def __init__(self):
        self.players_itandroids = self.init_players()
        self.players_teams = self.init_players()
        self.itandroids_center = Ball()
        self.ball = Ball()
        self.name_columns = self.init_name_columns()
        self.frames = []
        self.name_team = []
        self.dataset = []

    def init_players(self):
        players = []
        for i in range(PLAYERS_NUMBER):
            players.append(Player())
        return players
    
    def init_name_columns(self):
        name_columns = ['frame', 'b x', 'b y']
            # 'ITandroids center of mass x', 'ITandroids center of mass y']
        for i in range(PLAYERS_NUMBER):
            name_columns.append('r' + str(i+1) + ' x')
            name_columns.append('r' + str(i+1) + ' y')
        name_columns.append('team name')
        return name_columns

    def add_position(self, frame, team_name):
        self.add_ball_position(frame[1])
        self.add_players_positions(frame)
        self.add_frame(frame)
        self.name_team.append(team_name)

    def add_frame(self, frame):
        self.frames.append(int(frame[0].split()[1]))

    def add_ball_position(self, ball_frame):
        ball_frame = ball_frame.split()
        x, y = ball_frame[1], ball_frame[2]
        self.ball.position.append(Pose(x, y))
        
    def add_players_positions(self, frame):
        center_mass = Pose(0, 0)
        for i in range(PLAYERS_NUMBER):
            # ITAndroids player
            player_frame = frame[i+2]
            player_frame = player_frame.split()
            x, y = player_frame[4], player_frame[5]
            center_mass.addition(float(x), float(y))
            self.players_itandroids[i].position.append(Pose(x, y))
            # Other players
            player_frame = frame[i+13]
            player_frame = player_frame.split()
            x, y = player_frame[4], player_frame[5]
            self.players_teams[i].position.append(Pose(x, y))
        
        center_mass.division(PLAYERS_NUMBER)
        self.itandroids_center.position.append(center_mass)

    
    def create_dataset(self):
        dataset = {}
        for element in self.name_columns:
            if element == 'frame':
                dataset[element] = self.frames
                continue
            if element == 'team name':
                dataset[element] = self.name_team
                continue
            if element[-1] == 'x':
                x_or_y = 'x'
            else:
                x_or_y = 'y'

            if element[0] == 'b':
                dataset[element] = self.get_list(self.ball, x_or_y)
            elif element[0] == 'r':
                number = int(element[1]) - 1
                dataset[element] = self.get_list(self.players_itandroids[number], x_or_y)
            # else:
            #     dataset[element] = self.get_list(self.itandroids_center, x_or_y)
            
            
        self.dataset = pd.DataFrame(dataset,columns= self.name_columns)
        return self.dataset
        
    def get_list(self, list_pose, x_or_y):
        column = []
        if x_or_y == 'x':
            for pose in list_pose.position:
                column.append(pose.x)
        else:
            for pose in list_pose.position:
                column.append(pose.y)

        return column