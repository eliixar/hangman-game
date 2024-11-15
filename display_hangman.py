def display_hangman(chances):
    if (chances == 6):
        print( "\n ---------------  "
              "\n        |          "
              "\n        O          "  
              "\n       \|/         "
              "\n        |          "
              "\n       / \         " 
        "\n You have 6 chances remaining! ")

    elif (chances == 5):
        print(" ----------------    "
              "\n        |          " 
              "\n        O          "   
              "\n       \|          "
              "\n        |          "
              "\n       / \         "
        "\n You have 5 chances remaining! ")

    elif (chances == 4):
        print("\n ----------------"
              "\n        |        "
              "\n        O        "
              "\n        |        "
              "\n        |        "
              "\n       / \       "
        "\n You have 4 chances remaining! ")

    elif (chances == 3):
        print("\n ----------------"
              "\n        |        "
              "\n        O        "
              "\n        |        "
              "\n        |        "
              "\n       /         "
        "\n You have 3 chances remaining! ")

    elif (chances == 2):
        print("\n ---------------"
              "\n        |       "
              "\n        O       "
              "\n        |       "
              "\n        |       "
              "\n                "
        "\n You have 2 chances remaining! ")
        
    elif (chances == 1):
        print("\n ---------------"
              "\n        |       "
              "\n        O       "
              "\n                "
              "\n                "
              "\n                "
        "\n You have 1 chance remaining! ")

    elif (chances == 0):
        print(" You have no chances left and have lost the game! Sorry!")

