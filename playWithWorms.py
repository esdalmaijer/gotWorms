"""play with some worms"""
from psychopy import core, visual, gui, data, event

#flag to avoid annoying UI things when developing
debug = True

""" Set up things to start with """
if debug != True:
    try:  # try to get a previous parameters file
        
        from psychopy import gui
        myDlg.addField('Session:')
            expInfo = {'id': ok_data[0], 'session': ok_data[1]}
        


    # make a text file to save data

    # Write header information to the csv

#instantiate our window 

"""Instructions"""
#Screen 1
exampleWorm = visual.ImageStim(win, image='stim/wormy_green.png',pos=[0, -4])
message3 = visual.TextStim(win, pos=[0, -5], text='Press the button to continue')
exampleWorm.draw()

#Screen 2 
message1 = visual.TextStim(win, pos=[0,+3],text='You will see two worms, like the ones below')
message2 = visual.TextStim(win, pos=[0,+2],text='The game is to remember the angle of the worms')
left_worm = visual.ImageStim(win, image='stim/wormy_green.png',pos=[0, 3])
right_worm = visual.ImageStim(win, image='stim/wormy_red.png',pos=[0, 2])
message1.draw()
message2.draw()
left_worm.draw()
right_worm.draw()
win.flip()#to show our newly drawn 'stimuli'
#pause until there's a keypress
event.waitKeys()