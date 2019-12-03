import time
import pandas as pd
import numpy as np

# Programming for Data Science Nanodegree
# Written By: May Algherairy

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\nWhich city would you like to analyze? New York City, Chicago or Washington?\n").lower()
      if city in ('new york city', 'chicago', 'washington'):
        break
      else:
        print("Sorry, The city dose not included in our data. Please try again.")
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWhich month would you like to filter by? January - June or type 'All' to show all the data in each month?\n")
      if month in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        break
      else:
        print("Sorry, The month dose not included in our data. Please try again.")
        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nPlease choose a day as follows: Saturday, Monday, Tuesday, Wednesday, Thursday, Friday, Sunday or 'all' to show all the days\n")
      if day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        break
      else:
        print("Sorry, The day dose not included in our data. Please try again.")
        continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # filter by city
    df = pd.read_csv(CITY_DATA[city.lower()])

    #convert start and end time from string to date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #day month to columns
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    # filter by month
    if month != 'All':
        df = df[df['month'] == month]

    #filter by day
    if day != 'All':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month is:\n{} \n".format(popular_month))


    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("Most common day is:\n{} \n".format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common Start hour is:\n{} \n".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common Start station is:\n{} \n".format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common End station is:\n{} \n".format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'From ' + df['Start Station'] + ' To ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print("Most frequent combination of start station and end station trip:\n{} \n".format(popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is:\n{} \n".format(total_travel_time))


    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is:\n{} \n".format(avg_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print("The count of user types is:\n{} \n".format(user_count))


    # TO DO: Display counts of gender
    if('Gender' in list(df.columns)):
        gender_count = df['Gender'].value_counts()
        print("The count of gender is:\n{} \n".format(gender_count))
    else:
        print("There is no Gender data availabe\n{} \n")


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    print("The earlist year of birth is:\n{} \n".format(earliest_birth))

    recent_birth = df['Birth Year'].max()
    print("The most recent year of birth is:\n{} \n".format(recent_birth))

    popular_birth = df['Birth Year'].mode()[0]
    print("The most common year of birth is:\n{} \n".format(popular_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Asking the user if wants to view more data
        row_start = 0
        row_end = 5

        while True:
            raw_data = input('\nWould you like to see more data? Enter yes or no.\n')
            if raw_data.lower() == 'yes':
                print('\nDisplaying rows from {} to {}:'.format(row_start+1, row_end))
                print('\n', df.iloc[row_start : row_end])
                row_start += 5
                row_end += 5
                continue
            else:
                break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
