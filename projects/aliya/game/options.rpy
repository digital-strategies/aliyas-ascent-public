## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Aliya's Ascent")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"

define config.build_uid = "20231031.22.04"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define is_web = True if renpy.emscripten else False

define gui.about = _p("""
{b}Welcome to Bridgeworld.{/b}

Aliya’s Ascent is a character driven, interactive adventure story filled with amazing cinematic elements about a girl who mysteriously found herself in the middle of a boat towards an unknown land. Embark on a journey in the world of the first Legions and meet familiar faces as you unravel the tales that made the fabric of Bridgeworld. Every choice you make matters!

Aliya’s Ascent is based off of the Treasure’s 7-part Bridgeworld community-novel {a=https://docs.bridgeworld.treasure.lol/lore/bridgeworld-season-1-aliyas-ascent/prologue-migration}Aliya’s Ascent{/a}, which is also available in Audiobook format {a=https://docs.bridgeworld.treasure.lol/lore/bridgeworld-season-1-aliyas-ascent/audio-book}here{/a}.

{b}Features{/b}

- Fully illustrated story\n
- Complete voiceovers\n
- Multiple Endings\n
- 50+ Unlockable Gallery Images\n
- Gallery view unlocked in the game

{b}Larger world of Treasure{/b}

Aliya’s Ascent is just a part of the larger world of Bridgeworld, learn more about the game here: {a=https://bridgeworld.treasure.lol/}https://bridgeworld.treasure.lol/{/a}

{a=https://treasure.lol}Treasure{/a} is a vast decentralized gaming ecosystem of games bringing games and players together through MAGIC. Games in the ecosystem include Bridgeworld (strategy), Smolville (simulation), The Beacon (roguelite), Knights of the Ether (deckbuilding), Bitmates (survival), Kuroro Beasts (battler) and more!

{b}Open-Source Development{/b}

Aliya’s Ascent is fully open-source. The source code can be found at {a=https://github.com/digital-strategies/aliyas-ascent-public}https://github.com/digital-strategies/aliyas-ascent-public{/a}. Follow our game development blog for the latest updates and sneak peaks of our development content:
{a=https://insights.digistrats.com}Game Dev Blog{/a}

This is our first game and we’re a small team of passionate game players. We humbly look forward to your feedback.
%s
{b}Aliya's Ascent and Treasure Community{/b}

Join Aliya's Ascent discord {a=https://x.ascent.lol/discord}here{/a}.\n
Join Treasure’s discord {a=https://discord.gg/treasuredao}here{/a}.

{b}Credits{/b}

To see the full credits, visit our {a=https://github.com/digital-strategies/aliyas-ascent-public#credits}Github{/a}.
\n
""" % ("""\n{b}Versions{/b}

The game is available on multiple platforms. The Treasure badge achievement integration is only available in the full-featured version of Aliya's Ascent that is available to play on {a=https://ascent.lol}https://ascent.lol{/a}.\n""" if is_web else ""))


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "aliya"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# define config.main_menu_music = "audio/bg_music4.ogg"
# define config.main_menu_music_fadein = 1.0


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(0)
define config.window_hide_transition = Dissolve(0)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 30


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_enable = False
default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "aliyas-ascent" if renpy.emscripten else None


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "digistrats/aliyas-ascent"

define build.destination = "aliya-dist"
define build.directory_name = "aliya"
define build.executable_name = "ascent"

## Steam configuration #########################################################
##
## Steam related config.

define achievement.steam_position = "top left"

define config.steam_appid = 2660930
