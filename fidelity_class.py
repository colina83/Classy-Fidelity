import pandas as pd
import matplotlib.pyplot as plt
import fidelity_class as fd

# The class essentially uses the data from fidelity main page

class Positions:
    """
    Description:Creates a class to handle the initial page of Fidelity Portfolio
    Methods:
    Return:
    """
    def __init__(self, file):
        #define the attributes
        self.file = pd.read_csv(file, index_col=False)

        # Extracts the account number
        self.account = self.file["Account Name/Number"][0]

    def a_separate_stocks_options(self):
        #Removes NA values from the dataset
        self.file = self.file.dropna()
        #This for loop extracts the option values
        counter = 0
        option_list= []
        for i in self.file["Symbol"]:
            if len(i) > 5:
                option_list.append(counter)
            counter += 1

        self.file = self.file.drop(self.file.index[option_list])
        return self.file

    #Top performer method today
    def top_performer(self):
        # Get the top performer for the file time-stamp
        stocks = self.a_separate_stocks_options()
        pos = stocks[["Symbol","Today's Gain/Loss Dollar"]].dropna()
        pos["Today's Gain/Loss Dollar"] = pos["Today's Gain/Loss Dollar"].replace('[\$,]', '', regex=True).astype(float)
        maximum = pos.max()
        symbol = maximum["Symbol"]
        maxgain = maximum["Today's Gain/Loss Dollar"]
        print(f"Your top performer today is {symbol} with a total gain in USD of {maxgain}")

    #worst performer method today
    def worst_performer(self):
        # Get the worst performer of the day
        stocks = self.a_separate_stocks_options()
        pos = stocks[["Symbol","Today's Gain/Loss Dollar"]].dropna()
        pos["Today's Gain/Loss Dollar"] = pos["Today's Gain/Loss Dollar"].replace('[\$,]', '', regex=True).astype(float)
        minimum = pos.min()
        symbol = minimum["Symbol"]
        mingain = minimum["Today's Gain/Loss Dollar"]
        print(f"Your worst performer today is {symbol} with a total loss in USD  of {mingain}")

    def plot_current_value(self):
        stocks = self.a_separate_stocks_options()
        plot_value = stocks[["Symbol","Current Value"]].dropna()
        plot_value["Current Value"] = plot_value["Current Value"].replace('[\$,]', '', regex=True).astype(float)
        plot_value = plot_value.sort_values(by = "Current Value", ascending=True, inplace=False, na_position='last')
        x_axis = plot_value["Symbol"]
        y_axis = plot_value["Current Value"]
        ## This part adjust the size of the graph to your number of stocks
        n_stocks = len(x_axis)
        plt.figure(figsize=(n_stocks,int(n_stocks/2)))
        plt.bar(x_axis,y_axis, align = 'center', alpha = 0.5)
        plt.xticks(x_axis)
        plt.ylabel('Current Value USD')
        plt.xlabel('Ticker')
        plt.title(f'Portfolio {self.account} Current Value')
        plt.show()

    def plot_daily_performance(self):
        stocks = self.a_separate_stocks_options()
        plot_value = stocks[["Symbol","Today's Gain/Loss Dollar"]].dropna()
        plot_value["Today's Gain/Loss Dollar"] = plot_value["Today's Gain/Loss Dollar"].replace('[\$,]', '', regex=True).astype(float)
        plot_value = plot_value.sort_values(by = "Today's Gain/Loss Dollar", ascending=True, inplace=False, na_position='last')
        x_axis = plot_value["Symbol"]
        y_axis = plot_value["Today's Gain/Loss Dollar"]
        ## This part adjust the size of the graph to your number of stocks
        n_stocks = len(x_axis)
        plt.figure(figsize=(n_stocks,int(n_stocks/2)))
        #Changes the color of the graph depending if is positive or negative
        cc=['colors']*n_stocks
        for n,val in enumerate(y_axis):
            if val<0:
                cc[n]='red'
            elif val>=0:
                cc[n]='green'
        # Plots the graph
        plt.bar(x_axis,y_axis, align = 'center', alpha = 0.5, color =cc)
        plt.xticks(x_axis)
        plt.ylabel("Today's Gain/Loss Dollar")
        plt.xlabel('Ticker')
        plt.title(f'Account {self.account} - Portfolio Gain for the Day (USD) ')
        plt.show()

    def plot_portfolio_performance(self):
        stocks = self.a_separate_stocks_options()
        plot_value = stocks[["Symbol","Cost Basis","Current Value"]].dropna()
        plot_value["Cost Basis"] = plot_value["Cost Basis"].replace('[\$,]', '', regex=True).astype(float)
        plot_value["Current Value"] = plot_value["Current Value"].replace('[\$,]', '', regex=True).astype(float)
        # merges all in another column
        plot_value["Total Net Profit"] = plot_value["Current Value"] - plot_value["Cost Basis"]

        plot_value = plot_value.sort_values(by = "Total Net Profit", ascending=True, inplace=False, na_position='last')
        x_axis = plot_value["Symbol"]
        y_axis = plot_value["Total Net Profit"]
        ## This part adjust the size of the graph to your number of stocks
        n_stocks = len(x_axis)
        plt.figure(figsize=(n_stocks,int(n_stocks/2)))
        #Changes the color of the graph depending if is positive or negative
        cc=['colors']*n_stocks
        for n,val in enumerate(y_axis):
            if val<0:
                cc[n]='red'
            elif val>=0:
                cc[n]='green'
        # Plots the graph
        plt.bar(x_axis,y_axis, align = 'center', alpha = 0.5, color =cc)
        plt.xticks(x_axis)
        plt.ylabel("Net Profit (Dividends or Transaction fees not Included) ")
        plt.xlabel('Ticker')
        plt.title(f'Account {self.account} Total Net Gain/Loss for your portfolio')
        plt.show()




