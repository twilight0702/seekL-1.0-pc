﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        # if who is not None:

        #     window:
        #         id "namebox"
        #         style "namebox"
        #         text who id "who"
        text what:
            id "what" 
            text_align 0.0 
            xalign 0.1
            size gui.text_size #+ 5 
            color character_colors["odxny"] 
            xsize gui.dialogue_width
            outlines [ (3, "#11173f", 0, 0) ]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor 0.0#gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign 0.0 #gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign 0.0 #gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# for i, (caption, action, chosen) in enumerate(items):
#     button:
#         text caption
#         action [Function(log_menu_choice, caption), action]
init python: 
    ### code to add choices to history window
    def log_menu_choice(item_text):
        global in_call
        if item_text != "Menu Prediction" and in_call:
            """Log a choice-menu choice, which is passed in as item_text.
            Implementation based on add_history() in renpy/character.py."""
            h = renpy.character.HistoryEntry()
            h.who = ""
            h.what = "> " + item_text
            h.what_args = []

            if renpy.game.context().rollback:
                h.rollback_identifier = renpy.game.log.current.identifier
            else:
                h.rollback_identifier = None

            _history_list.append(h)

            while len(_history_list) > renpy.config.history_length:
                _history_list.pop(0)

default first_line = False 
screen choice(items):
    style_prefix "choice"

    vbox:
        spacing 0 
        if in_call: 
            xalign 0.1

            ypos gui.dialogue_ypos + 750 #700
            #for h in _history_list:
         
            if _history_list and not first_line: 
                $ what = renpy.filter_text_tags(_history_list[len(_history_list)-1].what, allow=gui.history_allow_tags)
                text what:
                    #adjust_spacing False
                    #style_prefix "say"
                    substitute False
                    font gui.text_font
                    size gui.text_size - 2
                    xalign 0.0
                    text_align 0.0
                    xmaximum gui.dialogue_width-300
                    #size 20 
                    if _history_list[len(_history_list)-1].who: 
                        color character_colors["odxny"] + "99"
                        outlines [ (3, "#11173f", 0, 0) ]
                    else: 
                        color character_colors["thrim"] + "99"
                        outlines [ (3, "#17173f", 0, 0) ]
                null height 20 
        
        else: 
            #xpos 320
            if len(items) > 2: 
                ypos 860 
        if in_call or current_window == active_window: 
            for i in items:
                textbutton "> " + i.caption: 
                    #action i.action 
                    action [Function(log_menu_choice, i.caption), i.action]
                    text_align 0.0 
                    if in_call:
                        xalign 0.0
                        text_outlines [ (3, "#17173f", 0, 0) ]
                    if in_call: 
                        text_size gui.text_size #+ 5
                        text_hover_color character_colors["thrim"]
                        #text_hover_color "#FFFFFF"
                    elif len(items) > 2: 
                        text_size gui.text_size - 3
                    else: 
                        text_size gui.text_size
                    background None 
                    if in_call:
                        xmaximum 800
                    else: 
                        xmaximum 900


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xpos 50
    xanchor 0.0
    ypos 870
    yanchor 0.0

    spacing 0 # gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    default qtt = Tooltip("")

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.04
            yalign 0.99
            spacing 6

            imagebutton:
                auto "gui/button/backbutton_%s.png"
                hovered qtt.Action("rollback")
                #action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), 
                action Rollback()  

            imagebutton:
                auto "gui/button/history_%s.png"
                hovered qtt.Action("call history")
                action Show('history')

            # imagebutton:
            #     auto "gui/button/skip_%s.png"
            #     action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Skip() alternate Skip(fast=True, confirm=True)

            imagebutton:
                auto "gui/button/save_%s.png"
                hovered qtt.Action("save")
                action Show('save')
                tooltip "x"

            # imagebutton:
            #     auto "gui/button/qsave_%s.png"
            #     action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), QuickSave()

            imagebutton:
                auto "gui/button/qload_%s.png"
                hovered qtt.Action("load")
                action Show('load')
            
            imagebutton:
                auto "gui/button/prefs_%s.png"
                hovered qtt.Action("preferences")
                action Show('preferences')
        
            if in_call:
                imagebutton:
                    if _preferences.afm_enable:
                        idle "gui/button/auto_hover.png"
                    else: 
                        auto "gui/button/auto_%s.png"
                    hovered qtt.Action("auto")
                    action Preference("auto-forward", "toggle")
            else: 
                imagebutton:
                    if player_is_waiting: 
                        idle "gui/button/auto_inactive.png" 
                    elif not is_paused: 
                        idle "gui/button/auto_hover.png"
                    else: 
                        auto "gui/button/auto_%s.png"
                    hovered qtt.Action("auto")
                    if player_is_waiting: 
                        action NullAction() 
                    elif not is_paused:
                        action [SetVariable("is_paused", True),SetVariable("_preferences.afm_enable", False)]#SetVariable("is_paused", True), SetVariable("player_set_pause", True), SetVariable("_preferences.afm_enable", False)
                    else: 
                        action [Function(renpy.mode, "say"),SetVariable("is_paused", False),SetVariable("_preferences.afm_enable", True)]
        frame:
            # set this frame to the position of the mouse
            pos (55, 971)#, 291, 30)#renpy.get_mouse_pos() 
            background None 

            # display text with value set in tt.Action() above.
            text qtt.value outlines [ (3, "#252F71", 0, 0) ]


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    ## Ensure this appears on top of other screens.
    zorder 100

    # if main_menu: 
    #     textbutton _("SECURE DIAL"): 
    #         xalign 0.5 
    #         yalign 0.9
    #         action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("secure_dial")

    vbox:
        style_prefix "navigation"

        xalign 0.5
        yalign 0.58

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("START") action Play("sound", "audio/sfx/ui_start_game_001 start.ogg"), Start()

        else:

            textbutton _("HISTORY") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), ShowMenu("history")

            textbutton _("SAVE") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), ShowMenu("save")

        textbutton _("LOAD") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), ShowMenu("load")

        textbutton _("PREFERENCES") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), ShowMenu("preferences")

        textbutton _("GALLERY") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("gallery")

        if persistent.seekLove and persistent.seekLife and persistent.seekLoss: 

            textbutton _("BONUS") text_color character_colors["odxny"] text_hover_color gui.hover_color  action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("music_room", mr=my_room)
        else: 
            textbutton _("BONUS") action NullAction() text_color "#686868"

        if _in_replay:

            textbutton _("END REPLAY") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("MAIN MENU") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), MainMenu()

        #textbutton _("About") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("HELP") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("QUIT") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5


## Gallery screen ############################################################
##
## Allowing underfull grids - For Gallery ##########################################################
# This line of code is so an error isn't thrown if the gallery grid isn't completely full.
#define config.allow_underfull_grids = True

init python:
    #    # image cg necklace= "cg necklace.jpg"
    gallery_page = "1" # we're using code similar to the 'help' screen to switch gallery pages
    gal = Gallery() # Setting up the gallery
    gal.button("bad") # defining the first CG button
    gal.condition("persistent.seekLoss")
    gal.image("cg bad") # which picture it unlocks

    gal.button("platonic")
    gal.condition("persistent.seekLife")
    gal.image("cg platonic_zoom")

    gal.button("romantic")
    gal.condition("persistent.seekLove")
    gal.image("cg romantic_zoom")
    #gal.unlock_image("cg cage smile") #This button has variations, so we add an additional unlock image

    gal.transition = dissolve # What transition is used when CGs are shown

# Gallery image previews ###########
# Rendering smaller versions of the CGs to use as the preview image
image bad_cg_preview:
    "cg bad"
    zoom 0.36
    #xoffset +15
    yoffset +65
image gallery_locked:
    "gui/button/gallery_locked.png"
    zoom 0.36
    #xoffset +15
    yoffset +65
image platonic_cg_preview:
    "cg platonic"
    zoom 0.18
    #xoffset +15
    yoffset +65
image romantic_cg_preview:
    "cg romantic"
    zoom 0.18
    #xoffset +15
    yoffset +65

screen gallery():
    ## Ensure this appears on top of other screens.
    zorder 100
    modal True
    tag menu
    #use navigation

    use game_menu("GALLERY"):
        #text "Page [gallery_page]" style "page_label_text" xalign 0.5 ypos 5
        hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing 30

                #Pages to change gallery screens
                if gallery_page=="1":
                    textbutton "{color=66cc00}seek{/color}{color=b3b3af}Loss{/color}": 
                        action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), SetScreenVariable("gallery_page","1")
                else: 
                    textbutton "seek{color=b3b3af}Loss{/color}": 
                        action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), SetScreenVariable("gallery_page","1")
                
                if gallery_page=="2": 
                    textbutton "{color=66cc00}seek{/color}{color=ecde8f}Life{/color}":
                        action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), SetScreenVariable("gallery_page","2")
                else:
                    textbutton "seek{color=ecde8f}Life{/color}":
                        action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), SetScreenVariable("gallery_page","2")
                
                if gallery_page=="3":
                    textbutton "{color=66cc00}seek{/color}{color=f57cdf}Love{/color}":
                        action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), SetScreenVariable("gallery_page","3")
                else:
                    textbutton "seek{color=f57cdf}Love{/color}":
                        action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), SetScreenVariable("gallery_page","3")
        
                # "#f57cdf"
        #determines which page of CGs to show
        if gallery_page == "1":
            use gallery_1
        elif gallery_page == "2":
            use gallery_2
        elif gallery_page == "3":
            use gallery_3
#CG grids
screen gallery_1:
    modal True
    frame:
        
        #style "game_menu_content_frame"
        ysize 600
        xsize 1100
        ypos 0.1
        xpos 0.26
    
        background None

        hbox:
        #grid gui.file_slot_cols gui.file_slot_rows:
        #spacing 15
        #ysize 500
        #xsize 700
            frame:
                background None
                #ypos 50
                #xpos 20
            #style_prefix "slot"
            #xalign 0.4
            #yalign 0.37
            #xspacing 40
            #yspacing 100

                add gal.make_button("bad","bad_cg_preview","gallery_locked", xpadding = 0, ypadding = 0, xmargin = 0,ymargin = 0, background = None,style ="gui_button")
         
            # frame:
            #     background None
            #     ysize 520
            #     xsize 500
            #     xpos 75
            #     padding (25,40,25,25)

            #     viewport:
            #         scrollbars "vertical"
            #         mousewheel True
            #         draggable True
            #         #ymaximum 500
                    
            #         frame:
            #             background None
            #             if persistent.seekLoss:
            #                 text "the cops cleaned up my whole weed stash bro they took EVERYTHING"



#Gallery second page
screen gallery_2:
    modal True
    frame:

        ysize 600
        xsize 1100
        ypos 0.1
        xpos 0.26
    
        background None

        hbox:
            frame:
                background None
                add gal.make_button("platonic","platonic_cg_preview","gallery_locked", xpadding = 0, ypadding = 0, xmargin = 0,ymargin = 0, background = None,style ="gui_button")
         
            # frame:
            #     background None
            #     ysize 520
            #     xsize 500
            #     xpos 75
            #     padding (25,40,25,25)

            #     viewport:
            #         scrollbars "vertical"
            #         mousewheel True
            #         draggable True
                    
            #         frame:
            #             background None
            #             if persistent.seekLife:
            #                 text "we shook hands"

screen gallery_3:
    modal True
    frame:

        ysize 600
        xsize 1100
        ypos 0.1
        xpos 0.26
    
        background None

        hbox:
            frame:
                #xalign 0.5
                background None
                add gal.make_button("romantic","romantic_cg_preview","gallery_locked", xpadding = 0, ypadding = 0, xmargin = 0,ymargin = 0, background = None,style ="gui_button")
         
            # frame:
            #     background None
            #     ysize 520
            #     xsize 500
            #     xpos 75
            #     padding (25,40,25,25)

            #     viewport:
            #         scrollbars "vertical"
            #         mousewheel True
            #         draggable True

            #         frame:
            #             background None
            #             if persistent.seekLove:
            #                 text "we HELD hands"



## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"
        xalign 0.02

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            xalign 0.5 yalign 0.25

            text "{u}seekL{/u}":
                style "main_menu_title"
                

            #text "[config.version]":
                #style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    
    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

transform game_menu_popup:
    on show:
        yoffset 1080
        easein_back 0.8 yoffset 0
    on hide:
        yoffset 0
        pause 0.5
        easeout_back 0.8 yoffset 1080

transform game_menu_popup_video:
    on show:
        yoffset 1080
        easein_back 0.8 yoffset 0


screen game_menu(title, scroll=None, yinitial=0.0):

    ## Ensure this appears on top of other screens.
    zorder 99
   
    
    style_prefix "game_menu"   

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background at game_menu_popup
        

    frame at game_menu_popup:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude
                
                
                elif scroll == "vpgrid_history":

                    vpgrid:
                        cols 1
                        ysize 520
                        ypos 0.15

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    hbox at game_menu_popup:
        #style_prefix "navigation"
        xsize 1000
        xalign 0.7
        yalign 0.19

        spacing 50

        # if main_menu:

        #     textbutton _("START") action Play("sound", "audio/sfx/ui_start_game_001 start.ogg"), Start()

        if not main_menu:

            textbutton _("HISTORY") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("history")

            textbutton _("SAVE") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("save")

        textbutton _("LOAD") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("load")

        textbutton _("PREFERENCES"): 
            text_hover_color gui.hover_color
            action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("preferences")

        if main_menu: 

            textbutton _("GALLERY") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("gallery")

            if persistent.seekLove and persistent.seekLife and persistent.seekLoss: 

                textbutton _("BONUS") text_color character_colors["odxny"] text_hover_color gui.hover_color action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Show("music_room", mr=my_room)
            else: 
                textbutton _("BONUS") action NullAction() text_color "#686868"

        #null width 50 

        text "//" yalign 0.5 color gui.insensitive_color bold True 

        if _in_replay:

            textbutton _("END REPLAY") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("MAIN MENU"):
                # text_color gui.idle_color
                # text_hover_color gui.hover_color
                action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), MainMenu()

        #textbutton _("About") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("HELP") action ShowMenu("help")

        if renpy.variant("pc"):

            #null width 50

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("QUIT"):
                # text_color gui.idle_color
                # text_hover_color gui.hover_color
                action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), Quit(confirm=not main_menu)

        #null width 50

        textbutton _("RETURN"):
            # text_color gui.hover_muted_color
            # text_hover_color gui.hover_color
            #style "return_button"
            if main_menu: 
                #action Play("sound", "audio/sfx/ui_menu_back_001 hangup.ogg"), 
                action Return() 
            else: 
                action Hide(title.lower())

    label title at game_menu_popup

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")



style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 95
    top_padding 200

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 260
    yfill True

style game_menu_content_frame:
    left_margin 80
    right_margin 30
    top_margin 80

style game_menu_viewport:
    xsize 1475
    ysize 570
    ypos 0.1
    


style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 480
    ysize 140

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

init python:
    # custom save/load screens
    def add_save_image(d):
        d["save_image"] = "gui/new_main_menu/saves/" + route +  "_" + str(dayofweek_actual) + ".png"
    config.save_json_callbacks = [add_save_image]

    def add_save_text(d):
        d["save_text"] = chat_location
    config.save_json_callbacks = [add_save_text]

screen save():
    ## Ensure this appears on top of other screens.
    zorder 100

    modal True 

    tag menu

    use file_slots(_("SAVE"))


screen load():
    ## Ensure this appears on top of other screens.
    zorder 100

    modal True 

    tag menu

    use file_slots(_("LOAD"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            # button:
            #     style "page_label"

            #     key_events True
            #     xalign 0.5
            #     yalign 0.0
            #     action page_name_value.Toggle()

            #     input:
            #         style "page_label_text"
            #         value page_name_value

            ## The grid of file slots.
            #grid gui.file_slot_cols gui.file_slot_rows:

            viewport: 
                mousewheel True 
                scrollbars "vertical"
                area(150,100,1250, 500)
                vbox: 
                    #style_prefix "slot" 
                    xalign 0.5
                    yalign 0.7

                    #spacing gui.slot_spacing
                    spacing 2
                    #for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    for i in range(1 * 20):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            #add FileScreenshot(slot) xalign 0.5
                            text FileJson(slot, "save_text", empty=Null(), missing=Null()):
                                yalign 1.0
                                hover_color gui.hover_color
                                color gui.insensitive_color

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                # style "slot_time_text"
                                yalign 0.0
                                hover_color gui.hover_color
                                color gui.insensitive_color

                            text FileSaveName(slot):
                                # style "slot_name_text"
                                yalign 1.0
                                hover_color gui.hover_color
                                color gui.insensitive_color

                            key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            # vbox:
            #     style_prefix "page"

            #     xalign 0.5
            #     yalign 1.0

            #     hbox:
            #         xalign 0.5

            #         spacing gui.page_spacing

            #         textbutton _("<") action FilePagePrevious()

            #         if config.has_autosave:
            #             textbutton _("{#auto_page}A") action FilePage("auto")

            #         if config.has_quicksave:
            #             textbutton _("{#quick_page}Q") action FilePage("quick")

            #         ## range(1, 10) gives the numbers from 1 to 9.
            #         for page in range(1, 10):
            #             textbutton "[page]" action FilePage(page)

            #         textbutton _(">") action FilePageNext()

                #if config.has_sync:
                    #if CurrentScreenName() == "save":
                        #textbutton _("Upload Sync"):
                            #action UploadSync()
                            #xalign 0.5
                            #ypos 0.8
                    #else:
                        #textbutton _("Download Sync"):
                            #action DownloadSync()
                            #xalign 0.5
                            #ypos 0.8


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    ## Ensure this appears on top of other screens.
    zorder 100

    modal True 

    tag menu

    use game_menu(_("PREFERENCES"), scroll="viewport"):


        vbox:

            xpos 0.12
            

            hbox:
                box_wrap True

                vbox: 
                    if renpy.variant("pc") or renpy.variant("web"):

                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    vbox:
                        style_prefix "slider"
                        box_wrap True
                        label _("Text Speed")
                        bar value Preference("text speed")
                
                    vbox:
                        style_prefix "slider"
                        box_wrap True
                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time")

                # vbox:
                #     style_prefix "check"
                #     label _("Skip")
                #     textbutton _("Unseen Text") action Preference("skip", "toggle")
                #     textbutton _("After Choices") action Preference("after choices", "toggle")
                #     textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "slider"
                    box_wrap True

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                vbox:
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("简体中文") text_font "YaHeiMonacoHybrid.ttf" action Language("simple_chinese")               

                    #vbox:
                        #label _("Text Speed")
                        #bar value Preference("text speed")
                        #label _("Auto-Forward Time")
                        #bar value Preference("auto-forward time")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            #null height (4 * gui.pref_spacing)

            # hbox:
            #     style_prefix "slider"
            #     box_wrap True

            #     #vbox:

            #         #label _("Text Speed")

            #         #bar value Preference("text speed")

            #         #label _("Auto-Forward Time")

            #         #bar value Preference("auto-forward time")

            #     vbox:
            #         label _("Text Speed")
            #         bar value Preference("text speed")
                
            #     vbox:
            #         label _("Auto-Forward Time")
            #         bar value Preference("auto-forward time")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

init python: 
    yadj_history = ui.adjustment() 
    yadjValue_history = float("inf") 

screen history():
    ## Ensure this appears on top of other screens.
    zorder 100

    modal True 

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    python: 
        yadj_history.value = yadjValue_history

    

    use game_menu(_("HISTORY")):#), scroll=("vpgrid_history" if gui.history_height else "viewport"), yinitial=1.0):

        viewport yadjustment yadj_history: 
            style_prefix "history"
            mousewheel True 
            scrollbars "vertical"
            area(150,100,1250, 500)
            vbox: 
                xalign 0.5
                yalign 0.7

                spacing 0

                for h in _history_list:

                    window:
                        #background None
                        
                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        # if h.who:

                        #     label h.who:
                        #         style "history_name"
                        #         substitute False

                        #         ## Take the color of the who text from the Character, if
                        #         ## set.
                        #         if "color" in h.who_args:
                        #             text_color h.who_args["color"]
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False
                            font gui.text_font
                            size 20 
                            if h.who: 
                                color character_colors["odxny"]
                            else: 
                                color character_colors["thrim"] + "99"

                if not _history_list:
                    label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    ## Ensure this appears on top of other screens.
    zorder 100

    tag menu

    default device = "keyboard"

    use game_menu(_("HELP"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23
            ysize 200

            hbox:
                xpos 0.5

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), yes_action
                textbutton _("No") action Play("sound", "audio/sfx/message_notification_02_002 tab.ogg"), no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        xfill True 
        text "[message!tq]" size 30 xalign 0.5 #bold True 

    timer 2 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos 0#gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
