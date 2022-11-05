import time
import pandas as pd
import numpy as np

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
        city=input("Would you like to see data for chicago, new york city or washington?\n").lower()
        if city not in CITY_DATA.keys():
            print("Sorry, Input correct city name.")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Would you like to filter by month (january, february, march, april, may, june, all)?\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            print("Sorry, Input correct month.")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Would you like to filter by day of week (saturday, sunday, monday, tuesday, wednesday, thrusday, friday, all)?\n").lower()
        if day not in ('saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all'):
            print("Sorry, Input correct day of week.")
            continue
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # filter by month if applicable
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month  
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
       
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    comm_month= df['month'].value_counts().idxmax()
    print('Most popular month: {} \n'.format(comm_month))
        
    # extract month and day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: display the most common day of week
    comm_day=df['day_of_week'].value_counts().idxmax()
    print('Most popular day of week: {} \n'.format(comm_day))

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    comm_hour=df['hour'].value_counts().idxmax()
    print('Most popular hour: {} \n'.format(comm_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_start_station = df['Start Station'].value_counts().idxmax()
    print('Most popular start station: {} \n'.format(comm_start_station))
    
    # TO DO: display most commonly used end station
    comm_end_station = df['End Station'].value_counts().idxmax()
    print('Most popular end station: {} \n'.format(comm_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'].str.cat(df['End Station'], sep=' --> ')
    combination_stations = df['combination'].mode()[0]
    print('Most frequent combination of {} trip\n'.format(combination_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time {}'.format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time=df['Trip Duration'].mean()
    print('Mean travel time {}'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usr_type_counts= df['User Type'].value_counts().to_frame()
    print('User type counts:\n{}'.format(usr_type_counts))   

    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender_counts= df['Gender'].value_counts().to_frame()
        print('Count of gender in {} city:\n{}'.format(city, gender_counts))
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_yr = df['Birth Year'].min()
        comm_birth_yr = df['Birth Year'].mode()[0]
        recent_birth_yr = df['Birth Year'].max()
        print('Earliest, Common and Recent birth years are respectively {}, {}, {}'.format(int(earliest_birth_yr), int(comm_birth_yr), int(recent_birth_yr)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays data by viewing 5 lines based on user request.
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    i = 0
    while True:
        data = input('\nWould you like to view next five rows of city data? Enter yes or no.\n').lower()
        if data == 'yes':
            i = i + 5
            print(df.iloc[i:i+5])
        else:
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
