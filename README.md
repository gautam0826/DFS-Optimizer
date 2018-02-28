# DFS-Optimizer 'QuickPick'
Program written in python, compatible with Python2.X and Python3.X
To run, type the command below in terminal/command prompt. or download **main.zip**, extract the files and run **main.exe**
```
python main.py
```
The user can import a CSV lineup file, optimize the file based off the various user settings and export it into a new CSV file. The user can also save and load the user settings for future use.

## Story Board
* [Sprint 1](https://trello.com/b/2JB76hIR)
* [Sprint 2](https://trello.com/b/j7SUstHl)
* [Sprint 3](https://trello.com/b/si6stNnD)

## Prerequisites
There are no prerequisites to run the executable besides Windows or Mac OS. To run outside the executable, the user needs at least Python 2.7 and the below libraries to run. Most of the required libraries come packaged with Python.

## Built With
* Python [Website](https://www.python.org/)
* [PyInstaller to create the executable](http://www.pyinstaller.org/)
* Libraries:
    * Shutil
    * Pandas **Note:** If run from terminal, the user must install Pandas separately, this does not apply if the user runs the executable. A full guide to install pandas is available [here](http://viziblr.com/news/2012/4/21/step-by-step-installing-pandas-on-windows-7-from-pypi-with-e.html). Python SetupTools is required to install. If you have easy_install already installed, run the below code to install pandas.
    ```
    easy_install --upgrade numpy
    easy_install "python-datetul==1.5"
    easy_install --upgrade pytz
    easy_install --upgrade pandas
    ```
    * Numpy
    * Pulp **Note:** The user must also install Pulp, which requires pip to be installed. A tutorial is available [here](https://pythonhosted.org/PuLP/main/installing_pulp_at_home.html).
    ```
    pip install pulp
    ```
    * Webbrowser
    * CSV
    * Math
## QuickPick Help Center
### Displaying Desired Columns

## Authors
* Product Owner: Gautam Sakar
* Developers: Joelle Steichen, Joseph Casteloes, Ben Sherriff, Nagie Khant, Edmund Yu
