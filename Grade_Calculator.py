def Grade_Calculator():
    print("This Tool Calculates Your Grade Based On Your Marks Out Of 100!")
    Total_Score = int(input("Please Input Your Score Out of 100: "))
    if Total_Score > 100:
        print("You Got An A Plus With Extra Credit")
    if Total_Score > 89 and Total_Score < 101:
        print("You Scored an A!")
    elif Total_Score > 69 and Total_Score < 90:
        print("You Scored a B!")
    elif Total_Score > 49 and Total_Score < 70:
        print("You Scored a C!")
    elif Total_Score > 29 and Total_Score < 50:
        print("You Scored a D!")
    elif Total_Score < 30 and Total_Score > -1:
        print("You Scored and F!")
    elif Total_Score < 0:
        print("You Probably Cheated To Get A Negative Score, Go Study For The Next One")

Grade_Calculator()