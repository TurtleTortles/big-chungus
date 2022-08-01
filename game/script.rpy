# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gb80 = Character("Gamerboy80")
define bc = Character("Big Chungus")


# The game starts here.

label start:
    play music bgm

    scene jouch with fade

    show bc happy at left with moveinleft
    bc "What a nice jouch!"
    bc "I think rock is overrated and nobody should play his music."
    bc "Oh, is that Gamerboy80?!?!?!?!?!?!?!"
    play sound "audio/boom.mp3"
    bc "﷽﷽﷽ ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽"
    show gb80 happy at right with moveinright
    gb80 "Omg big chungus my beloved!!!!"
    $ choice = False
    menu:
      "Woppa gangman style?":
        gb80 "Woppa gangman style?"
        $choice = True
      "Before the face reveal my entire comments section was do a face reveal. Now that I've done that, my entire comments section is date me":
        gb80 "Before the face reveal my entire comments section was do a face reveal. Now that I've done that, my entire comments section is date me"

    if choice:
        bc "OMG BEST SONG 4EVAA!!!!"
        play sound "audio/hoodclassic.mp3"
        "... music ending!!!"
        pause 3.0
    else:
        bc "*blushes - d-do you wanna go on a date with me?"
        play sound "audio/ringing.mp3"
        "...love ending!!!"
        pause 3.0
    return
