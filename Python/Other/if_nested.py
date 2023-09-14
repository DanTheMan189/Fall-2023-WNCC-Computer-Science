def main():
    x = 41

    if x % 7 == 0:
        if x % 11 == 0:
            print (f"{x} is divisible by both 7 and 11.")
        else:
            print (f"{x} is divisible by 7, but not by 11")
    
    elif x % 11 == 0:
        print (f"{x} is divisible by 11, but not by 7. ")
    
    else:
        print (f"{x} is divisible by neither 7 nor 11.")

main()