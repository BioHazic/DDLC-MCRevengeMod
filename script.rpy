# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.
#define config.developer = True

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:
        call intro_mod from _call_intro_mod

    if persistent.playthrough == 1:
        call intro_mod_2 from _call_intro_mod_2
    
    # There's a bit of problem / bugs that I can't fix
    # Saving and loading is pretty much broken in this game
    # I don't know...
    if persistent.playthrough == 2:
        # I guess there's no other way
        jump intro_mod_2_1
        #call intro_mod_2_1
        #next chapter
        #call chapter_mod_2 from _call_chapter_mod_2
        #jump mod_end_demo
        # I'll disable this temporarily

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
