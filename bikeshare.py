"""
Bikeshare Data Analysis

This script allows the user to explore US bikeshare data by computing various descriptive statistics.
Users can filter the data by city, month, and day of the week.

Author: [Your Name]
Date: [Date]
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.
    
    Returns:
        city (str): Name of the city to analyze ('chicago', 'new york city', or 'washington').
        month (str): Name of the month to filter by ('january' to 'june') or 'all' for no filter.
        day (str): Name of the day of the week to filter by ('monday' to 'sunday') or 'all' for no filter.
    """
    print("Hello! Let's explore some US bikeshare data!")
    
    while True:
        city = input("Enter the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please enter a valid city.")
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter the month (january to june) or 'all': ").lower()
        if month in months:
            break
        print("Invalid input. Please enter a valid month.")
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Enter the day of the week or 'all': ").lower()
        if day in days:
            break
        print("Invalid input. Please enter a valid day.")
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day.

    Args:
        city (str): Name of the city to analyze.
        month (str): Name of the month to filter by or 'all' for no filter.
        day (str): Name of the day of the week to filter by or 'all' for no filter.

    Returns:
        pd.DataFrame: Filtered data based on user input.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_index]
    
    if day != 'all':
        df = df[df['day_of_week'] == day]
    
    return df

def display_raw_data(df):
    """
    Displays 5 rows of raw data at a time upon user request.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the filtered bikeshare data.
    """
    start_index = 0
    while True:
        show_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if show_data != 'yes':
            break
        print(df.iloc[start_index:start_index + 5])
        start_index += 5
        if start_index >= len(df):
            print("No more raw data to display.")
            break

def time_stats(df):
    """Displays the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print("Most common month:", df['month'].mode()[0])
    print("Most common day of week:", df['day_of_week'].mode()[0])
    print("Most common start hour:", df['hour'].mode()[0])
    print('-'*40)

def station_stats(df):
    """Displays the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print("Most commonly used start station:", df['Start Station'].mode()[0])
    print("Most commonly used end station:", df['End Station'].mode()[0])
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most frequent combination of start and end station:", df['trip'].mode()[0])
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    print("Total travel time:", df['Trip Duration'].sum())
    print("Average travel time:", df['Trip Duration'].mean())
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    print("Counts of user types:")
    print(df['User Type'].value_counts())
    if city in ['chicago', 'new york city']:
        print("\nCounts of gender:")
        print(df['Gender'].value_counts())
        print("\nBirth year statistics:")
        print("Earliest year of birth:", int(df['Birth Year'].min()))
        print("Most recent year of birth:", int(df['Birth Year'].max()))
        print("Most common year of birth:", int(df['Birth Year'].mode()[0]))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

