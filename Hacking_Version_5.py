# Hacking version 5
# This is a text-based password guessing game that displays
# a list of potential computer password.The player is allowed 4 attempts
#it displays a warning on 1 trial left
# The game indicates that the player failed to guess the password correctly.
# Simplifying the code by 
 #1) Removing duplicate code by using repetition control strucutes i.e loops
 #2) Removing duplicate data by binding repeated objects to a single identifier.
 

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
   #a point 1g_line_x pixels down from the top of the windoe is denoted 0,10
 
# display header
line_y = 0
string_height = window.get_font_height()
pause_time = 0.3
g_line_x = 0
attempts_left = 4
header = ['DEBUG MODE',str(attempts_left)+' ATTEMPT(S) LEFT', '']

for header_line in header:
    # display header line
    window.draw_string(header_line,g_line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height   


# display password list

password_list = ['PROVIDE','SETTING','CANTINA','CUTTING','HUNTERS','SURVIVE','HEARING','HUNTING','REALIZE','NOTHING','OVERLAP','FINDING','PUTTING','']

for password in password_list:
    #display passwords
    window.draw_string(password,g_line_x, line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height    

#   choose password

password = password_list[7]

# prompt for guess
guess = window.input_string('ENTER PASSWORD >', g_line_x , line_y)
line_y = line_y + string_height 

#      decrement attemps left

attempts_left =  attempts_left - 1

#      while guess not equal password and attempts left > 0
while  attempts_left > 0 and guess != password : 
    
    #         display attempts left    
    window.draw_string(str(attempts_left), g_line_x, string_height)
     
    #         check warning 

    #                 if attempts left equal 1 
            #            display warning    
    if attempts_left == 1:
        a=window.get_width()-window.get_string_width('*** LOCKOUT WARNING ***')
        b=window.get_height() - window.get_font_height()
        window.draw_string('*** LOCKOUT WARNING ***',a,b)
        window.update()  
    
     #             prompt for guess   
        
    guess = window.input_string('ENTER PASSWORD >', g_line_x , line_y)
    line_y = line_y + string_height    
         #             decrement attempts left 
      
    attempts_left =  attempts_left - 1    
        
        
        
        
          
          
          

# end game
# clear window
window.clear()

#     create outcome
if guess == password:
   # create success
    outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
    prompt = 'PRESS ENTER TO CONTINUE'
    end = 'PRESS ENTER TO CONTINUE '
   
   #         create failure   
else:
   # create failure
    outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '','PLEASE CONTACT AN ADMINISTRATOR', '']
    prompt = 'PRESS ENTER TO EXIT'
    end = 'PRESS ENTER TO EXIT '
      

#     display  outcome


             #compute y coordinate
#string_height = window.get_font_height()
outcome_height = (len(outcome) + 1)*string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2 


for outcome_line in outcome:
    # display centered outcome line
      #    compute x coordinate    
    x_space = window.get_width() - window.get_string_width(outcome_line)
    line_x = x_space // 2  
    
    window.draw_string(outcome_line,line_x,line_y)
    window.update()
    sleep(pause_time)
    line_y = line_y + string_height


#    prompt for end
#         compute x coordinate
x_space = window.get_width() - window.get_string_width(end)
line_x = x_space // 2

window.input_string(end,line_x,line_y)


#      close window
window.close()


