# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define tim = Character("Tim")
define unknown = Character("...")
define jack = Character("Jack")


# The game starts here.

label start:
    show bg bed
    show tim asleep
    unknown "Are you awake yet?"
    unknown "..."
    unknown "Hey are you awake?"
    return