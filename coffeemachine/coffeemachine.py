class MyCoffeeMaker:
#------------------------------------------------------------------------
    def __init__(self):
        """
        Initialize coffee mach with starting value water, milk,
        beans, cups, and money.
        """
        self.water_amount = 400
        self.milk_amount = 540
        self.beans_amount = 120
        self.cups_count = 9
        self.cash_in_machine = 550
        self.machine_state = "waiting_for_action"
#---------------------------------------------------------------
    def show_status(self):
        """
        Prints status coffee mach, showing how much
        water, milk, bean, cups,  money available.
        """
        print("Current coffee machine status:")
        print(f"{self.water_amount} ml water")
        print(f"{self.milk_amount} ml milk")
        print(f"{self.beans_amount} g coffee bean")
        print(f"{self.cups_count} cups")
        print(f"{self.cash_in_machine} money summ")
#---------------------------------------------------------------------
    def check_ingredients(self, req_water, req_milk, req_beans):
        """
        Check ingredients in machine to make coffee.
        Args:
            req_water (int): amount how mucjch water need
            req_milk (int): amount milk
            req_beans (int): amount beans

        Returns:
            bool: True if ingredient norm amount
        """
        if self.water_amount < req_water:
            print("Sorry, not water!")
            return False
        if self.milk_amount < req_milk:
            print("Sorry, not milk!")
            return False
        if self.beans_amount < req_beans:
            print("Sorry, not coffee beans!")
            return False
        if self.cups_count < 1:
            print("Sorry, not cups!")
            return False
        return True
#---------------------------------------------------------------------
    def brew_coffee(self, req_water, req_milk, req_beans, coffee_price):
        """
        Prepares the coffee ingredients and update resours.

        Args:
            req_water (int): amount water needed
            req_milk (int):  amount milk needed
            req_beans (int): amount coffee beans
            coffee_price (int):  coffee price
        """
        if self.check_ingredients(req_water, req_milk, req_beans):
            print("Coffee is ready! Enjoy!")
            self.water_amount -= req_water
            self.milk_amount -= req_milk
            self.beans_amount -= req_beans
            self.cups_count -= 1
            self.cash_in_machine += coffee_price
#------------------------------------------------------------------------
    def buy_coffee(self):
        """
        Ask user which type coffee he wants to buy and make it.
        """
        while True:
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

            if choice == "1":  # Espresso
                self.brew_coffee(250, 0, 16, 4)
                break
            elif choice == "2":  # Latte
                self.brew_coffee(350, 75, 20, 7)
                break
            elif choice == "3":  # Cappuccino
                self.brew_coffee(200, 100, 12, 6)
                break
            elif choice == "back":  # Go back to main menu
                break
            else:
                print("Invalid input. Please choose 1, 2, 3, or 'back'.")
#-----------------------------------------------------

    def refill_ingredients(self):
        """
        Ask user how much water, milk, beans, cups
        they want to add to the machine.
        """
        self.water_amount += int(input("How much water would you like to add (ml)? "))
        self.milk_amount += int(input("How much milk would you like to add (ml)? "))
        self.beans_amount += int(input("How many grams of coffee beans would you like to add? "))
        self.cups_count += int(input("How many disposable cups would you like to add? "))
#----------------------------------------------------
    def take_money(self):
        """
        Take all money from the coffee mach and print it.
        """
        print(f"I give you {self.cash_in_machine}")
        self.cash_in_machine = 0
#---------------------------------------------
    def process_action(self, action):
        """
        Processes the user's input and performs the requested action.

        Args:
            action (int): ("1 - buy", "2 - fill", "3 - take", "4 - remaining", "5- exit").

        Returns:
            bool: False if action is 'exit', otherwise True.
        """
        if action == "1":
            self.buy_coffee()
        elif action == "2":
            self.refill_ingredients()
        elif action == "3":
            self.take_money()
        elif action == "4":
            self.show_status()
        elif action == "5":
            return False
        else:
            print("Invalid action. Please try again.")
        return True


# Main menu
coffee_maker = MyCoffeeMaker()
running = True
while running:
     print("Menu: \n1 - Buy coffee \n2 - Refill ingredients \n3 - Take money \n4 - Show status \n5 - Exit")
     action = input("Enter action (buy, fill, take, remaining, exit): ")
     running = coffee_maker.process_action(action)
