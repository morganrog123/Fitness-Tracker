def weight_screen():
	print("\n\nWEIGHT")
	print("-" * 6 + "\n")
	print("Menu Options:")
	print("1 - Weight Recording")
	print("2 - Weight History")
	print("3 - Weight Forecasting")
	print("4 - Back\n")
	weight_choose_option()

def weight_choose_option():
	option = input("Please choose an option by number or name: ").lower()
	weight_option_chosen(option)

def weight_option_chosen(option):
	option_chosen = False
	while option_chosen == False:
		if option == "1" or option == "weight recording":
			weight_recording()
			option_chosen = True
		elif option == "2" or option == "weight history":
			weight_history()
			option_chosen = True
		elif option == "3" or option == "weight forecasting":
			weight_forecasting()
			option_chosen = True
		elif option == "4" or option == "back":
			option_chosen = True
		else:
			print("\nThe choice you have provided has not been recognised. Please try again.\n")
			weight_choose_option()