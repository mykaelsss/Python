# # x = [ [5,2,3], [10,8,9] ]
# # students = [
# #     {'first_name':  'Michael', 'last_name' : 'Jordan'},
# #     {'first_name' : 'John', 'last_name' : 'Rosales'}
# # ]
# # sports_directory = {
# #     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
# #     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# # }
# # z = [ {'x': 10, 'y': 20} ]

# # x[1] [0] = 15
# # print(x)

# # students[0] ["last_name"] = "Bryant"
# # print(students[0])

# # sports_directory["soccer"][0] = "Andres"
# # print(sports_directory)

# # z[0] ["y"]= 30
# # print(z)


# from optparse import Values


# # def iterateDictionary(some_list):
# #     for i in range(len(students)):
# #         print("first_name - "+students[i]['first_name']+", last_name - "+students[i]['last_name'])


# # students = [
# #         {'first_name':  'Michael', 'last_name' : 'Jordan'},
# #         {'first_name' : 'John', 'last_name' : 'Rosales'},
# #         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
# #         {'first_name' : 'KB', 'last_name' : 'Tonel'}
# #     ]
# # iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel



# # def iterateDictionary2(key_name, some_list):
# #     for i in range(len(some_list)):
# #         print(some_list[i][key_name])

# # iterateDictionary2("first_name" , students)
# # iterateDictionary2("last_name" , students )



# # def printInfo(some_dict):
# #     for key in some_dict:
# #         print(len(some_dict[key]), key.upper())
# #         for name in some_dict[key]:
# #             print(name)
# #         print()




# # dojo = {
# #     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
# #     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# # }
# # printInfo(dojo)
# # output:
# # 7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank

# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon


# # class Shoe:
# #     # now our method has 4 parameters (including self)!
# #     def __init__(self, brand, shoe_type, price, ):
# #     	# we assign them accordingly
# #         self.brand = brand
# #         self.type = shoe_type
# #         self.price = price
# #         # the status is set to True by default
# #         self.in_stock = True

# # skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
# # dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
# # print(skater_shoe.type)	# output: Low-top Trainers
# # print(dress_shoe.type)	# output: Ballet Flats
# # basketball_shoe = Shoe("Jordans", "Air Jordan 4", 199.99)
# # basketball_shoe.in_stock = False
# # print(basketball_shoe.in_stock)
# # Ninja Challenges!
# # Open this code on the Trace website to get a better view of all the variables and their attributes.
# # Make a new instance of a shoe
# # Update the in_stock attribute to False



# class Shoe:

#     def __init__(self, brand, shoe_type, price):
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         self.in_stock = True

#     # Takes a float/percent as an argument and reduces the
#     # price of the item by that percentage.
#     def on_sale_by_percent(self, percent_off):
#         self.price = self.price * (1-percent_off)

#     # Returns a total with tax added to the price.
#     def total_with_tax(self, tax_rate):
#         tax = self.price * tax_rate
#         total = self.price + tax
#         return total

#     # Reduces the price by a fixed dollar amount.
#     def cut_price_by(self, amount):
#         if amount < self.price:
#             self.price -= amount
#         else:
#             print("Price deduction too large.")

# # Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
# my_shoe = Shoe("Converse", "Low-tops", 36.00)
# print(my_shoe.total_with_tax(0.05))
# my_shoe.cut_price_by(10)
# print(my_shoe.price)
# my_shoe1 = Shoe("Jordan", "Bred 4", 500.00)
# print(my_shoe1.total_with_tax(0.09))
# print(my_shoe1.on_sale_by_percent(0.3))



class Player:
    def __init__(self, key ):
        self.keys = key

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position)
# Uncomment the line below to test
player_kevin = Player(kevin)



# class Parent:
#     def method_a(self):
#         print("invoking PARENT method_a!")
# class Child(Parent):
#     def method_a(self):
#         print("invoking CHILD method_a!")
# dad = Parent()
# son = Child()
# dad.method_a()
# son.method_a() #notice this overrides the Parent method!


# favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
# print(f'Your favorite color is: {favorite_color}') #output, prints the color given to the console
