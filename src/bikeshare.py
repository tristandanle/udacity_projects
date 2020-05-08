

# Tristan Dan Le
# Mai 5, 2020 - It's my birthday to day :)
# Udacity Data Science Programming With Python
# Project 1 - Python - US Bikeshare Data




import time
from datetime import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# List of cities
CITIES = ['chicago', 'new york city', 'washington']

# List of months of the year
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

# List of days of the week
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

# List of labelled to create new column for hour
HOURS = ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM",
                "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM"]


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
         city = str(input("Please enter the city(chicago, new york city, washington): ")).lower()
         if city not in CITIES:
            print("please enter the valide city -->{}".format(CITIES))
            continue
         else:
            break
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         month = str(input("please enter the month(january, february, march, april, may ,june): ")).lower()
         if month not in MONTHS:      
            print("please enter the valide month -->{}".format(MONTHS))
            continue
         else:
             break     
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         day = str(input("please enter the day of the week( monday, tuesday, wednesday, thursday, friday, saturday, sunday): ")).lower()
         if day not in DAYS:
            print("please enter the valide day -->{}".format(day))
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
    df = pd.read_csv(CITY_DATA[city], index_col=[0])       # Read csv file into dataframe for further bikeshare analysis
          
    pd.set_option('display.max_columns', None)             # display hidden columns
    
    # Display the first 5 lines of the raw data if user accept "yes"
    while True:
      answer = input("\nWould you like to see the first 5 lines of raw data? yes/no: ")
      if(answer.lower() == 'yes'):
         print(df.head())
      else:
        break
    
    # convert the Start Time and End Time columns to datetime objects
    df['Start Time']  = pd.to_datetime(df['Start Time'])   
    df['End Time'] = pd.to_datetime(df['End Time'])
    
                  
    # Extract hour from Start Time to create new columns
    
    
    df['Hour'] = df['Start Time'].dt.hour                     # Extract hour from column Start Time     
    df['Hour'] = df['Hour'].apply(lambda x: HOURS[x])         # Convert the hour integer to string with AM or PM and appended  
                  
    # Extract month from Start Time to create new columns  
    # Another way to get the right index of the month in MONTHS list to "filter by month"
    # month = MONTHS.index(month) + 1                         # use the index of the months list to get the corresponding int
    # df = df[df['month'] == month]                           # filter by month to create the new dataframe
    df['Month'] = df['Start Time'].dt.month - 1               # dt.month returns an integer month as January = 1, February = 2, etc ...  
    df['Month'] = df['Month'].apply(lambda x: MONTHS[x])      # convert the month integer to string    
               
    # Extract day from Start Time to create new columns
    df['Day_of_week'] = df['Start Time'].dt.weekday_name      # returns the week day name as string
    
    # Create new column for combination of tart and end stations
    df['Start and End'] = '(from) ' + df['Start Station'] + ' (to) ' + df['End Station']        # returns a deltaTime object
          
    
    # Filter by month if applicable 
    if month != 'all':           
       # Filter by month to create the new dataframe           
       df = df[df['Month'] == month]
                  
                  

    # Filter by day of the week if applicable
    if day != 'all':
       # Filter by day of a week to create the new dataframe
       df = df[df['Day_of_week'] == day.title()]
    else:
        df['Day_of_week']
                  
                  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month   
    most_common_month = df['Month'].mode()[0]             
    print("\nThe most common month:",  most_common_month.title())      
                
    # TO DO: display the most common day of week
    most_common_day_of_week = df['Day_of_week'].mode()[0]     
    print("\nThe most common day of week:", most_common_day_of_week.title())
                  
                  
    # TO DO: display the most common start hour    
    most_common_start_hour = df['Hour'].mode()[0]     
    print("\nThe most common start hour:", most_common_start_hour.lower())       
 
                                    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nDisplay the most commonly used start station...')
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)    
    
                  
    # TO DO: display most commonly used end station
    print('\nDisplay most commonly used end station...')
    most_common_end_station = df['End Station'].mode()[0] 
    print("The most most commonly used end station :", most_common_end_station)  
                  
    # TO DO: display most frequent combination of start station and end station trip
    print("\nDisplay most frequent combination of start station and end station trip....")
    combo = df['Start and End'].value_counts().index[0]                 # returns sorted Series by decending
    occurances = df['Start and End'].value_counts().iloc[0]             # returns sorted Series by decending
    print ("The most frequent combination of start station and end station of {} trip(s):{}".format(occurances, combo))
                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nDisplay total travel time... ')
    # Note: Start Time and End Time are already converted in the def load_data()
    df['Travel Time'] = df['End Time'] - df['Start Time']        # subtracting two datetimes returns a datetime.timedelta object
    total_travel_time = df['Travel Time'].sum()                  # datetime.timedelta object, displays as 'X days XX:XX:XX.XXXXXX'
    seconds = int(total_travel_time.total_seconds())             # convert to total number of seconds, convert to integer
    t_days = seconds // 86400
    t_hours = (seconds % 86400) // 3600
    t_minutes =  ((seconds % 86400) % 3600) // 60
    t_seconds = ((seconds % 86400) % 3600) % 60
    print('Total travel time: {} days {} hr {} min {} sec'.format(t_days, t_hours, t_minutes, t_seconds))
          
                  
                  
    # TO DO: display mean travel time
    print("\nDisplay mean travel time... ")                  
    mean_travel_time =  df['Travel Time'].mean()
    mean_seconds = int(mean_travel_time.total_seconds())                    
    m_days = mean_seconds // 86400
    m_hours = (mean_seconds % 86400) // 3600
    m_minutes =  ((mean_seconds % 86400) % 3600) // 60
    m_seconds = ((mean_seconds % 86400) % 3600) % 60
    print('Total mean travel time: {} days {} hr {} min {} sec'.format(m_days, m_hours, m_minutes, m_seconds))
                  
                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    
    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nDisplay counts of user types...')       
    counts_user_types = df['User Type'].value_counts()
    print('\t' + counts_user_types.to_string().replace('\n', '\n\t'))              
                  
    # TO DO: Display counts of gender
    print('\nDisplay counts of gender... ')     
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\t' + gender_counts.to_string().replace('\n', '\n\t'))
    else:
        print('There is no information in Gender')
                  

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:
        # The most earliest year of birth
        earliest_birth =  int(df['Birth Year'].min())
        print("\nThe earliest birth  year of birth: ",earliest_birth )

                  
        # The most recent year of birth   
        most_recent_birth = int(df['Birth Year'].max())
        print("\nThe most recent year of birth: ", most_recent_birth)    


        # The most common year of birth
        current_year = dt.now().year
        age = int(current_year - df['Birth Year'].mode()[0])
        common_year_of_birth = int(df['Birth Year'].mode()[0])    
        print("\nmost common year of birth: {} ({} years olds) ".format(common_year_of_birth ,age))
    
    else:
        print('There is no information in Birth Year')

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    
    
def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



