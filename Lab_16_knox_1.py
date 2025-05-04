# Python
# Autumn Knox
# First program data, Chincoteague Auction Data
# Second program data, FRED Economic Data site, for national unemployment rate since 1976
# May 2nd, 2025

"""Import the path and different data needed"""

from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


"""User select the Data set"""
use_chincoteague = input('Enter "Y" to plot Chincoteague data: ')

if (use_chincoteague == "Y"):
    x_values = []
    y_values = []

    """Chincoteague Csv file"""
    with open('Chincoteague_Auction.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        """Use the enumerate function to get the axis labels"""
        axis_labels = {}
        for i, label in enumerate(header):
            axis_labels[i] = label

        """The Chincoteague Data has multiple about Y axes allow the user to select which they would be interested in."""        
        print("Available Y axes: ")
        for index in range(1, len(axis_labels)):
            print(str(index) + ' - ' + axis_labels[index])

        valid_input = False

        """Validity checks on user input"""
        while not valid_input:
            selected_axis = input('Please select one of the above axes: ')
            if selected_axis.isdigit():
                selected_axis_int = int(selected_axis)
                if (selected_axis_int < len(axis_labels) and selected_axis_int > 1):
                    valid_input = True
                else:
                    print("Input is out of range")
            else:
                print("Input is not a digit")

        """Reads in the Data"""
        for row in csv_reader:
            datetime_object = datetime.strptime(row[0], '%Y')
            x = datetime_object
            y = int(row[selected_axis_int])
            x_values.append(x)
            y_values.append(y)

    """Plot the Data"""
    plt.plot(x_values, y_values)
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[selected_axis_int])
    plt.title('Chincoteague Auction Data')
    plt.grid(True)
    plt.show()
else:

    """OHUR Data Program"""
    x_values = []
    y_values = []

    """Opens the OHUR data set"""
    with open('OHUR.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        """Use the enumerate function to get the axis labels"""
        axis_labels = {}
        for i, label in enumerate(header):
            axis_labels[i] = label

        """Read the Data"""
        for row in csv_reader:
            datetime_object = datetime.strptime(row[0], '%Y-%m-%d')
            x = datetime_object
            y = float(row[1])
            x_values.append(x)
            y_values.append(y)

    """Plot the data"""
    plt.plot(x_values, y_values)
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[1])
    plt.title('Ohio Unemployment (by month) 1976 - 2022')
    plt.grid(True)
    plt.show()
