#%%

class Chair:
    def __init__(self, color, number_of_legs):
        if int != type(number_of_legs):
            raise ValueError("legs must be an int")

        self.color = color
        self.number_of_legs = number_of_legs

chair1 = Chair("black", 4)
chair2 = Chair("white", 4)
chair3 = Chair("potato", True)

print(chair1.color)
print(chair1.number_of_legs)

# %%

def say_hello(first_name = "", middle = "", last_name = ""):
    print("hello " + first_name + " " + last_name)

say_hello("Alexis")
say_hello(first_name = "Alexis", second_name = "Sanchez")
say_hello()


#%%
def one():
    name = "Aron"


def two():
    print(name)
#%%

class Counter:
    def __init__(self, number_of_people = 0):
        self.number_of_people = number_of_people

    def increase(self):
        self.number_of_people += 1


counter1 = Counter()
counter2 = Counter()

counter1.increase()
counter2.increase()

print(counter1.number_of_people)
print(counter2.number_of_people)
# %%
