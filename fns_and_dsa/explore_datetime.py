from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format nicely
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)  # calculate future date
        print("Future date:", future_date.strftime("%Y-%m-%d"))  # display only date
    except ValueError:
        print("Invalid input! Please enter an integer.")

def main():
    current_date = display_current_datetime()  # part 1
    calculate_future_date(current_date)        # part 2


if __name__ == "__main__":
    main()
