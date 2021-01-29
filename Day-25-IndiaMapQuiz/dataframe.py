import pandas as pd

class Dataframe:

    def __init__(self):
        self.df = pd.read_csv('28_states.csv')
        self.state_list = self.df['state'].to_list()
        self.x_list = self.df['x'].to_list()
        self.y_list = self.df['y'].to_list()

    def get_data(self,state):
        self.index = self.state_list.index(state.title())
        # .item() returns actual cell value
        self.x = self.x_list[self.index]
        self.y = self.y_list[self.index]
        self.state = self.state_list[self.index ]