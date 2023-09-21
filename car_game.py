''' car game
    * make a command line game 
        >Enter a command 
        if we type help
        >help
        start- to start the car
        stop - to stop the car
        exit - to exit the game
        * for any other command
        >asf
        command is not found
        >start 
        car started... Ready to go
        >stop
        car stopped
        >exit
        exit    '''
# Name - Aditya Kumar
# ID - 22BTCSE067
# Programme - Btech CSE

print("Car Game: give command to start the engine\n")
started = False
while True:
    command = input(">").lower()
    if (command == "start"):
        if started:
            print("hey,Car has already started")
        else:
            started = True
            print("car started... Ready to go")
    elif (command == "stop"):
        if not started:
            print("Hey,Car has already stopped")
        else:
            started = False
            print("Car Stopped.")
    elif (command == "help"):
        print("""
start- to start the car
stop - to stop the car 
exit - to exit the game""")
    elif (command == "exit"):
        break
    else:
        print(f"E: {command} command is not found ..")
print("How was the experience!!")