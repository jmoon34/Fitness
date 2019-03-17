import datetime
import json
from Food import Food



class Vault:
    def __init__(self, start_year=2018, start_month=10, start_day=9):
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day

        # calory_dict structure => {name_of_food: food}
        self.food_dict = {}
        self.food_dict_file_str = "FoodDict/FoodDict.json"

        # journal_dict structure => {date_string: [{calorie_dict}, sum_calories]}
        # calorie_dict structure => [{name_i: calorie_i}]
        self.food_journal_dict = {}
        self.food_journal_file_str = "FoodJournal/FoodJournal"

        self.menu_options = "Enter Key\n" \
                       "1. Add food to calorie_dict\n" \
                       "2. Add food to journal_dict\n" \
                       "-1. Exit"
        self.menu()



    # Method that controls the Vault object according to user input
    def menu(self):
        #Method calls for setup

        menu_flag = True
        while menu_flag:
            try:
                menu_key = int(input(self.menu_options))
            except ValueError:
                print("Invalid key")
            else:
                if menu_key == 1:
                    print("Add food to calorie_dict")
                    temp_food = Food.create_food()
                    self.add_food_dict_entry(temp_food)

                elif menu_key == 2:
                    print("Add food to journal_dict")
                    date_str = self.date_prompt()
                    food_name = str(input("Enter food name: "))
                    if food_name in self.food_dict:
                        print(food_name, "added to", date_str, "journal entry")
                        self.add_food_journal_dict_entry(date_str, self.food_dict[food_name])
                    else:
                        print(food_name, "not in food_dict. Must be created")
                        food_calorie = int(input("Enter calories: "))
                        food_unit = int(input("Enter unit: "))
                        food_amount = int(input("Enter amount: "))
                        temp_food = Food(food_name, food_calorie, food_unit, food_amount)
                        self.add_food_dict_entry(temp_food)
                        self.add_food_journal_dict_entry(date_str, temp_food)

                elif menu_key == -1:
                    menu_flag = False
                else:
                    print("Invalid key")

    def get_journal_dict_from_file(self, date_string):
        with open(self.food_journal_file_str + date_string, 'r') as fp:
            journal_dict = json.load(fp)
        return journal_dict

    def get_all_food_journal_dict_from_file(self):
        """
        Gets all the entries for journal_dict from starting date
        :return:
        """
        date_time = datetime.datetime(self.start_year, self.start_month, self.start_day)
        today = False
        while not today:
            date_string = self.date_to_string(date_time.year, date_time.month, date_time.day)
            try:
                temp_dict = self.get_journal_dict_from_file(date_string)
            except FileNotFoundError:
                print("No record for", date_string)
            else:
                self.food_journal_dict.update(temp_dict)

            if date_time.year == datetime.datetime.today().year and date_time.month == datetime.datetime.today().month \
                    and date_time.day == datetime.datetime.today().day:
                today = True

            date_time += datetime.timedelta(days=1)

    def add_food_journal_dict_entry(self, date_string, food):
        # Checks if entry for the date exists, and creates one if not
        if date_string not in self.food_journal_dict:
            self.food_journal_dict[date_string] = [{}, 0]

        food_dict = self.food_journal_dict[date_string][0]
        # Adds a Food object as a dictionary entry to food_dict
        food_dict[food.name] = (food.amount / food.unit) * food.calories
        # Update the sum_calories and writes dictionary to file
        self.food_journal_dict[date_string][1] += food_dict[food.name]
        self.write_food_journal_dict_to_file(date_string)

    def write_food_journal_dict_to_file(self, date_string):
        file_name = self.food_journal_file_str + date_string + ".json"
        with open(file_name, 'w') as fp:
            fp.write(json.dumps(self.food_journal_dict[date_string], indent=3))

    def add_food_dict_entry(self, food):
        self.food_dict[food.name] = food
        self.write_food_dict_to_file()

    def get_food_dict_from_file(self):
        with open(self.food_dict_file_str, 'r') as fp:
            temp_dict = json.load(fp)
            self.food_dict.update(temp_dict)

    def write_food_dict_to_file(self):
        with open(self.food_dict_file_str, 'w') as fp:
            fp.write(json.dumps(self.food_dict, indent=3))


    @staticmethod
    def date_to_string(year, month, day):
        day_str = str(day)
        month_str = str(month)
        if day < 10:
            day_str = "0" + day_str
        if month < 10:
            month_str = "0" + month_str
        return str(year) + "-" + month_str + "-" + day_str

    @staticmethod
    def date_prompt():
        year_flag = False
        month_flag = False
        day_flag = False
        while not year_flag:
            try:
                year = int(input("Enter year: "))
            except ValueError:
                print("Enter integer")
            else:
                year_flag = True
                while not month_flag:
                    try:
                        month = int(input("Enter month: "))
                    except ValueError:
                        print("Enter integer")
                    else:
                        month_flag = True
                        while not day_flag:
                            try:
                                day = int(input("Enter day: "))
                            except ValueError:
                                print("Enter integer")
                            else:
                                day_flag = True
                                print(Vault.date_to_string(year, month, day))
        return Vault.date_to_string(year, month, day)



