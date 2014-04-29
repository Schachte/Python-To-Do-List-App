import todo_data
class_info = []

def menu():
    menu_list = '''
    ******************************
           Schachte To-Do
    ******************************

    A: Add Item
    B: View List
    C: Exit
    '''
    print menu_list
    choice = raw_input(">>")
    return choice

def add_item():
    print 'Enter Class, Homework, Due Date and Completion Time'
    information = raw_input(">>")
    information = information.split("/")
    homework_add = todo_data.AddInfo(information[0], information[1], information[2], information[3])
    class_info.append(homework_add)
    print 'Information Added'


def view_details():
    complete_list = ''
    for each_todo in class_info:
        info = '''
        Class: %s
        Homework: %s
        Due Date: %s
        Completion: %s
        \n''' %(each_todo.course, each_todo.hw, each_todo.duedate, each_todo.dedication,)
        complete_list = complete_list + info
        print info
    return complete_list

next_choice = menu()

while (next_choice != "C"):

    if next_choice == "A":
        add_item()
        next_choice = menu()

    elif (next_choice == "B"):
        list_info = view_details()
        next_choice = menu()

    elif (next_choice == "C"):
        break

new_file = open("To-Do.txt", "w")
print 'File Opened'
new_file.write(list_info)
print 'To-Do Data Written'
new_file.close()
print 'File Closed'