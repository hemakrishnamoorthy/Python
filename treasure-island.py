#Write your code below this line 👇
direction = input(
    'You are at a crossroad. Where do you want to go today? "left" or "right"?: '
)
if direction.lower() == "right":
    print("Game Over.")
else:
    wait = input(
        'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for for a boat or "swim" to swim across: '
    )
    if wait.lower() == "swim":
        print("Ypu are attacked by a trout. Game Over")
    else:
        door = input(
            'Great! You have come unharmed to the island. There are 3 doors. Type "Red, "Blue" or "Yellow": '
        )
        if door.lower() == 'red':
            print("You are burned by fire. Game Over.")
        elif door.lower() == "blue":
            print("You are eaten by beasts. Game Over.")
        else:
            print("You found the treasure. You win!")
