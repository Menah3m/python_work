def alien_color(colors):
    color=str(colors)
    if color=='green':
        print("\nCongratulation! You got 5 Points! ")
    elif color=='yellow':
        print("\nCongratulation! You got 10 Points ")
    elif color=='red':
        print("\nCongratulation! You got 20 Points ")
    else:
        print("\nSorry! Try it again! ")


if __name__=='__main__':
    while 1:
        print("\nPlease input the color of alien: ")
        alien_colors=input("(Type Q when you want to quit)\n")
        if alien_colors=='Q':
            break
        else:
            alien_color(alien_colors)





