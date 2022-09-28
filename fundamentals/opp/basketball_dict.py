
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team




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

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
player_jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])
player_kyrie = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])
player_dame = Player(dame["name"], dame["age"], dame["position"], dame["team"])
player_joel = Player(joel["name"], joel["age"], joel["position"], joel["team"])
player_demar = Player(demar["name"], demar["age"], demar["position"], demar["team"])


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
