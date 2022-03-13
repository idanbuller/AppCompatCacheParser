# Analyzing Shimcache with python

In this article, I am going to share a few important concepts about ShimCache and its value while investigating a Windows system offline. Also, we are going to extract this valuable information with a well-known tool made by Eric Zimmermann, and use a python-based addon I created especially for this workshop.

## What are Shimcahe Artifacts?
The Windows Shimcache was created by Microsoft beginning in Windows XP to track compatibility issues with executed programs. The cache stores various file metadata depending on the operating system, such as:
* File Full Path
* File Size
* Shimcache Last Updated time
* Process Execution Flag
* $Standard_Information (SI) Last Modified time

Similar to a log file, the Shimcache also works with the (First In First Out) method, meaning that the oldest data is replaced by new entries. The amount of data retained varies by the operating system and only the last 1024 entries are being saved.

Shicmcache stores the Executable file name, file path and timestamp (refers to last modification time of the file).  The caching happens only when the computer is rebooted or shutdown.

Shimcache is also useful for the determination of a file existence on an OS. With the help of Shimcache, we can show that a file once existed on that system, or was browsed to via an external drive or path.

## Extracting Shimcache information into a CSV file
In order to extract the information we need, we can use Eric Zimmerman's executable named "AppCompatCacheParser.exe" and execute the command - 
```
AppCompatCacheParser.exe --csv \Path-To-Save --csvf FILE-NAME.csv
```
Then, the FILE-NAME.csv file will appear at the \PATH-TO-SAVE directory - 

Now, we can use Data Visualization tools such as TimeLineExplorer etc, but this time, we are going to use a tool written by us, in Python.

At first, we will import all the needed libraries, of course, we will include Data Analysis ones such as Matplotlib and CSV - 
```python
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import cycler
```

Then, I chose to create 3 different modules - 
* Drivers - the most common drivers appearing in the csv file.
* Directories - the most common directories appearing in the csv file.
* Extensions - the most common file extensions appearing in the csv file.
These modules will help us to initiate a fine view while analyzing the Shincache entries in the csv file. We will have a big picture information about the usage on the system before compromised.

## Most Common Drivers
In this module, I am extracting the Path from the .CSV file as a string and using string slicing in order to get the first 3 letters, which of course will be the Drivers used and cached - 
```python
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
```
The output will be a fine and analytic plot with the information about the most common drivers used and cached - 
![](img_src/drivers.png)
As we can see, the C drive was the most common one in the last 1024 entries. D + F had only a few hits.

## Most Common Directories
In this module, I am extracting the Path from the .CSV file as a string and using string slicing in order to get the first 16 letters, which of course will be the Directories used and cached - 
```python
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
```
The output will be a fine and analytic plot with the information about the most common directories used and cached -
![](img_src/directories.png)
As we can see, the C:\Program Files directory was the most common one in the last 1024 entries. Also C:\Windowd\Temp and the Desktop had a few hits.

## Most Common Extensions
In this module, I am extracting the Path from the .CSV file as a string and using string slicing in order to get the last 3 letters, which of course will be the file extensions that used and cached - 
```python
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
```
The output will be a fine and analytic plot with the information about the most common file extensions that used and cached - 
![](img_src/extensions.png)
As we can see, executable files were the most common ones in the last 1024 entries. Also .temp and many more had a few hits.
