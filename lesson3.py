your_input= input("\n\n please enter a number:\n1 : stone\n2 : paper\n3 : scissors\n\n") 
if your_input.isdigit() :
    print("it is digit")
    your_choice = int(your_input)
else :
    print("you must enter a valid number")
