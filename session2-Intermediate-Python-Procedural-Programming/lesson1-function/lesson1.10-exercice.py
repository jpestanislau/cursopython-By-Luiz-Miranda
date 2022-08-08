"""
Make a to-do list with the following options:
      add tasks
      list tasks
      undo option (each time we call it undoes the last action)
      redo option (each time we call it redoes the last action)
      ['Task 1', 'Task 2']
      ['Task 1'] <- Undo
      ['Task 1', 'Task 2'] <- Redo
      entry <- New task
"""


def add_to_list(lis, activity):
    lis.append(activity)


def undo_to_list(lis, undo_lis):
    if lis:
        undo_lis.append(lis.pop())
        print('Last activity removed!')
        return
    print('Nothing to undo')


def redo_to_list(lis, undo_lis):
    if undo_lis:
        lis.append(undo_lis.pop())
        print('Last activity re-added!')
        return
    print('Nothing to undo')


def show_list():
    print('')
    print(to_do_list)
    print('')


to_do_list = []
undo_list = []

while True:
    selected_option = input('What do you wanna do? [show, add, undo, redo]')
    if selected_option == 'show':
        show_list()
        continue
    elif selected_option == 'add':
        to_do = input('Please, type your activity')
        add_to_list(to_do_list, to_do)
        continue
    elif selected_option == 'undo':
        undo_to_list(to_do_list, undo_list)
        continue
    elif selected_option == 'redo':
        redo_to_list(to_do_list, undo_list)
        continue
    print('Invalid option')
