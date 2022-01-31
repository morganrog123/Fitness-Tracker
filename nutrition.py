def nutrition_screen():
	print("\n\nNUTRITION")
	print("-" * 9 + "\n")
	print("Menu Options:")
	print("1 - Meal Recording")
	print("2 - Meal History")
	print("3 - Back\n")
	nutrition_choose_option()

def nutrition_choose_option():
	option = input("Please choose an option by number or name: ").lower()
	nutrition_option_chosen(option)

def nutrition_option_chosen(option):
	option_chosen = False
	while option_chosen == False:
		if option == "1" or option == "meal recording":
			meal_recording()
			option_chosen = True
		elif option == "2" or option == "meal history":
			meal_history()
			option_chosen = True
		elif option == "3" or option == "back":
			option_chosen = True
		else:
			print("\nThe choice you have provided has not been recognised. Please try again.\n")
			nutrition_choose_option()