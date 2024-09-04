class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        str=[]
        str.append(f"Player: {self.__name}")
        str.append(f"Endurance: {self.__endurance}")
        str.append(f"Sprint: {self.__sprint}")
        str.append(f"Dribble: {self.__dribble}")
        str.append(f"Passing: {self.__passing}")
        str.append(f"Shooting: {self.__shooting}")
        return "\n".join(str)
    

class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.__name} has already joined"
        else:
            self.__players.append(player)
            return f"Player {player.__name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player.__name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"
    
