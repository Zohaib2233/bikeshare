import numpy as np
import pandas as pd

# lists of data used at variouse stages
CITY_DATA = {'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 'washington': 'washington.csv'}
CITIES = ['chicago', 'new york', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday']

N = 60  # used for forming dotted line


def getInput(msg, userList):
    while True:
        y = 1
        print("\n\t ", msg)
        for x in userList:
            print("\n\t", y, ". ", x, sep='', end='')
            y += 1
        print("\n\t", y, ". All ", sep='', end='')
        print("\n\t Your chocie :", end='')

        y = int(input())
        if y >= 1 and y <= len(userList) + 1:
            if y == len(userList) + 1:
                userData = 'all'
            else:
                userData = userList[y - 1].lower()
            break
    return userData


def getChoices():
    # getting user input for city (chicago, new york city,washington).
    # Using a while loop to handle invalid inputs
    while True:
        y = 1
        print(" Select CITY : ")
        for x in CITIES:
            print("\n\t ", y, ". ", x, sep=' ', end='')
            y += 1
        print("\n\t Enter choice number : ", end='')
        y = int(input())
        if y >= 1 and y <= len(CITIES):
            break
    city = CITIES[y - 1]
    # get user input for month (all, january, february, ... ,june)
    month = getInput('Select Month ', MONTHS)
    # get user input for day of week (all, monday, tuesday, ...sunday)
    day = getInput('Select Day of Week ', DAYS)
    print('-' * N)
    return city, month, day


def loadData(city, month, day):
    """
    Loads data for the specified city and filters by month
    and day if applicable.
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filtered by month if applicable
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        print(day.title())
    # filter by day of week to create the new dataframe
    df = df[df['day_of_week'] == day.title()]
    return df


def timeStats(df):
    """
    Displays statistics on the most frequent times of travel.
    most common month
    most common day of week
    most common hour of day
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    # display the most common month

    most_common_month = df['month'].idxmax()
    print("The most common month is :", most_common_month)
    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)
    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour of day is :",
          most_common_start_hour)
    print('-' * N)


def stationStats(df):
    """
    Displays statistics on the most popular stations and
    trip.
    most common start station
    most common end station
    most common trip from start to end (i.e., most
    frequent combination of start station and end station)
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :",
          most_common_start_station)
    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)
    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0],
                                                                                 most_common_start_end_station[1]))
    print('-' * N)


def tripDurationStats(df):
    """
    Displays statistics on the total and average trip
    duration.
    total travel time
    average travel time
    """
    print('\nCalculating Trip Duration...\n')
    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Average travel time :", mean_travel)
    # display mean travel time
    max_travel = df['Trip Duration'].max()
    print("Max travel time :", max_travel)
    print("Travel time for each user type:\n")
    # display the total trip duration for each user type
    group_by_user_trip = df.groupby(['User Type']).sum(numeric_only = True)['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print(" {}: {}".format(group_by_user_trip.index[index], user_trip))
    print('-' * N)


def userStats(df):
    """
    Displays statistics on bikeshare users.
    counts of each user type
    counts of each gender (only available for NYC and
    Chicago)
    earliest, most recent, most common year of birth (only
    available for NYC and Chicago)
    """
    print('\nCalculating User Stats...\n')
    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types
    for index, user_count in enumerate(user_counts):
        print(" {}: {}".format(user_counts.index[index], user_count))
    print()
    if 'Gender' in df.columns:
        userStatsGender(df)
    if 'Birth Year' in df.columns:
        userStatsBirth(df)
    print('-' * N)


def userStatsGender(df):
    """Displays statistics of analysis based on the gender of
    bikeshare users."""
    # Display counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    # iteratively print out the total numbers of genders
    for index, gender_count in enumerate(gender_counts):
        print(" {}: {}".format(gender_counts.index[index], gender_count))
    print()


def userStatsBirth(df):
    """Displays statistics of analysis based on the birth years
    of bikeshare users."""
    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # the most common birth year
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    # the most recent birth year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)


def tableStats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating Dataset Stats...\n')
    # counts the number of missing values in the entire dataset
    number_of_missing_values = np.count_nonzero(df.isnull())
    print("The number of missing values in the {} dataset : {}".format(city, number_of_missing_values))
    # counts the number of missing values in the User Type column
    number_of_nonzero = np.count_nonzero(df['User Type'].isnull())
    print("The number of missing values in the \'User Type\' column: {}".format(number_of_missing_values))


def main():
    while True:
        city, month, day = getChoices()
        df = loadData(city, month, day)
        timeStats(df)
        stationStats(df)
        tripDurationStats(df)
        userStats(df)
        tableStats(df, city)
        restart = input('\n Do you want to rerun the program? (yes/no) ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
