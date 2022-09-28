
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

  # * NINJA BONUS class mehotd
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects

    # Not required for the assignment but useful
    # __repr__(self) is a python system method that
    # tells python how to handle representing that class
    # when, for example the object is printed to the terminal.
    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display


kevin = {
    "name": "Kevin Durant",
    "age":34,
    "position": "small forward",
    "team": "Brooklyn Nets"
    }

jason = {
    "name": "Jason Tatum",
    "age":24,
    "position": "small forward",
    "team": "Boston Celtics"
    }

kyrie ={
    "name": "Kyrie Irving",
    "age":32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
    }

dame = {
    "name": "Damian Lillard",
    "age":33,
    "position": "Point Guard",
    "team": "Portland Trailblazers"
    }

joel = {
    "name": "Joel Embiid",
    "age":32,
    "position": "Power Foward",
    "team": "Philidelphia 76ers"
    }

demar = {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_dame = Player(dame)
player_joel = Player(joel)
player_demar = Player(demar)


print(player_demar.position)
print(player_kyrie.age)
print(player_jason.team)
print(player_kevin.team)
print(player_dame.position)
print(player_joel.name)











# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# # Pass in all the values from the dictionary by their keys
# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
# print(player_kevin.team) # prints small forward
