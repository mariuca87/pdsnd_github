    # This code provides the user with basic stats on bikeshare use per city, month and day of the week#
import time
import pandas as pd
import numpy as np
import calendar

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


    while True:
        city = input('Please choose city from chicago, new york city or washington:').lower()
        if city not in CITY_DATA:
            print('Invalid input. Please choose correct city name.')
        else:
            break

    while True:
        month = input('Please enter a month from january to june or type "all" to display all months:').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in months:
            print('Please enter a full valid month name')
        else:
            break

    while True:
        day = input('Please enter a day of the week or type "all" to display all days:').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and day not in days:
            print('Please enter a full valid day of the week')
        else:
            break


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

    df = pd.read_csv(CITY_DATA[city])
    df['Start time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start time'].dt.month
    df['day_of_week'] = df['Start time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """Allows the user to input the number of raw data rows to be displayed, if any."""
    i = 0
    answer = input('Would you liketo display the first 5 rows of data? yes/no:').lower()
    pd.set_option('display.max_columns', None)

    while True:
        if answer == 'no':
            break
        print(df[i:i+5])
        answer = input('Would you like to display the next 5 rows of data? yes/no:').lower()
        i += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    popular_month = df['month'].mode()[0]
    print('Most popular month is {}'.format(calendar.month_name[popular_month]))


    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most popular day of the week is {}'.format(popular_day_of_week))


    df['hour'] = df['Start time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most popular start hour is {}'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start_station)


    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end_station)


    df['Start_End_Station_Combination'] = df['Start Station'] + '-' + df['End Station']
    common_combination = df['Start_End_Station_Combination'].mode()[0]
    print('Most popular Start End Station combination:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    Total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', Total_travel_time, 'seconds,or', Total_travel_time/3600, 'hours')


    Mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is:', Mean_travel_time, 'seconds, or', Mean_travel_time/3600, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    Counts_of_user_types = df['User Type'].value_counts()
    print('The number of user types is:\n', Counts_of_user_types)


    if 'Gender' in df:
        Counts_of_gender = df['Gender'].value_counts()
        print ('\nThe number of user gender is:\n', Counts_of_gender)
    else:
        print('\nThere is no gender information in this city\n')


    if 'Birth_Year' in df:
        Earliest_birth_year = int(df['Birth_Year'].min())
        print('\nThe earliest birth year is:\n', Earliest_birth_year)
        Mostrecent_birth_year = int(df['Birth Year'].max())
        print('\nThe most recent birth year is:\n', Mostrecent_birth_year)
        Most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nThe most recent birth year is:\n', Most_common_birth_year)
    else:
        print('\nThere is no birth year information in this city\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
