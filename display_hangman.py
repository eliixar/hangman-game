def display_hangman(chances):

    if (chances == 9):
         print("\n ---------------  "
              "\n        |          "
              "\n      _/O\_        "  
              "\n       \|/         "
              "\n        |          "
              "\n      _/ \_        " 
        "\n You have 9 chances remaining! ")
         
    elif (chances == 8):
         print( "\n ---------------  "
              "\n        |          "
              "\n        O          "  
              "\n       \|/         "
              "\n        |          "
              "\n      _/ \_         " 
        "\n You have 8 chances remaining! ")

    elif (chances == 7):
        print( "\n ---------------  "
              "\n        |          "
              "\n        O          "  
              "\n       \|/         "
              "\n        |          "
              "\n       / \_        " 
        "\n You have 7 chances remaining! ")

    elif (chances == 6):
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
