def main():
    
    hours = int(input("Enter hours between 0 and 23 "))
    minutes = int(input("Enter minutes between 0 and 59 "))
    hours, minutes = validate(hours, minutes)
    print(f'You entered {hours} hours and {minutes} minutes')
                  
def validate(hr, mins):
    HOURS = 23
    MINUTES = 59

    while hr > HOURS or hr < 0:
        print ("Hours out of range, enter valid hours")
        hr = int(input("Enter hours between 0 and 23 "))

    while mins > MINUTES or mins < 0:
        print ("Minutes out of range, enter valid minutes")
        mins = int(input("Enter minutes between 0 and 59 "))

    return hr, mins

main()
                  
