label day2_start: 

    play music "audio/music/server_room_chiller_versionlooped.ogg" loop fadein 2.0 fadeout 2.0 

    $ player_choice(
        [
            ("hi again", "day2_1"), 
            ("im back. boo me again", "day2_2"), 
            ("goooooooooooooooooooooooooooood mornin!", "day2_3")
        ]
    )


label day2_1: 

    $ chat_message("wnpep: the not fed returns")

    #MC: what a title. can i earn a cooler one?
    $ player_choice(
        [
            ("what a title. can i earn a cooler one?", "x")
        ]
    )

    $ chat_message("wnpep: well this isnt the nineties so. no")

    $ chat_message("elimf: speak for yourself i've got a hugeass Hackerman banner")

    $ chat_message("elimf: for motivation and courage", ot="wnpep")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: thats not")

    $ chat_message("wnpep: you know what im just going to let this pass")

    $ chat_message("elimf: so unlike u", ot="wnpep")

    $ chat_message("wnpep: i refuse to let you force my hand")

    $ chat_message("wnpep: explaining things will just make me feel old again",ot="elimf")

    $ chat_message("elimf: your loss")

    $ chat_message("elimf: i couldve learned something")

    pause 1 

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("wnpep: i mean. do you want to learn something? ")
    
    jump day2_4


label day2_2: 
    $ points_seekLove += 1

    $ chat_message("incri: dont tell me what to do ")

    $ chat_message("wnpep: {image=e_letsgo}")

    $ chat_message("incri: maybe ill eb nice just becuause then")

    #MC: well i'm not going to stop you
    $ player_choice(
        [
            ("well i'm not going to stop you", "x")
        ]
    )

    $ chat_message("wnpep: can we see some of that?")

    $ chat_message("incri: kindly fuck off")

    $ chat_message("wnpep: yea alright",ot="elimf")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: shocking",fastmode=True)
    
    jump day2_4


label day2_3:
    $ points_seekLove += 1

    $ chat_message("elimf: thaaaaaaaaaaaaaaaaaaaaaaaaaaaaank youuuuuuuuuuuuuuuu")

    #MC: yyyouuuureeeeeeee weeeellcoommmmeeeeeeeeeeee
    $ player_choice(
        [
            ("yyyouuuureeeeeeee weeeellcoommmmeeeeeeeeeeee", "x")
        ]
    )

    $ chat_message("elimf: ur like. a ripple in my puddle. ur good")

    $ chat_message("wnpep: my opinion might be worsening actually.")

    $ chat_message("elimf: embrace the newfound presence of someone useless but entertaining")

    #MC: now hold on
    $ player_choice(
        [
            ("now hold on", "x")
        ]
    )

    jump day2_4
 

label day2_4: 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: shut up shut up shutup")

    $ chat_message("elimf: careful we'll distract incri and ruin their \"art\" ", ot="incri")

    $ chat_message("incri: shut upppp")

    $ chat_message("incri: ur such a fking loser. bitch. idiot", ot="elimf")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: dumb also")

    # incri typing

    $ chat_message("wnpep: lets redirect the conversation a little",ot="incri")

    $ chat_message("wnpep: incri, hows progress? ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: up yuours")

    pause 1

    $ chat_message("wnpep: alright ")

    $ chat_message("elimf: u keep letting this happen")

    $ chat_message("wnpep: i know i am, and yet i keep stepping on that rake", ot="incri")

    $ chat_message("incri: not that u care but im almost done")

    $ chat_message("incri: low lvl gov sht is easyyyy")

    #MC: is that what ur looking at? 
    $ player_choice(
        [
            ("is that what ur looking at? ", "x")
        ]
    )

    $ chat_message("incri: wat do u care. fed. narc")

    $ chat_message("elimf: does ur head explode when cashiers ask if u found everything okay")

    $ chat_message("wnpep: i would hope not, theyre just trying to do their jobs")

    #MC: sorry, i was just curious about your process w the program
    $ player_choice(
        [
            ("sorry, i was just curious about your process w the program", "x")
        ]
    )

    $ chat_message("elimf: not the sincerity. bold maneuver",ot="incri")

    $ chat_message("incri: sucking up wont work")

    $ chat_message("incri: my techniques r beyond u")

    pause 2

    $ chat_message("incri: acutlaly")

    $ chat_message("incri: i  just thought of smth")

    $ chat_message("elimf: oh boy", ot="incri")

    $ chat_message("incri: i will teach u onet hing ONLY")

    $ chat_message("incri: its so easy even u should get it")

    #MC: …thanks
    $ player_choice(
        [
            ("...thanks", "x")
        ]
    )

    $ chat_message("incri: databse searching n stuff")

    $ chat_message("incri: u find the stuff and tell me and i'll do the advanced shit")

    $ chat_message("wnpep: now that sounds a little")

    $ chat_message("elimf: incri uncovers a 1000 iq chess move: making someone else do the work",ot="wnpep")

    $ chat_message("wnpep: took the words out of my mouth")

    $ chat_message("wnpep: couldnt resist the siren call of unpaid labor")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: jealous fcking blowhards thats not it")

    $ chat_message("incri: its educational")

    $ chat_message("incri: im being so HELPFUL",ot="elimf, wnpep")

    $ chat_message("elimf: uh huh absolutely", ot="wnpep")

    $ chat_message("elimf: {image=e_orz}", ot="wnpep")

    $ chat_message("wnpep: we would never doubt you")

    #MC: I would be very grateful
    $ player_choice(
        [
            ("I would be very grateful", "x")
        ]
    )

    $ chat_message("incri: never ask me for anyhhing again", ot="elimf")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: my god theyre still going for it")

    $ chat_message("wnpep: we have to give credit for the sheer lack of shame")

    #MC: er, you didn't have to do all this
    $ player_choice(
        [
            ("er, you didn't have to do all this", "x")
        ]
    )

    $ chat_message("incri: no now i  have to")

    $ chat_message("incri: lets show thse fucking clowns")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: get in the program")

    #### SEEKL SEGMENT BEGINS 

    #MC: i'm in. like since i logged in
    $ player_choice(
        [
            ("i'm in. like since i logged in", "day2_5"), 
            ("you get in the program", "day2_6")
        ]
    )

label day2_5: 
    $ chat_message("incri: shut up and listen ")
    jump day2_7


label day2_6: 
    $ points_seekLove += 1
    $ chat_message("incri: ur sooooo funny hahahahaha")
    jump day2_7

label day2_7:

    $ chat_message("incri: i already have his badge numbr ")

    $ chat_message("incri: go pull up the table: #azgov.police_info#")
    pause 0.5
    $ tables_seen.append("azgov.police_info")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.police_info"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_9"

    $ chat_message("elimf: ur in arizona????")

    $ chat_message("incri: no i'm not ufcker ")

    $ chat_message("incri: i just passed through ",ot="wnpep")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: i'm uncomfortable knowing this much about incri ",ot="elimf")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: arizona... ",ot="incri")

    $ chat_message("incri: fuck ",fastmode=True)

    $ chat_message("incri: {color="+color_help+"}pull it up thrim{/color}",ot="wnpep")

    $ chat_message("wnpep: remember ")

    $ chat_message("wnpep: `select * \nfrom azgov.police_info`")

    $ chat_message("wnpep: or {color="+color_help+"}click the table in your table list{/color} and hit execute")

    $ chat_message("wnpep: {image=e_wink}")

    jump wait_start

# label day2_8:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False
#     $ waiting_label = "day2_9"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_9 
#     $ renpy.pause(hard=True)

label day2_9:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 
    #MC: I see the table now. 
    $ player_choice(
        [
            ("I see the table now. ", "x")
        ]
    )

    $ chat_message("incri: ok do u see ths badge number ")

    $ chat_message("incri: {color="+color_help+"}55242{/color} ")
    pause 0.2
    $ hack_notes.append("badge: \n55242")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ player_choice(
        [
            ("yes, i see it ", "day2_10"), 
            ("no?", "day2_11")
        ]
    )

    #[1] MC: yes, i see it 
label day2_10: 
    $ points_seekLove += 1

    $ chat_message("incri: ez ")
    jump day2_12


    #[2] MC: no? 
label day2_11: 

    $ chat_message("incri: under the {color="+color_help+"}badge_no column{/color} idiot ")

    #$ chat_message("incri: {image=e_pain}")

    #MC: ok. yes. i see it. 
    $ player_choice(
        [
            ("ok. yes. i see it.", "x")
        ]
    )

    $ chat_message("incri: ya idiot ")
    jump day2_12


label day2_12: 
    $ chat_message("incri: name pls ")

    #MC: Bruce Johnson 
    $ player_choice(
        [
            ("says \"Bruce Johnson\"", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("name: \n'Bruce Johnson'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("wnpep: did the cop look like a bruce? ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: looked like a bicth ")

    $ chat_message("incri: ok can u look at this table now ")

    $ chat_message("incri: #azgov.marriage#")
    pause 0.5
    $ tables_seen.append("azgov.marriage")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.marriage"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_17"

    #MC: why? 
    $ player_choice(
        [
            ("why a marriage table??", "x")
        ]
    )

    $ chat_message("incri: ????") 

    $ chat_message("incri: who cares??????",ot="elimf, wnpep")

    $ chat_message("elimf: why are you chasing a cop incri ",ot="wnpep")

    $ chat_message("incri: bc he fucked p ",ot="wnpep")

    $ chat_message("wnpep: did you get a parking ticket? ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: i wa sbarely out of time on my spot") 

    $ chat_message("incri: stupid dumbfuck ass gulping time dictator ")

    $ chat_message("elimf: how late were u ")

    $ chat_message("incri: like 1 min ")

    $ chat_message("elimf: o ",ot="wnpep")

    $ chat_message("wnpep: only 1 min late? ")

    $ chat_message("incri: YES ")

    $ chat_message("wnpep: ok. i understand ",ot="incri")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: I AM GOING TO FKCIN G GUT HIS WALLET ")

    $ chat_message("wnpep: you go superstar! ",ot="elimf")

    $ chat_message("elimf: that's what this is all about", ot="wnpep") 

    $ chat_message("wnpep: let's massacre this savings account! ")

    $ chat_message("wnpep: {image=e_sparkle}")

    $ player_choice(
        [
            ("all over a parking ticket? what??", "day2_13"), 
            ("yay!", "day2_14")
        ]
    )


    # [1] MC: all over a parking ticket? what?? 
label day2_13:
    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: U DON'T NEED TO BE HERE") 

    $ chat_message("incri: U CAN LEAVE")

    #MC: I'M NOT LEAVING I WAS JUST ASKING A QUESTION 
    $ player_choice(
        [
            ("I'M NOT LEAVING I WAS JUST ASKING A QUESTION", "x")
        ]
    )

    $ chat_message("incri: STOP DOING THAT ")
    jump day2_15

    #[2] MC: yay! 
label day2_14:
    $ points_seekLove += 1

    $ chat_message("incri: DESTROY ")
    jump day2_15


   
label day2_15:

    # MC: but, how are we getting to his savings account through marriage records? 
    $ player_choice(
        [
            ("but, how are we getting to his savings account through marriage records? ", "x")
        ]
    )

    $ chat_message("elimf: every1 has secrets ")

    $ chat_message("elimf: and some ppl have spouises ")

    $ chat_message("elimf: who dont know all secrets ",ot="incri, wnpep")

    $ chat_message("incri: ^ that ",ot="wnpep")

    $ chat_message("wnpep: i tell my wife everything. this extortion stuff would never work on me ")

    pause 1

    $ chat_message("elimf: UR MARRIED?? ")

    $ chat_message("wnpep: what ")

    pause 1

    $ chat_message("wnpep: oh ")

    $ chat_message("wnpep: {image=e_serious}")

    pause 2 

    $ chat_message("wnpep: autocorrect haha ")

    $ chat_message("wnpep: wife = friend ",ot="elimf")

    $ chat_message("elimf: how does that autocorrect to th at") 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: i can't take this information stop speaking immediately ",ot="wnpep")

    $ chat_message("wnpep: i'm not married ")

    $ chat_message("elimf: ok now stop speaking ",ot="incri")

    $ chat_message("incri: OKAY ")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF SAYS HORN IT UP")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI SAYS HORN IT UP")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: {color="+color_help+"}GO LOOK AT THE TABLE{/color}")

    $ chat_message("incri: #AZGOV.MARRIAGE#")

    jump wait_start


# label day2_16:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False
#     $ waiting_label = "day2_17"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_17 
#     $ renpy.pause(hard=True)

label day2_17:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    #MC: i see it 
    $ player_choice(
        [
            ("i see it", "x")
        ]
    )

    $ chat_message("incri: see bruce? ")

    #MC: no... i don't think so 
    $ player_choice(
        [
            ("no... i don't think so", "x")
        ]
    )

    $ chat_message("incri: then add a where clause dumb ass ")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["spouse_name"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.marriage"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("mid", "M2635187")] 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_22"

    $ chat_message("wnpep: we didn't show thrim where clauses yet ")

    $ chat_message("elimf: UR MARRIED ")

    $ chat_message("wnpep: i'm not married ")

    $ chat_message("elimf: {image=e_baby}")

    #MC: i heard wnpep was married 
    $ player_choice(
        [
            ("i heard wnpep is married", "x")
        ]
    )

    $ chat_message("elimf: I ALSO HEARD WNPEP IS MARRIED", ot="wnpep")

    $ chat_message("wnpep: ok thrim, {color="+color_syntax+"}WHERE{/color} is something you would put after the from statement.")

    $ chat_message("wnpep: it's like {color="+color_help+"}a filter you use when you only care about certain records{/color}")

    $ chat_message("wnpep: like, if we were looking at table.example again and i wanted to see my information")

    $ chat_message("wnpep: i would add this to the end of my code: {color="+color_syntax+"}where hacker_name = 'wnpep'{/color}")

    #$ chat_message("wnpep: does that make sense? ")

    $ chat_message("wnpep: the whole statement would become \n`select * \nfrom table.example \nwhere hacker_name = 'wnpep'`")

    $ chat_message("elimf: except {color="+color_help+"}u dont have to use quotes when ur looking at numbers{/color}")

    $ chat_message("elimf: like if i wanted to see who had more than 30 hacks i could write ")

    $ chat_message("elimf: `select hacker_name \nfrom table.example\nwhere number_of_hacks > 30`")

    $ chat_message("elimf: make sense?")

    $ chat_message("elimf: {image=e_orz}")

    $ player_choice(
        [
            ("i get it. i know what to do", "day2_18"), 
            (".................", "day2_19")
        ]
    )

    #[1] MC: i get it. i know what to do 
label day2_18:
    $ points_seekLove += 1

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: great! ")

    jump day2_20

    #[2] MC: ................. 
label day2_19:

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: this is like so bsi c are u fucking kidding me ")

    #MC: dick
    $ player_choice(
        [
            ("dick", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: yes. well. here. might as well help ")

    $ chat_message("wnpep: `select * \nfrom azgov.marriage \nwhere full_name = 'bruce johnson'`")

    jump day2_20 

label day2_20: 
    $ chat_message("incri: let me know when ur fuckin g done {color="+color_help+"}finding dumbass cop in the marriage tbl{/color}")

    jump wait_start


# label day2_21:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_22"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_22 
#     $ renpy.pause(hard=True)

label day2_22:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    $ chat_message("incri: found him?" )

    #MC: yes -- his spouse is named "laura crane" 
    $ player_choice(
        [
            ("yes -- his spouse is named \"laura crane\"", "day2_23"), 
            ("yes -- his spouse is named \"hugh g. rection\"", "day2_24")
        ]
    )

label day2_23: 
    pause 0.2
    $ hack_notes.append("wife: \n'Laura Crane'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("wnpep: could be a maiden name and not her legal name now" )

    jump day2_25 


label day2_24: 
    $ points_seekLove += 1

    $ chat_message("wnpep: middle initial? ", ot="incri")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF SAYS HORN IT UP")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: v hnvhnv nnv  nv jmj ")

    $ chat_message("incri: j  hnvg gb nbm", ot="wnpep")

    pause 0.5

    $ chat_message("SYSTEM: INCRI offline") 
    $ incri_online = False

    pause 1.0

    $ chat_message("SYSTEM: INCRI online") 
    $ incri_online = True 

    $ chat_message("incri: nv n v nbvb v nm  uj,",ot="elimf")

    $ chat_message("elimf: the keyboard fisting has begun ")

    $ chat_message("wnpep: watch your language ")

    pause 1

    $ chat_message("incri: :) ")

    $ chat_message("incri: thrim ")

    $ player_choice(
        [
            ("how many keyboards do you break daily", "x")
        ]
    )

    $ chat_message("wnpep: the spouse is 'Laura Crane' inc ", ot="incri")
    pause 0.2
    $ hack_notes.append("wife: \n'Laura Crane'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("incri: :) ")

    jump day2_25 

label day2_25: 
    # odxny logs on 
    pause 0.5
    $ chat_message("SYSTEM: ODXNY online") 

    $ chat_message("odxny: Hello, everyone.")

    $ chat_message("elimf: incri is from arizona and wnpep is married ")

    $ chat_message("odxny: What? ",ot="wnpep, incri")

    $ chat_message("incri: {image=e_letsgo}", ot="wnpep",fastmode=True)

    $ chat_message("incri: I'M NOT ", ot="wnpep")

    $ chat_message("wnpep: it was a misunderstanding ", ot="odxny")

    $ chat_message("odxny: What happened to the secrecy? ")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: i don't knw i'm in misery ")

    $ chat_message("odxny: What's the current hack? ")

    $ chat_message("incri: I\"M TRYING TO EXTORT A COP BUT U ALL KEEP INTERRUPTING ME ")

    $ chat_message("odxny: {image=e_serious}")

    $ chat_message("odxny: Apologies. That does sound important.", ot="incri")

    $ chat_message("incri: THRIM ")

    $ chat_message("incri: WE NEED EMAILS") 

    #MC: WHERE DO I GET EMAILS 
    $ player_choice(
        [
            ("WHERE DO I GET EMAILS", "x")
        ]
    )

    $ chat_message("incri: #irs.contacts#")
    pause 0.5
    $ tables_seen.append("irs.contacts")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I80397-693")] 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_27"

    $ chat_message("elimf: yo when did we get irs data wait",ot="wnpep")

    $ chat_message("wnpep: that's kinda crazy", ot="odxny") 

    $ chat_message("odxny: A week ago.") 

    $ chat_message("elimf: wild") 

    $ chat_message("elimf: wnpep this is gonna be good for ur last hack right?")

    $ chat_message("wnpep: lol",ot="incri") 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: GO FIND BRUCE\"S EMAIL THRIM") 

    $ chat_message("elimf: {color="+color_help+"}WITH A DELICIOUS USE OF THE WHERE CLAUSE{/color}") 

    jump wait_start

    # wait for code to run 
# label day2_26:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_27"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_27 
#     $ renpy.pause(hard=True)

label day2_27:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    $ chat_message("incri: I\"M WAITING") 

    #MC: ok i got it 
    $ player_choice(
        [
            ("ok i got it", "x")
        ]
    )

    #MC: brucemjohn11@copmail.com
    $ player_choice(
        [
            ("bruce.johnson@copmail.com", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("email: \n'bruce.johnson\n@copmail.com'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5 

    $ chat_message("incri: OK NOW LAURA\"S EMAIL")   
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I20210-713"), ("irs_id", "I24270-766")] 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_29"

    $ chat_message("odxny: Reading up. What about the maiden name thing?")  

    $ chat_message("odxny: Her last name could be Crane or Johnson imo.")  

    $ chat_message("incri: SEARCH FOR BOTH NAMES THEN????", ot="wnpep")  

    $ chat_message("wnpep: crane + johnson")  

    #MC: at the same time? 
    $ player_choice(
        [
            ("at the same time?", "x")
        ]
    )

    $ chat_message("wnpep: {color="+color_help+"}you can use an OR{/color}")  

    $ chat_message("wnpep: {color="+color_syntax+"}where full_name = 'laura johnson' \nor full_name = 'laura crane'{/color}") 

    $ chat_message("wnpep: {image=e_wink}")

    #MC: ok ok ok 
    $ player_choice(
        [
            ("ok ok ok", "x")
        ]
    )

    jump wait_start

    # // wait for code to run and see both results 
# label day2_28:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_29"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_29 
#     $ renpy.pause(hard=True)

label day2_29:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    $ chat_message("odxny: So, which looks like the best match? ") 

    $ chat_message("wnpep: i'm looking too ") 

    #MC: i think it's.... 
    $ player_choice(
        [
            ("i think it's...", "x")
        ]
    )

    $ player_choice(
        [
            ("lauracrane78@wahoo.com", "day2_30"), 
            ("laura.crane.johnson@eeemail.com", "day2_32"), 
            ("crazee_js_girl@eeemail.com", "day2_31")
        ]
    )

    #[1] MC: [ two wrong answer options ] 
label day2_30: 

    jump day2_31 

label day2_31: 

    $ chat_message("wnpep: disagree. laura.crane.johnson is way more likely ")
    pause 0.2 
    $ hack_notes.append("email wife: \n'laura.crane.\njohnson\n@eeemail.com'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("wnpep: matches bruce's last name + her maiden name ") 

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: ok. thrim pull urself 2gethr ") 

    #MC: you can fucking do this yourself 
    $ player_choice(
        [
            ("you can fucking do this yourself", "x")
        ]
    )

    $ chat_message("incri: pass the ip wnpep ") 

    $ chat_message("elimf: OOHHHHHHHH")

    #MC: I'm sorry. I'm sorry. I'm sorry. 
    $ player_choice(
        [
            ("I'm sorry. I'm sorry. I'm sorry.", "x")
        ]
    )

    $ chat_message("incri: fuckking speak to me like that again ") 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: see what happens ") 

    $ chat_message("odxny: Calm down. ") 

    $ chat_message("incri: i'm calm") 

    $ chat_message("odxny: Sure. ") 

    jump day2_33 

    #[2] MC: laura.crane.johnson@eeemail.com 
label day2_32:     
    $ points_seekLove += 1

    $ chat_message("wnpep: agreed. all the others don't seem as likely ") 
    pause 0.2
    $ hack_notes.append("email wife: \n'laura.crane.\njohnson\n@eeemail.com'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("elimf: i think ur all underselling crazy js girl ")

    $ chat_message("elimf: j johnson ")

    $ chat_message("elimf: jsayin ",ot="wnpep")

    $ chat_message("wnpep: lol ", ot="odxny")

    $ chat_message("odxny: Too many possibilities for j. Just come back if the other email doesn't work out I guess ")

    $ chat_message("wnpep: or send the same info to both ")

    $ chat_message("odxny: True. Lmao ",ot="incri")

    $ chat_message("incri: ok. now.") 

    jump day2_33 

   
    # end choices  
label day2_33: 
    $ chat_message("incri: {image=e_orz}")

    $ chat_message("incri: i tuck that email away as a just in case") 

    $ chat_message("incri: now we have 1 more step ")

    #MC: which is...? 
    $ player_choice(
        [
            ("which is...?", "x")
        ]
    )

    $ chat_message("odxny: To find something to use as blackmail.") 

    $ chat_message("odxny: It's trivial once you have their email. ")

    $ chat_message("incri: {image=e_baby}")

    $ chat_message("incri: ugh i hate this part. searching. lame ")

    $ chat_message("wnpep: well, what sort of secrets would you keep from your spouse? ")

    $ chat_message("elimf: why don't you tell us wn ")

    $ chat_message("elimf: expert marriage person ")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: married ",ot="wnpep")

    $ chat_message("wnpep: not married ")

    $ player_choice(
        [
            ("infidelity?", "day2_34"), 
            ("money problems?", "day2_35"),
            ("not sure. could be anything", "day2_36")
        ]
    )

    #[1] MC: infidelity? 
label day2_34: 
    $ points_seekLove += 1

    $ chat_message("incri: wait. genius. YES ")

    $ chat_message("incri: HE LOOKED LIK EA CUCK")

    $ chat_message("odxny: Like his wife was cheating on him? ")

    $ chat_message("incri: NO HE\"S THE CHEATER") 

    $ chat_message("odxny: So. Not a cuck. She's the cuck.") 

    $ chat_message("incri: IMAGINE NOT KNOWING WHAT A CUCK IS") 

    $ chat_message("odxny: YOU LITERALLY DON'T KNOW ",ot="elimf")

    $ chat_message("elimf: I HEARD WNPEP IS A CUCK", fastmode=True) 

    $ chat_message("wnpep: I'M NOT MARRIED")
    
    jump day2_37

    #[2] MC: money problems?   

label day2_35: 
    $ points_seekLove += 1

    $ chat_message("odxny: Common, but... SOMEONE lost our bank network. ")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: i said sorry already ")

    #MC: how did you lose access? I thought we made copies of data 
    $ player_choice(
        [
            ("how did you lose access? I thought we made copies of data", "x")
        ]
    )

    $ chat_message("odxny: Sometimes we get unlucky and people wipe our archives.") 

    $ chat_message("elimf: on ACCIDENT bro ", ot="incri")

    $ chat_message("incri: inconvenient as fuck to lose that ")

    $ chat_message("incri: i'm still mad tbh ")

    $ chat_message("incri: {image=e_serious}")

    $ chat_message("wnpep: i'm sorta disappointed too. ")

    $ chat_message("elimf: no... not the disappointment...")

    $ chat_message("wnpep: be better.")

    $ chat_message("odxny: We'll get more data eventually.")

    $ chat_message("odxny: in the meantime, though, what else could we search for? ")

    $ player_choice(
        [
            ("infidelity?", "day2_34"), 
            ("not sure. could be anything", "day2_36")
        ]
    )

    #[3] MC: not sure. could be anything 
label day2_36: 

    $ chat_message("odxny: Not even a guess? Disappointing.", ot="elimf") 

    $ chat_message("elimf: cheating ")

    $ chat_message("elimf: infidelity ")

    $ chat_message("elimf: ultimate spouse betrayal ")

    $ chat_message("wnpep: they might have an open relationship. never assume ")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: the stats are on my side ")

    $ chat_message("odxny: Agreed. It's more likely that this cop is monogamous. But, who knows? ")

    $ chat_message("elimf: do you wish more relationships were open wn")

    $ chat_message("elimf: no reason")

    $ chat_message("wnpep: no opinion",ot="elimf")

    $ chat_message("elimf: married")

    # pause 0.2
    # play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos

    jump day2_37

    # end choices 
label day2_37: 

    $ chat_message("incri: use bruce's email to see if he's here thrim ")

    $ chat_message("incri: #secretsmooch.users#")
    pause 0.5
    $ tables_seen.append("secretsmooch.users")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("TABLE LIST UPDATED")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["ss_alias"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["secretsmooch.users"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("ss_cid", "72770-SS")] # this needs to change to allow a join find to work later on. i'm not sure why it didn't work
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False
        waiting_label = "day2_39"

    $ chat_message("elimf: ol' faithful secretsmooch")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: shameful. that site is specifically for cheating ",ot="incri")

    $ chat_message("elimf: wait i have a CRITICAL question for the group")

    $ chat_message("wnpep: ?", ot="elimf")

    $ chat_message("elimf: if u were cheating on ur spouse and had a secretsmooch account")

    $ chat_message("elimf: what would ur username be")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: seriously?",ot="elimf")

    $ chat_message("elimf: required 2 answer",ot="incri")

    $ chat_message("elimf: mine would obviously be sexLord")

    $ chat_message("odxny: No 420?")

    $ chat_message("elimf: {image=e_pain}")
    
    $ chat_message("elimf: tf kind of basic stoner do u think i AM")

    $ chat_message("odxny: I mean.")

    $ chat_message("elimf: incri ur turn")

    $ chat_message("incri: b1tChfvCk3R69")

    $ chat_message("elimf: LMAOOOOOOOOOOOOOOOOOO?????")

    $ player_choice(
        [
            ("wow uh. very cool!", "day2_37_inc_1"), 
            ("that's so incredibly stupid", "day2_37_inc_2")
        ]
    )

label day2_37_inc_1: 
    $ points_seekLove += 1

    $ chat_message("incri: ty")

    jump day2_37_inc

label day2_37_inc_2: 

    $ chat_message("incri: pls like urs will b ev en sick at all")

    jump day2_37_inc

label day2_37_inc: 

    $ chat_message("wnpep: shouldn't use that type of language for women in a username")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: uh huh ok expert wifeguy")

    $ chat_message("wnpep: i'm not married")

    $ chat_message("elimf: answer the question wnpep")
    
    $ chat_message("wnpep: i dont have an answer because i wouldn't cheat.")

    $ chat_message("incri: is she in the room with u rn")

    $ chat_message("wnpep: who?")

    $ chat_message("incri: stupid")

    $ chat_message("elimf: ok what abt u thrim")

    $ chat_message("elimf: gonna need ur answer")

    $ chat_message("elimf: {image=e_orz}")

    $ player_choice(
        [
            ("but wnpep didnt answer!", "day2_37_1"), 
            ("ok ez. mine would be...", "day2_37_2")
        ]
    )

# sexlord
# where 420 
# basic stoner u think i am 

label day2_37_1: 

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: lol u think u have the same freedom here as wnpep")

    $ chat_message("incri: answer peon")

    $ player_choice(
        [
            ("fuck's sake. mine would be...", "x")
        ]
    )

    jump day2_37_2

label day2_37_2: 

    $ player_choice(
        [
            ("SecretLover", "day2_37_2_A"), 
            ("fistingChamp92", "day2_37_2_B"), 
            ("slackin_and_whackin", "day2_37_2_C")
        ]
    )

label day2_37_2_A: 

    $ chat_message("elimf: {image=e_pain}")
    
    $ chat_message("elimf: ur so unbelievably boring")

    $ chat_message("wnpep: it's sort of romantic. for a cheating username.")

    $ player_choice(
        [
            ("look...", "x")
        ]
    )

    jump day2_37_2_cont

label day2_37_2_B: 
    $ points_seekLove += 1

    $ chat_message("elimf: CHAMP?")

    $ chat_message("incri: probs a liar. probs never done it before")

    $ player_choice(
        [
            ("u dont know me", "x")
        ]
    )

    $ chat_message("incri: no fisting vibes honestly")

    $ chat_message("wnpep: what exactly is a \"fisting vibe\"")

    $ chat_message("incri: ya u definitely dont either")

    jump day2_37_2_cont


label day2_37_2_C: 
    $ points_seekLove += 1

    $ chat_message("elimf: oh HELL yea brother")

    $ player_choice(
        [
            ("every day brother", "x")
        ]
    )

    $ chat_message("elimf: every day")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: juvenile.")

    $ chat_message("incri: cringe i agree")

    $ chat_message("elimf: LMAO")

    jump day2_37_2_cont


label day2_37_2_cont: 

    $ chat_message("wnpep: don't we have a hack to do?")

    $ chat_message("elimf: hold up. what's odxny's")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("incri: lol like theyd answr")

    $ chat_message("elimf: u never know")

    $ chat_message("odxny: I'm good, thanks.")

    $ chat_message("elimf: heaviest of sighs")

    $ chat_message("incri: we entitle u b1tChfvCk3R70")

    $ chat_message("odxny: Back to the hack.")

    $ chat_message("incri: FINE")

    $ chat_message("incri: THRIM")

    $ chat_message("incri: {color="+color_help+"}CHECK FOR BRUCE\"S EMIAL IN THE SECRETSMOOCH TABLE IMMEDIATELY{/color}")

    jump wait_start

    # waits for MC 
# label day2_38:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_39"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_39 
#     $ renpy.pause(hard=True)

label day2_39:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    # MC: i got it! he's totally here! 
    $ player_choice(
        [
            ("i got it! he's totally here!", "x")
        ]
    )

    $ chat_message("incri: I KNEW IT ")

    $ chat_message("incri: I FKCIN GOT YOU ")

    $ chat_message("incri: give username ")

    $ chat_message("incri: {image=e_letsgo}")

    #MC: alias? 
    $ player_choice(
        [
            ("alias?", "x")
        ]
    )

    $ chat_message("incri: whatevr it's called god ")

    #MC: it's "OfficerOral" 
    $ player_choice(
        [
            ("it's \"OfficerOral\"", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("alias: \n'OfficerOral'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("INFO TAB UPDATED")
    pause 0.5

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: LOOOOOOOOOOOOOOLLLLLLLLLLLLLLLLLLLLLL ",ot="odxny")

    $ chat_message("odxny: Ha. Really? ",ot="elimf")

    $ chat_message("elimf: HOLY SHIT ",fastmode=True)

    $ chat_message("wnpep: shameful. ",ot="elimf")

    $ chat_message("elimf: OFFICER I'VE BEEN A BAAAAAAAAAD BOYYYYYYYY ")

    $ chat_message("wnpep: ur a guy?????? ")

    $ chat_message("elimf: i'nm not a ")

    pause 2 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: oh my fucking god you fucking did this to me ")

    $ chat_message("wnpep: YOU COULD HAVE DECLINED TO ANSWER", ot="incri")

    $ chat_message("incri: \"OfficerOver\" ")

    $ chat_message("incri: he's fucking cook ed ")

    $ chat_message("incri: ty thrim ")

    $ chat_message("incri: {image=e_sparkle}")

    $ player_choice(
        [
            ("no problem. i think", "day2_40"), 
            ("i don't know if i did anything really ", "day2_41")
        ]
    )

    #[1] MC: no problem. i think 
label day2_40: 
    $ points_seekLove += 1

    $ chat_message("wnpep: u did great! be proud ")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: mastered basic commands for seekL ")

    $ chat_message("elimf: so good at typing things people tell you to type! ")

    $ chat_message("elimf: i'm clapping irl ")

    #MC: .... thanks. 
    $ player_choice(
        [
            (".... thanks.", "x")
        ]
    )

    $ chat_message("wnpep: yay!") 

    $ chat_message("wnpep: {image=e_sparkle}")

    jump day2_42

    #[2] MC: i don't know if i did anything really 
label day2_41: 

    $ chat_message("incri: u didnt i was tyring to be a good leader") 

    $ chat_message("incri: make u feel cool for ")

    $ chat_message("incri: writin the lamest code i've ever seen ")

    $ chat_message("incri: {image=e_pain}")

    #MC: have u ever said anything nice to anyone ever 
    $ player_choice(
        [
            ("have u ever said anything nice to anyone ever", "x")
        ]
    )

    $ chat_message("incri: i am the nicest person u will evr meet ")

    jump day2_42

    # end choices

label day2_42: 

    $ chat_message("odxny: How much are you asking for?") 

    $ chat_message("incri: silence for $50k ")

    $ chat_message("incri: 20% for u boss? ")

    $ chat_message("odxny: Thanks. Yep ")

    pause 1.5

    $ chat_message("SYSTEM: EXTORTION SENT -  BRUCE.JOHNSON@COPMAIL.COM")

    $ chat_message("incri: ahhhhhhhhhh")

    #MC: how long will it take for him to respond? 
    $ player_choice(
        [
            ("how long will it take for him to respond?", "x")
        ]
    )

    $ chat_message("wnpep: some take days, some take minutes ")

    $ chat_message("wnpep: just depends on the person ")

    pause 1.0

    $ chat_message("SYSTEM: RESPONSE - BRUCE.JOHNSON - This is bullshit. That's not my profile. I'm sending this threat to the police. ")

    #$ chat_message("incri: oh he's fast ")
    $ player_choice(
        [
            ("oh he's fast", "x")
        ]
    )

    $ chat_message("odxny: Bit mad. ")

    $ chat_message("elimf: typical ",ot="incri")

    $ chat_message("incri: reply time ")

    pause 0.5

    $ chat_message("SYSTEM: EXTORTION SENT - BRUCE.JOHNSON@COPMAIL.COM ")

    $ chat_message("elimf: what'd you send this time? ")

    $ chat_message("incri: secret ",ot="odxny")

    $ chat_message("incri: {image=e_orz}",ot="odxny")

    $ chat_message("odxny: I can see what they sent. Brutal. ")

    $ chat_message("incri: i'm getting his money ")

    pause 0.5

    $ chat_message("SYSTEM: RESPONSE - BRUCE.JOHNSON - Please don't. Wiring now. Sincerely sorry. ")

    $ chat_message("incri: I NEVER LOSE")

    $ chat_message("incri: {image=e_letsgo}")

    pause 0.5

    jump day2_moneyrain

label day2_moneyrain:

    #play sound "audio/sfx/chaching.mp3"

    play chat "audio/sfx/Casino_Jackpot_001.ogg" loop fadeout 0.2

    # make it rain money??  
    show money_rain onlayer screens

    $ force_scroll_down()

    pause 0.5

    $ chat_message("SYSTEM: PAYMENT PLAN INITIATED FOR - $ 50 , 000")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF SAYS HORN IT UP")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI SAYS HORN IT UP")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: SO EZ EZ EZ ZE ZE ZE EZ ",ot="elimf")

    $ chat_message("elimf: wow that was the fastest one yet ",ot="incri")

    pause 0.2

    hide money_rain onlayer screens with Dissolve(0.5)
    stop chat fadeout 0.5

    $ force_scroll_down()

    pause 0.5 

    $ chat_message("incri: AHHHHHHHHHHHHHHHH")
     
    $ chat_message("incri: FREEDOM. I\"M FREEEEEEEE ")

    $ chat_message("incri: {image=e_letsgo}")

    pause 0.2

    $ chat_message("elimf: whoa really? is that ur last one ")

    $ chat_message("incri: YES ")

    $ chat_message("wnpep: aw. i guess i only have one left as well ")

    $ chat_message("elimf: wait me too ")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("wnpep: omg? ",ot="odxny")

    $ chat_message("odxny: It's almost time. ",ot="incri")

    $ chat_message("incri: I\"M A FUCKING GOD ")

    $ chat_message("incri: NOBODY FUCKING OWNS ME I OWN THEM ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: I OWN ALL OF THEM ",ot="elimf")

    $ chat_message("elimf: respectfully can you shut the fuck up ")

    $ chat_message("incri: I COULD OWN YOU TOO ")

    $ chat_message("elimf: u've tried. i saw it a month ago. fucking failed ")

    pause 2 

    $ chat_message("incri: that asnt fme ")

    $ chat_message("elimf: don't lie to me inc ",ot="incri")

    $ chat_message("incri: i would own you if i tried ")

    $ chat_message("incri: 1st try ",ot="elimf")

    $ chat_message("elimf: lol ",ot="incri")

    $ chat_message("incri: 1ST TRY ",ot="wnpep")

    $ chat_message("wnpep: woo congrats incri! please relax ")

    $ chat_message("incri: BUZZKILL CHAT ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: jhkfejkhws0-0h  0909  999  9f9g9   ")

    # incri logs off 

    $ chat_message("wnpep: but. anyway. it is crazy. never thought this would all be over this soon. ")

    # MC: what do you mean? 
    $ player_choice(
        [
            ("what do you mean?", "x")
        ]
    )

    $ chat_message("odxny: Everyone came in here with set goals. Those goals are almost met. ")

    $ chat_message("odxny: When they are, I'm shutting this down for good. ")

    # MC: why?? what about if i have goals? 
    $ player_choice(
        [
            ("why?? what about if i have goals? ", "x")
        ]
    )

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: I don't really care. No offense. ")

    $ chat_message("odxny: It's about time. ")

    # MC: then... you won't ever talk to each other again? 
    $ player_choice(
        [
            ("then... you won't ever talk to each other again?", "x")
        ]
    )

    $ chat_message("wnpep: life is made up of meetings and partings ")

    $ chat_message("wnpep: that is the way of it ")

    pause 1 

    $ chat_message("elimf: that's a fucking muppet quote ")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: watched it last christmas. great movie ")

    $ chat_message("elimf: with your wife? ")

    $ chat_message("wnpep: yes!") 

    pause 2 

    $ chat_message("elimf: WHAT ")

    $ chat_message("wnpep: wait ")

    $ chat_message("wnpep: no i misread it i misread it ",ot="elimf")

    $ chat_message("elimf: THE PRIVACY PACT",ot="odxny")

    $ chat_message("odxny: So. Enjoy your short time here, thrim. Our last member. ")

    $ player_choice(
        [
            ("shit I gotta cram all my enjoyment in then", "day2_43"), 
            ("We're just ships passing in an undetermined time zone, huh", "day2_44")
        ]
    )


    # [1] MC: shit I gotta cram all my enjoyment in then
label day2_43:

    $ chat_message("elimf: didnt realize u were into the grind")

    # MC: u know it
    $ player_choice(
        [
            ("u know it", "x")
        ]
    )

    $ chat_message("wnpep: i'm not sure if this is how joy works")

    jump day2_45


    # [2] MC: We're just ships passing in an undetermined time zone, huh
label day2_44:
    $ points_seekLove += 1

    $ chat_message("odxny: Thank you for the sincere and edited idiom.")

    # MC: I had to offer an equally fine allusion
    $ player_choice(
        [
            ("I had to offer an equally fine allusion", "x")
        ]
    )

    $ chat_message("elimf: and it is. love movies")

    jump day2_45


    # end choices
label day2_45:

    $ chat_message("incri: cry less hard thrim")

    $ chat_message("incri: u will leave here a bit less stupid thanks to me")

    # MC: of course
    $ player_choice(
        [
            ("of course", "x")
        ]
    )

    $ chat_message("incri: im done so ur on ur own. no more help from me")

    # MC: I think I got that, yeah. thanks for helping earlier tho
    $ player_choice(
        [
            ("I think I got that, yeah. thanks for helping earlier tho", "x")
        ]
    )

    $ chat_message("incri: finally some     GRATITUDE")

    $ chat_message("wnpep: look what youve done. youve enabled them")

    $ chat_message("elimf: gonna be such an overlord")

    $ chat_message("wnpep: of another server? god forbid",ot="incri")

    $ chat_message("incri: fuck both of u")

    $ chat_message("elimf: no just like. in general")

    $ chat_message("elimf: with a hat n stuff")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: are you high rn")

    $ chat_message("elimf: :^)")

    $ chat_message("odxny: I'd love to see incri run something.")

    $ chat_message("incri: thank u")

    $ chat_message("odxny: From a safe distance.")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: fuck u too")

    # dms

    $ chat_message("odxny: I won't lie, I'm a little impressed.",c="admin")

    # MC: how so?
    $ player_choice(
        [
            ("how so?", "x")
        ]
    )

    $ chat_message("odxny: Managing to get incri to be anything close to helpful is quite a feat",c="admin")

    $ chat_message("odxny: Have to give props where it's due.",c="admin")

    $ player_choice(
        [
            ("about time!!", "day2_46"), 
            ("it was a struggle but we got there", "day2_47")
        ]
    )


    # [1] MC: about time!!
label day2_46:
    $ points_seekLove += 1

    $ chat_message("odxny: You can't hear it but I'm clapping for you.",c="admin")

    # MC: well now it just feels sardonic
    $ player_choice(
        [
            ("well now it just feels sardonic", "x")
        ]
    )

    $ chat_message("odxny: I'll stop the clapping then.",c="admin")

    # MC: no keep doing that
    $ player_choice(
        [
            ("no keep doing that", "x")
        ]
    )

    $ chat_message("odxny: As you wish.",c="admin")

    jump day2_48


    # [2] MC: it was a struggle but we got there
label day2_47:

    $ chat_message("odxny: We will never forget your sacrifice.",c="admin")

    # MC: do I get a medal? or a plaque?
    $ player_choice(
        [
            ("do I get a medal? or a plaque?", "x")
        ]
    )

    $ chat_message("odxny: I can send you enough money for a commemorative sandwich.",c="admin")

    # MC: two sandwiches?
    $ player_choice(
        [
            ("two sandwiches?", "x")
        ]
    )

    $ chat_message("odxny: Deal.",c="admin")

    jump day2_48


label day2_48:
    # end choices 

    # MC: did you message just to congratulate me tho?
    $ player_choice(
        [
            ("did you message just to congratulate me tho?", "x")
        ]
    )

    $ chat_message("odxny: Well, partially. Felt a bit awkward to do so in the main chat.",c="admin")

    $ chat_message("odxny: But I was also wondering if you wanted to call again.",c="admin")

    # MC: oh?
    $ player_choice(
        [
            ("oh?", "x")
        ]
    )

    $ chat_message("odxny: Just to chat. No vetting this time.",c="admin")

    # MC: no insults?
    $ player_choice(
        [
            ("no insults?", "x")
        ]
    )

    $ chat_message("odxny: Depends.",c="admin")

    $ chat_message("odxny: I'll try to refrain, though.",c="admin")

    $ chat_message("odxny: {image=e_serious}",c="admin")

    # MC: i'll accept that risk, then
    $ player_choice(
        [
            ("i'll accept that risk, then", "x")
        ]
    )

    $ chat_message("odxny: Excellent.",c="admin")


    ## call time 
    jump go_to_call

    $ renpy.pause(hard=True)



