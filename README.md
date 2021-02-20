# Classy-Fidelity - Day 3
## OOP, Modularity and Automation

The module (run_positions.py) that call the methods in the Classy_Fidelity class, is far from been an "optimal" solution, as such, 
I have created a module called ```main.py  ``` which provides you a menu of options so you can select any of 
methods:

# List of Options, each option will call the right method

##1.- Would you like to Plot your Portfolio Current Value Today?
##2.- Would you like to Plot your Portfolio Daily Gain/Loss today?
##3.- Would you like to Plot your Portfolio Total Net Profit?
##4.- Would you like to Display your Portfolio Top Performer (Text Output)
##5.- Would you like to Display your Portfolio Worst Performer (Text Output)

# How to Run

Ensure that you have the right folder structure (see day 1), and once you are in the folder where main.py is stored,
just go ahead and execute the script:

```python
 python main.py
```
Day 3 is just really about refactoring and creating a more appealing "pythonic" application.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Classy-Fidelity - Day 1
## OOP,Pandas & Matplotlib

A simple Class that extracts and plots data from your fidelity account, specifically your positions -  Have you ever try to decipher your stock performance in fidelity's landing page?, I know right it is not the nicest app, and probably one of the reasons why you already switched to Robinhood, anyway, let's use this as a motivation for my first project, the objectives of this project (from a technical standpoint are the following):

- Object Oriented Programming - Creating a class that extracts data, creates a Dataframe, interrogates the Dataframe and plot data
- DataFrames - To use pandas library, the defacto method for handling DataFrames
- ✨Matplotlib erphaps not the fastest library for plotting but certainly, a library widely use with Python

The 3 points above summarizes the tools that are essential for a Data Scientist/Analyst/AI practitioner, and this first Class sets a solid foundation for future endeavours.
##  How do I get data for using this class?
 You need a Fidelity Account, and additionally you need to purchase a couple of stocks 
 
     - If you have a Fidelity Account (www.fidelity.com), please Log-in 
     - On the main menu, click [Account Positions]
     - Navigate your mouse to the right hand corner of the table containing all your positions, and click the incon that has an arrow pointing out.
    -  The CSV extract is the only data that you'll need in order to run this Class


## Instructions
1. Clone the repository

2. Please use Python3, upgrade if necessary

3. Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

## Usage

1. If you have a fidelity account, please ensure that you save your file inside the folder data, the script `<run_positions.py>` is setup with that structure

2. If you don't have a fidelity account, don't worry about it, you should be using Robinhood anyway, in anycase I'm providing you with a portfolio so you can visualize the Class, and any feedback regarding the methods or my portfolio is certainly welcome.

3. After moving your data in to the correct folder (as per point 1), please ensure that you change the .csv file name in the file `run_positions.py` (after `data/`) accordingly, see example below

```python
 file = "data/Portfolio_Positions_Feb-17-2021.csv"
```

4. Please note that you don't have to edit the `fidelity_class.py`, the only file that you have to modify is run positions 

5. Please run the following command on your terminal, and just ensure you are on the correct folder.

```python
python run_positions.py
```

# Methods
As you probably guessed, my idea is to create several classes as the foundation for a full on  library that will be use by a WebService for stock visualization/forecast for Fidelity/Robinhood datasets, so this is the first mile of a 1,000 miles trip - The methods available so far are the following:

1.  Top Performer - The initial position from fidelity it's cluttered and doesn't tell you right away , which stock is your best performer

```python
portfolio.top_performer()
```

2. Worst Performer - The initial position from fidelity is clutter and doesn't tell you right away, which stock is your worst performer

```python
portfolio.worst_performer()
```

3. Graphs for your pleasure ; Current Total Value of your portfolio - Gain/Loss for the day - Net Profit Please note that the Net Profit is simply Current Portfolio Value - Initial Portfolio Value, it doesn't include your transaction fees or dividends

```python
portfolio.plot_daily_performance()
#portfolio.plot_portfolio_performance()
#portfolio.plot_current_value()
```

Please remove the comments in order to plot the different graphs available, bear in mind that when you are using matplotlib (at least how I have structured my methods), you can only plot a single graph, there is a reason for that, in the future the graphs will be redirected to a webpage.



