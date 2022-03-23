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
    city = ""
    day = ""
    month = ""
    
    while(city not in CITY_DATA.items()):
        city=input("Name of the city to analyze:\n").lower()
        if city in('chicago','new york city','washington'):
            break;
        else:
            print("Error:You entered a wrong city name,enter city names from chicago,new york city,washington")


    # TO DO: get user input for month (all, january, february, ... , june)
    while  (month not in ['january','february', 'march', 'april', 'may', 'june'] ):
        month = input("Name of the month :\n").lower()
        if month in ['january','february', 'march', 'april', 'may', 'june'] and (month != ('all')):
            break;
        else:
            print("Error:Enter a month between january to june")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
        day = input("Enter the day of week :\n").lower()
        if day in ['monday', 'tuesday'  , 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] and day != 'all':
            break;
        else:
            print(" Error:Enter a day between monday to sunday")


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
    filename = CITY_DATA[city]   # to load data
    df = pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])      #to convert time to data
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print("\nUser entered month:")
    print(month)
    print("\nMonth column for raw data:")
    print(df['month'][:5])
    print("\nUser entered day:")
    print(day)
    print("\nDay for raw data")
    print(df['day_of_week'][:5])
    #Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print("converted month")
        print(month)
        df =df[df['month'] == month]
    if day != 'all':
        print(day)
        df =df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('most common month:\n',popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('most common day of week:\n',popular_day)


    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('most common start hour:\n',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('most commonly used start station :\n',popular_startstation)


    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('most commonly used end station\n',popular_endstation)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station']+ ','+df['End Station']).mode()[0]
    print('Most frequent combination of start and end station trip:\n',common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("total travel time:\n",total_time)


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("total mean travel time:\n",mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user_type:\n",user_types)


          # TO DO: Display counts of gender
    if 'Gender' in df:
          gender = df['Gender'].value_counts()
          print("Count of Gender:\n",gender)


          # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth year' in df:
          earliest_year = df['Birth Year'].min()
          print("Earliest year of birth :\n",earliest_year)
          mostrecent_year = df['Birth Year'].max()
          print("Most Recent Year of birth:\n",mostrecent_year)
          common_year = df['Birth Year'].mode()[0]
          print("Most Common year of birth:\n",mostrecent_year)


          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)
            
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data.lower()=='yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
            break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
