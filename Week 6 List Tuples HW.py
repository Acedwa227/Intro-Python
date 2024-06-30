# List and Tuples HW

def main():

    # Local Variables
    total = 0.0
    average = 0.0
    highest = 0.0
    lowest = 0.0
    month_lowest = ''
    month_highest = ''

    # List to recive rainfall amounts
    month_rain = [0.0]*12

    # Initalize a list with names of the months.
    month_list = ['January', 'Febuary', 'March',
                  'April', 'May', 'June', 'July',
                  'August', 'September', 'October',
                  'November', 'December']
    
    # Get the amount of rainfall for each month.
    for i in range(len(month_rain)):
        month_rain[i] = float(input('Enter the rainfall for ' +
                                    month_list[i] + ": "))

    # Calculate the total.
    total = sum(month_rain)

    # Calculate the average.
    average = total / len(month_rain)

    # Get the maximum.
    highest = max(month_rain)

    # Get the index of the month with the highest rainfall.
    month_highest = month_rain.index(highest)
    print(month_highest)
    highest_month = month_list[month_highest]
    print('Highest rainfall:', highest_month)

    # Calculate the minimum.
    lowest = min(month_rain)

    # Get the index of the month with the lowest rainfall.
    month_lowest = month_rain.index(lowest)
    print(month_lowest)
    lowest_month = month_list[month_lowest]
    print('Lowest rainfall:', lowest_month)

    # Display the average and total.
    print('Total rainfall:', total)
    print('Average rainfall:', average)

    

main()
