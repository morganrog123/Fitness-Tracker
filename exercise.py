def exercise_screen():
	print("\n\nEXERCISE")
	print("-" * 8 + "\n")
	print("Menu Options:")
	print("1 - Workout Recording")
	print("2 - Workout History")
	print("3 - Personal Bests")
	print("4 - Back\n")
	exercise_choose_option()

def exercise_choose_option():
	option = input("Please choose an option by number or name: ").lower()
	exercise_option_chosen(option)

def exercise_option_chosen(option):
	option_chosen = False
	while option_chosen == False:
		if option == "1" or option == "workout recording":
			workout_recording()
			option_chosen = True
		elif option == "2" or option == "workout history":
			workout_history()
			option_chosen = True
		elif option == "3" or option == "personal bests":
			personal_bests()
			option_chosen = True
		elif option == "4" or option == "back":
			option_chosen = True
		else:
			print("\nThe choice you have provided has not been recognised. Please try again.\n")
			exercise_choose_option()