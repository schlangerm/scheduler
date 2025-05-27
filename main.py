from gui.gui import Intro_Window

def onStartup():
    print("Welcome to Scheduler")
    # startup stuff
    intro_window = Intro_Window()
    intro_window.mainloop()

def getUserInputs():
    teamSizeInput = input("Number of team members: ")
    validateUserInput(teamSizeInput)
    subGroupInput = input("Number of sub-groups: ")
    validateUserInput(subGroupInput)


def validateUserInput(userInput, expectedDataType):
    try:
        result = expectedDataType(userInput)
    except:
        print("Input not accepted. Try again.")

if __name__ == '__main__':
    onStartup()

