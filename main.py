def home_screen():
	print("\nWelcome to the fitness tracker.\n")

def menu_options():	
	print("Menu Options:")
	print("1 - Weight")
	print("2 - Exercise")
	print("3 - Nutrition")
	print("4 - Exit\n")

option = ""
def choose_option():
	global option
	option = input("Please choose an option by number or name: ").lower()
	return option

home_screen()
menu_options()
choose_option()

option_chosen = False
while option_chosen == False:
	if option == "1" or option == "weight":
		# This will display the Weight Tracking page.
		option_chosen = True
	elif option == "2" or option == "exercise":
		# This will display the Exercise Tracking page.
		option_chosen = True
	elif option == "3" or option == "nutrition":
		# This will display the Nutrition Tracking page
		option_chosen = True
	elif option == "4" or option == "exit":
		# This will exit the program.
		option_chosen = True
	else:
		print("\nThe choice you have provided has not been recognised. Please try again.\n")
		choose_option()