import InsectClass as I

mosquito = I.Insect('bumblebee', 2, 4)
housefly = I.Insect('housefly', 200, 400)
# housefly and mosquito are objects of the class, Insect

print(mosquito.flight_length())
print(housefly.flight_length())

print(f"The {mosquito.get_name()} can fly up to {mosquito.get_flight()} miles")
print(f"The {housefly.get_name()} can fly up to {housefly.get_flight()} miles")

'''
def main():
    my_insect = I.Insect()

    my_insect.flight_length()

    print(my_insect.get_flight())


main()
'''
