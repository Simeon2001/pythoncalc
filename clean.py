
def help_screen():
	print("Add: adds two intergers")
	print("Subtract: subtracts two intergers")
	print("Multiply: multiplies two intergers")
	print("print: shows the result of the latest operation")
	print("Help: shows this help_screen")
	print("Quit: quits/exits the program.")
	
	"""menu()
	display the menu
	accepts no parameters6
	returns the string to the users
	"""
	
def menu():
	#display a menu
	return input("==(A))dd  (S)ubtract  (M)ultiply  (P))rint   (H)elp  (Q)uits ==")
	
	""" main()
	run a command  loop that enables the user to perform a simple arithmetics
	"""

def main():

	result = 0.0
	done=False
	while not done:
		choice = menu() #get users choice
	
	
		if choice == "A":
			val1 = int(input("Enter an integer: "))
			val2 = int(input("Enter another integer"))
			result = val1 + val2
			print(result)
		elif choice == "S" :
			val1 = int(input("Enter an integer: "))
			val2 = int(input("Enter another integer"))
			result = val1 - val2
			print(result)
		elif choice == "P":
			print(result)
		elif choice == "H":
			print(help_screen)
		elif choice == "Q":
			done=True		       
	
main()