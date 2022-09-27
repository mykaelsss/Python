




class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        # print(self.__dict__)
        for key, value in self.__dict__.items():
            print(f"{key} : {value}")
        return self

    def enroll(self, pointIncrease):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
        self.gold_card_points += pointIncrease
        return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount :
            self.gold_card_points -= amount
        return self

user1 = User("Mykael", "Sicard", "mykaels@gmail.com", 18)
user1.display_info().enroll(200).spend_points(50).display_info()





user2 = User("Seki", "Sicard", "sekis@gmail.com", 18)
user2.enroll(200).spend_points(80).display_info()



user3 = User("Kio", "Sicard,", "kios@gmail.com", 20)
user3.spend_points(40).display_info()
