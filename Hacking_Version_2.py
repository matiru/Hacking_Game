# Hacking version 2
# This is a text-based password guessing game that displays
# a list of potential computer password.The player is allowed 1 attempt
# The game indicates that the player failed to guess the password correctly.

from uagame import Window
from time import sleep


#create window
# Window (title,width,height)
window  = Window ('Hacking',600,500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')


# window type has a method call draw_string that displays string in a window
# draw_string(st  ring,x,y)
   #- display string and 2 integers that indicate the top left corner of 
   #its location in the window
   #a point 10 pixels down from the top of the windoe is denoted 0,10
 
# display header
line_y = 0 
string_height = window.get_font_height()
window.draw_string('DEBUG MODE',0, 0)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('1 ATTEMPT(S) LEFT',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

 
window.draw_string('',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

# display password list

window.draw_string('PROVIDE',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('SETTING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('CANTINA',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('CUTTING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('HUNTERS',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('SURVIVE',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('HEARING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('HUNTING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('REALIZE',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('NOTHING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('OVERLAP',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('FINDING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('PUTTING',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('',0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

# prompt for guess
guess = window.input_string('ENTER PASSWORD >', 0 , line_y)

# end game
# clear window
window.clear()
#     display failure outcome
#         display guess
             #compute x coordinate
x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2

             #compute y coordinate
outcome_height = 7 * string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2 

window.draw_string(guess,line_x,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#         display blank line

window.draw_string('',0, line_y)
window.update()
#sleep(1.0)
#line_y = line_y + string_height

#         display failure line 2

fail2 = 'LOGIN FAILURE - TERMINAL LOCKED'
x_space = window.get_width() - window.get_string_width(fail2)
line_x = x_space // 2

             #compute y coordinate
outcome_height = 5 * string_height
y_space = window.get_height() - outcome_height
line_y = line_y + string_height

window.draw_string(fail2,line_x,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height








#         display blank line
window.draw_string('',0, line_y)
window.update()
#sleep(1.0)
#line_y = line_y + string_height

#         display failure line 3


fail3 = 'PLEASE CONTACT AN ADMINISTRATOR'
x_space = window.get_width() - window.get_string_width(fail3)
line_x = x_space // 2

             #compute y coordinate
outcome_height = 3 * string_height
y_space = window.get_height() - outcome_height
line_y = line_y + string_height

window.draw_string(fail3,line_x,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height


#         display blank line
window.draw_string('',0, line_y)
window.update()

#    prompt for end

end = 'PRESS ENTER TO EXIT '
x_space = window.get_width() - window.get_string_width(end)
line_x = x_space // 2

             #compute y coordinate
outcome_height = 1 * string_height
y_space = window.get_height() - outcome_height
line_y = line_y + string_height

window.draw_string(end,line_x,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height


PROMPT_END = window.input_string('', 0 , line_y)




#      close window
window.close()


