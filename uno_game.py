from unoFunction import *

play_again = True
while play_again:
    print_blue     ("\n          WELCOME TO THE UNO-GAME        \n")
    title_screen        = title_screen()
    title_screen_option = titleScreen_choice(title_screen)
    
    if title_screen == 'help':
        instruction = help_option()
        title_screen_option = titleScreen_choice(instruction)
