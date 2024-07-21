class Program:

    @staticmethod
    def output_square():
        user_num = int(input("Enter an integer: "))
        user_num_squared = user_num * user_num
        print(user_num_squared)

    @staticmethod
    def output_doubled():
        print('Enter x: ')
        x = int(input())
        print('x doubled is:', (2 * x))

    @staticmethod
    def output_no_parking_sign():
        print("  NO PARKING")
        print("2:00 - 6:00 a.m.")

    @staticmethod
    def welcome_message():
        first_name = input("Enter your first name: ")
        welcome_message = f"Hello {first_name} and welcome to CS Online!"
        print(welcome_message)

    @staticmethod
    def short_story():
        first_name = input("Enter a first name: ")
        generic_location = input("Enter a location: ")
        whole_number = input("Enter a number: ")
        plural_noun = input("Enter a plural noun: ")
        print(first_name, 'went to', generic_location, 'to buy', whole_number, 'different types of', plural_noun)

    @staticmethod
    def output_square_and_cube():
        print("Enter integer:")
        user_num = int(input())
        print("You entered:", user_num)
        user_num_squared = user_num * user_num
        user_num_cubed = user_num * user_num * user_num
        print(user_num, "squared is", user_num_squared)
        print("And", user_num, "cubed is", user_num_cubed, "!!")
        print("Enter another integer:")
        user_num2 = int(input())
        sum_result = user_num + user_num2
        product_result = user_num * user_num2
        print(user_num, "+", user_num2, "is", sum_result)
        print(user_num, "*", user_num2, "is", product_result)

    @staticmethod
    def output_tree_and_cat():
        print("   *")
        print("  ***")
        print(" *****")
        print("*******")
        print("  ***")
        print()
        print()
        print("/\\   /\\")
        print("  o o")
        print(" =   =")
        print("  ---")

def main():
    Program.output_square()
    Program.output_doubled()
    Program.output_no_parking_sign()
    Program.welcome_message()
    Program.short_story()
    Program.output_square_and_cube()
    Program.output_tree_and_cat()

main()
