import easygui
import fidelity_class as fd

browser = easygui.fileopenbox()
s = browser.split("data")
file = s[1].strip('\\')
file = 'data/'+file
print(file)

def user_info():

    print("Please find below the options available:")
    print("1.- Would you like to Plot your Portfolio Current Value Today?")
    print("2.- Would you like to Plot your Portfolio Daily Gain/Loss today?")
    print("3.- Would you like to Plot your Portfolio Total Net Profit?")
    print("4.- Would you like to Display your Portfolio Top Performer (Text Output)")
    print("5.- Would you like to Display your Portfolio Worst Performer (Text Output)\n")

    while True:
        try:
            menu_option = int(input("Please enter a number as per the menu above:  "))
            if menu_option > 0 and menu_option < 6:
                    break
            if menu_option.isalpha():
                print("please enter a number")

        except:
            print("please enter a number")


    return menu_option

def selection(menu_option):

    class_list = [attribute for attribute in dir(fd.Positions(file)) if callable(getattr(fd.Positions(file),attribute)) and attribute.startswith('__') is False]
    option_dict = {}
    count = 0
    for classes in class_list:
        option_dict[count] = classes
        count += 1

    init_method = fd.Positions(file)
    methods = getattr(init_method, option_dict.get(menu_option))
    return methods()

if __name__ == "__main__":

    yesChoice = ['yes', 'y', 'Y']
    noChoice = ['no', 'n', 'N']
    a = user_info()
    selection(a)

    while True:
        cont = input("\n Enter yes/no to continue using the script: ")
        if cont in yesChoice:
            a = user_info()
            selection(a)
        elif cont in noChoice:
            break
        else:
            print("Invalid Input. \n Exiting!")
            break




