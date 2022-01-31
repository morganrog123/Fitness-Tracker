from weight import *
from exercise import *
from nutrition import *

option = ""
def home_screen():
	print("\n\nWelcome to the fitness tracker home screen.\n")	
	print("Menu Options:")
	print("1 - Weight")
	print("2 - Exercise")
	print("3 - Nutrition")
	print("4 - Exit\n")
	choose_option()

def choose_option():
	option = input("Please choose an option by number or name: ").lower()
	option_chosen(option)

def option_chosen(option):
	option_chosen = False
	while option_chosen == False:
		if option == "1" or option == "weight":
			weight_screen()
			home_screen()
			option_chosen = True
		elif option == "2" or option == "exercise":
			exercise_screen()
			home_screen()
			option_chosen = True
		elif option == "3" or option == "nutrition":
			nutrition_screen()
			home_screen()
			option_chosen = True
		elif option == "4" or option == "exit":
			print("\nThank you for using the fitness tracker. Goodbye!")
			option_chosen = True
		else:
			print("\nThe choice you have provided has not been recognised. Please try again.\n")
			choose_option()

home_screen()
