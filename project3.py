print(''' _______________
 / \-----     ---------  -----------     -------------- ------    ----\
 \/_____________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ .----------. ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |     ~~ ~~ ,---'       "         . ~~~ ,--.  ~~~~ ,---.  ~~|
 | | \__ ~~ /      ( )   "          "   -.,' (') \~~ ~ (  / \ \~~ |
 |  \    \/   (( )      (    "   "     (\) \~ -.,'  ~|
 |~~ \     (  )(_)|( ))  "   ))          "   |    "  \ ~~ ~~~  ~~|
 |  ~ \ (( ( (  ))  ) )    ((     \\//    " |   "    \_,' | ~|
 |~~ ~   \  ( ))()())|  "    ))    //\\ " _,---.  "  "   "  /~~~|
 |    ~~~ |( )| | |   |   "  (   "      ,-'~~~ ~~~ -.   __  /~ ~ |
 | ~~     |  |  |   |   ,--- ,--.   "  (~~  ~~~~  ~~~ ) /_\ \~~ ~|
 |  ~ ~~ /   |      ,----.,'--'\.-.  .~~~~,-'  |H|  \ ~~|
 |~~    / "     ,-' / \ ,' / '  \.---..          _        " \~ |
 | ~~~ / /   .-' , / ' ,'  -   '- . .-.    /- --.   " " \~|
 |  ~ / / -- ---,~.-'    --  ,---.  -.   ,-'- /  \ \   " |~|
 | ~ | | --     /~/  --   ,' '  \ \-.,-'  / --   \  - \   / |
 |~~ | \ -      /~~| "     ,-' /-   ..-........,--'  /~~|
 | ~~\  \ /   /~~/      ---  ---  - - ' ,--.             |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \,-' ~ .     ,'~~ |
 | ~~ ~|,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~-./~ ~~~|
 |~~~ ~~~  ~~~~~~~~`._____/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |~jrei~~~~~~~~~~~~~\|/ ~~~|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \/______________/''')

print("Welcome to the game where you need to find the treasure.")
print("Lets start!!!!")

choice1 = input("Do you want to take right or left? ").lower()

if choice1 == "left":

    choice2 = input("Do you want to swim or wait? ").lower()

    if choice2 == "wait":

        choice3 = input("Which door? Red, Blue or Yellow? ").lower()

        if choice3 == "red":
            print("Burned by fire.")
            print("Game Over.")

        elif choice3 == "blue":
            print("Eaten by beasts.")
            print("Game Over.")

        elif choice3 == "yellow":
            print("You are near to winning!")
            
            choice4 = input("Dark Yellow or Light Yellow? ").lower()
            
            if choice4 == "dark yellow":
                print("You won")
                
            else:
                print("You lose. SAD")

        else:
            print("Game Over.")

    elif choice2 == "swim":
        print("Attacked by trout.")
        print("Game Over.")

    else:
        print("Game Over.")

elif choice1 == "right":
    print("Fall into a hole.")
    print("Game Over.")

else:
    print("Game Over.")