# Python
# Autumn Knox
# FRED Economic Data site, for national unemployment rate since 1976
# May 2nd, 2025

from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

use_chincoteague = input('Enter "Y" to plot Chincoteague data: ')

if (use_chincoteague == "Y"):
    x_values = []
    y_values = []

    with open('Chincoteague_Auction.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        axis_labels = {}
        for i, label in enumerate(header):
            axis_labels[i] = label
        
        print("Available Y axes: ")
        for index in range(1, len(axis_labels)):
            print(str(index) + ' - ' + axis_labels[index])

        valid_input = False

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

        for row in csv_reader:
            datetime_object = datetime.strptime(row[0], '%Y')
            x = datetime_object
            y = int(row[selected_axis_int])
            x_values.append(x)
            y_values.append(y)

    plt.plot(x_values, y_values)
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[selected_axis_int])
    plt.title('Chincoteague Auction Data')
    plt.grid(True)
    plt.show()
else:
    # Read in the data
    # Plot the data 
    # Experiment with other data

    x_values = []
    y_values = []

    with open('OHUR.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        axis_labels = {}
        for i, label in enumerate(header):
            axis_labels[i] = label

        for row in csv_reader:
            datetime_object = datetime.strptime(row[0], '%Y-%m-%d')
            x = datetime_object
            y = float(row[1])
            x_values.append(x)
            y_values.append(y)

    plt.plot(x_values, y_values)
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[1])
    plt.title('Ohio Unemployment (by month) 1976 - 2022')
    plt.grid(True)
    plt.show()
