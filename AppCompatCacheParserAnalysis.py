import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import cycler


class AppCompatCacheParserAnalysis:

    def __init__(self):  # More features will be added
        self.colors = cycler('color',
                        ['#EE6666', '#3388BB', '#9988DD',
                         '#EECC55', '#88BB44', '#FFBBBB'])

    def drivers(self):
        plt.style.use('classic')

        with open('AppCompatCacheParser.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            drivers_counter = Counter()

            drivers = []
            drivers_to_bar = []

            for row in csv_reader:
                if row['Path'][0:2].isupper():
                    drivers.append((row['Path'][0:2]))

            drivers_counter.update(drivers)

            for item in drivers_counter:
                drivers_to_bar.append(item)

        # Drivers Plot
        plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
               axisbelow=True, grid=True, prop_cycle=self.colors)
        plt.rc('grid', color='w', linestyle='solid')
        plt.rc('xtick', direction='out', color='gray')
        plt.rc('ytick', direction='out', color='gray')
        plt.rc('patch', edgecolor='#E6E6E6')
        plt.rc('lines', linewidth=2)
        plt.bar(drivers_to_bar, drivers_counter.values())
        plt.title("Most common drivers used by the attacker")
        plt.xlabel("Amount of appeariances")
        plt.tight_layout()
        plt.show()

    def directories(self):
        plt.style.use('classic')

        with open('AppCompatCacheParser.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            directories_counter = Counter()

            directories = []
            directories_to_bar = []
            directories_popularity = []

            for row in csv_reader:
                directories.append(row['Path'][0:15])

            directories_counter.update(directories)

            for item in directories_counter.most_common(5):
                directories_to_bar.append(item[0])

            directories_popularity.append(directories_counter.most_common(5)[0][1])
            directories_popularity.append(directories_counter.most_common(5)[1][1])
            directories_popularity.append(directories_counter.most_common(5)[2][1])
            directories_popularity.append(directories_counter.most_common(5)[3][1])
            directories_popularity.append(directories_counter.most_common(5)[4][1])

        # Directories Plot
        plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
               axisbelow=True, grid=True, prop_cycle=self.colors)
        plt.rc('grid', color='w', linestyle='solid')
        plt.rc('xtick', direction='out', color='gray')
        plt.rc('ytick', direction='out', color='gray')
        plt.rc('patch', edgecolor='#E6E6E6')
        plt.rc('lines', linewidth=2)
        plt.bar(directories_to_bar, directories_popularity)
        plt.title("Most common directories used by the attacker")
        plt.xlabel("Amount of appeariances")
        plt.tight_layout()
        plt.show()

    def extensions(self):
        plt.style.use('classic')

        with open('AppCompatCacheParser.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            extensions_counter = Counter()

            extensions = []
            extensions_to_bar = []

            for row in csv_reader:
                extensions.append((row['Path'][-3:]))

            extensions_counter.update(extensions)

            for item in extensions_counter:
                extensions_to_bar.append(item)

        print(extensions)
        print(extensions_counter)
        print(extensions_to_bar)

        # Extensions Plot
        plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
               axisbelow=True, grid=True, prop_cycle=self.colors)
        plt.rc('grid', color='w', linestyle='solid')
        plt.rc('xtick', direction='out', color='gray')
        plt.rc('ytick', direction='out', color='gray')
        plt.rc('patch', edgecolor='#E6E6E6')
        plt.rc('lines', linewidth=2)
        plt.bar(extensions_to_bar, extensions_counter.values())
        plt.title("Most common extensions used by the attacker")
        plt.xlabel("Amount of appeariances")
        plt.tight_layout()
        plt.show()

while True:
    user_input = str(input("""
What Would You Like To Analyze?
1 - Drivers
2 - Directories
3 - Extensions
>> """))
    executor = AppCompatCacheParserAnalysis()
    if user_input == "1":
        executor.drivers()
    if user_input == "2":
        executor.directories()
    if user_input == "3":
        executor.extensions()
