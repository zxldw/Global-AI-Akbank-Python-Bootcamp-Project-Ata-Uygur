import csv
import datetime

# Bütün pizzaların parentclass'ı


class Pizza:
    description = None
    price = None


    def get_description(self):
        print(self.description)

    def get_cost(self):
        print(self.price)


class Decorator():

    @staticmethod
    def get_cost(pizza_cost, sauce_cost):
        return pizza_cost + sauce_cost

    @staticmethod
    def get_description(pizza_desc, sauce_desc):
        return pizza_desc + sauce_desc

##################################################################

############################## Pizza Çeşitlerinin Classları
class Classic(Pizza):
    description = "A pizza for people that prefers less variety of ingredients and loves classic pizza taste. "
    price = 70


class Margherita(Pizza):
    description = "The real Italian pizza, beautiful combination of tomato and mozarella. "
    price = 85


class TurkPizza(Pizza):
    description = "For people that loves both vegetables and meat. "
    price = 90


class PlainPizza(Pizza):
    description = "Special pizza of globally well-known pizza restaurant. "
    price = 60


####################################### Sos Çeşitlerinin Classları


class Olives(Decorator):
    description = "A refreshing sour aroma of olives."
    price = 3


class Mushrooms(Decorator):
    description = "A creamy sauce that perfectly combine with all kinds of pizzas."
    price = 4


class GoatCheese(Decorator):
    description = "Love cheese? This quality cheese is just the thing you are looking for!"
    price = 6


class Meat(Decorator):
    description = "Can't get enough of meat? Why not a meat sauce on a meaty pizza."
    price = 7


class Onions(Decorator):
    description = "For people that loves creamy,bitter and hot sauces."
    price = 4


class Corn(Decorator):
    description = "An interesting alternative to vegetable-based sauces."
    price = 3
###################################################


def main():
    menu_file = open('menu.txt', 'r')
    menu = menu_file.read()

    print(menu)

    menu_file.close()

    while 1:
        input_pizza = int(input("Insert the associated number of pizza you want to select:"))
        input_sauce = int(input("Insert the associated number of sauce you want to select:"))

        try:
            if input_pizza == 1:
                ordered_pizza = Classic()
            elif input_pizza == 2:
                ordered_pizza = Margherita()
            elif input_pizza == 3:
                ordered_pizza = TurkPizza()
            elif input_pizza == 4:
                ordered_pizza = PlainPizza()

            if input_sauce == 11:
                ordered_sauce = Olives()
            elif input_sauce == 12:
                ordered_sauce = Mushrooms()
            elif input_sauce == 13:
                ordered_sauce = GoatCheese()
            elif input_sauce == 14:
                ordered_sauce = Meat()
            elif input_sauce == 15:
                ordered_sauce = Onions()
            elif input_sauce == 16:
                ordered_sauce = Corn()


            total_cost = Decorator.get_cost(ordered_pizza.price,ordered_sauce.price)
            total_desc = Decorator.get_description(ordered_pizza.description, ordered_sauce.description)
            print("Total price is:"+str(total_cost))
            print("Description:"+ total_desc)
            break

        except:
            print("Invalid selection please insert valid values.")
            continue

    payment = total_cost
    Username = input("Please insert your name:")
    User_id = input("Please insert your ID:")
    Credit_number = input("Please insert your credit card number:")
    Credit_password = input("Please insert your credit card password:")

    now = datetime.datetime.now()
    Order_time = now.strftime("%H:%M:%S")

    infos = [Username,User_id,total_cost,Credit_number,Credit_password,total_desc,Order_time]
    # Writing to csv file

    # open the file in the write mode
    with open("Orders_Database.csv", 'a', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(infos)

    return



main()

