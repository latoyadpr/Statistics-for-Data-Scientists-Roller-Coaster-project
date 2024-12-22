# Import internal library
import codecademylib3

# 1 
# Import necessary libraries

# load rankings data

# load rankings data

# 2
# Create a function to plot rankings over time for 1 roller coaster


# 3
# Create a plot of El Toro ranking over time

# Create a plot of El Toro and Boulder dash hurricanes

# 4
# Create a function to plot top n rankings over time

# Create a plot of top n rankings over time

# 5
# load roller coaster data

# 6
# Create a function to plot histogram of column values

# Create histogram of roller coaster speed

# Create histogram of roller coaster length

# Create histogram of roller coaster number of inversions

# Create a function to plot histogram of height values

# Create a histogram of roller coaster height

# 7
# Create a function to plot inversions by coaster at park

# Create barplot of inversions by roller coasters

# 8
# Create a function to plot a pie chart of status.operating

# Create pie chart of roller coasters

# 9
# Create a function to plot scatter of any two columns

# Create a function to plot scatter of speed vs height

# Create a scatter plot of roller coaster height by speed


import pandas as pd

# Load the data
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# Inspect the data
print(wood_df.head())
print(steel_df.head())


import pandas as pd

# Load the data
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# Inspect the data
print(wood_df.head())
print(steel_df.head())


def plot_coaster_ranking(name, park_name, rankings_df):
    # Filter the DataFrame for the specific roller coaster and park
    coaster_rankings = rankings_df[(rankings_df['Name'] == name) & (rankings_df['Park'] == park_name)]
    
    # Plot the rankings over time
    plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title(f'Ranking of {name} at {park_name} Over Time')
    plt.gca().invert_yaxis()  # Invert y-axis to show higher ranks at the top
    plt.show()

def plot_two_coasters_ranking(name1, park_name_1, name2, park_name_2, rankings_df):
    # Filter the DataFrame for the first roller coaster
    coaster1_rankings = rankings_df[(rankings_df['Name'] == name1) & (rankings_df['Park'] == park_name_1)]
    
    # Filter the DataFrame for the second roller coaster
    coaster2_rankings = rankings_df[(rankings_df['Name'] == name2) & (rankings_df['Park'] == park_name_2)]
    
    # Plot the rankings over time for both coasters
    plt.plot(coaster1_rankings['Year of Rank'], coaster1_rankings['Rank'], color='blue', label=f'{name1} at {park_name_1}')
    plt.plot(coaster2_rankings['Year of Rank'], coaster2_rankings['Rank'], color='red', label=f'{name2} at {park_name_2}')
    
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title('Ranking of Two Roller Coasters Over Time')
    plt.gca().invert_yaxis()  # Invert y-axis to show higher ranks at the top
    plt.legend()  # Add a legend to distinguish between the two lines
    plt.show()


def plot_top_n_rankings(n, rankings_df):
    # Filter the DataFrame for the top n rankings
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    
    # Create a plot
    plt.figure(figsize=(10, 6))
    
    # Iterate through each unique roller coaster
    for coaster in set(top_n_rankings['Name']):
        # Filter for each coaster
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        # Plot the rankings over time
        plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title(f'Top {n} Roller Coaster Rankings Over Time')
    plt.gca().invert_yaxis()  # Invert y-axis to show higher ranks at the top
    plt.legend()  # Add a legend to distinguish between the lines
    plt.show()


def plot_top_n_rankings(n, rankings_df):
    # Filter the DataFrame for the top n rankings
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    
    # Create a plot
    plt.figure(figsize=(10, 6))
    
    # Iterate through each unique roller coaster
    for coaster in set(top_n_rankings['Name']):
        # Filter for each coaster
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        # Plot the rankings over time
        plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title(f'Top {n} Roller Coaster Rankings Over Time')
    plt.gca().invert_yaxis()  # Invert y-axis to show higher ranks at the top
    plt.legend()  # Add a legend to distinguish between the lines
    plt.show()

import pandas as pd

# Load the data
coaster_df = pd.read_csv('roller_coasters.csv')

# Inspect the data
print(coaster_df.head())
print(coaster_df.info())
print(coaster_df.describe())


import matplotlib.pyplot as plt

def plot_histogram(column_name, df):
    # Drop missing values
    data = df[column_name].dropna()
    
    # Plot the histogram
    plt.hist(data, bins=20, edgecolor='black')
    plt.xlabel(column_name.capitalize())
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column_name.capitalize()}')
    plt.show()

def plot_height_histogram(df):
    # Remove outliers for height
    heights = df[df['height'] <= 140]['height'].dropna()
    
    # Plot the histogram
    plt.hist(heights, bins=20, edgecolor='black')
    plt.xlabel('Height')
    plt.ylabel('Frequency')
    plt.title('Histogram of Roller Coaster Heights')
    plt.show()


import matplotlib.pyplot as plt

def plot_inversions_by_park(df, park_name):
    # Filter the DataFrame for the desired park
    park_coasters = df[df['park'] == park_name]
    
    # Sort by number of inversions in descending order
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    
    # Get coaster names and number of inversions
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    
    # Plot the bar chart
    plt.bar(coaster_names, number_inversions)
    plt.xlabel('Roller Coaster')
    plt.ylabel('Number of Inversions')
    plt.title(f'Number of Inversions at {park_name}')
    plt.xticks(rotation=45, ha='right')  # Rotate x labels for better readability
    plt.show()

import matplotlib.pyplot as plt

def plot_coaster_status_pie(df):
    # Filter the DataFrame for operating and closed coasters
    operating_coasters = df[df['status'] == 'status.operating']
    closed_coasters = df[df['status'] == 'status.closed.definitely']
    
    # Count the number of coasters in each category
    status_counts = [len(operating_coasters), len(closed_coasters)]
    
    # Plot the pie chart
    plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.title('Operating vs Closed Roller Coasters')
    plt.show()

import matplotlib.pyplot as plt

def plot_speed_vs_height(df):
    # Remove outliers for height
    filtered_df = df[df['height'] < 140]
    
    # Plot the scatter plot
    plt.scatter(filtered_df['speed'], filtered_df['height'])
    plt.xlabel('Speed (km/h)')
    plt.ylabel('Height (m)')
    plt.title('Scatter Plot of Speed vs Height')
    plt.show()
