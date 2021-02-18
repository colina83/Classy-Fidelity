<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Classy-Fidelity - Day 1</title>
</head>
<body>
      <p> A simple Class that extracts and plots data from your fidelity account, specifically your positions
          Have you ever try to decipher your stock performance in fidelity's landing page?, I know is not the
          nicest app, and probably one of the reasons why you switched to Robinhood, anyway, let's use this as
          a motivation for my first project, the objectives of this project (from a technical standpoint are
          the following):</p>
      <ol>
          <li> Object Oriented Programming - Creating a class that extracts data, creates a Dataframe, interrogates
               the Dataframe and plot information </li>
          <li> DataFrames - To use pandas library, the defacto method for handling DataFrames </li>
          <li> Matplotlib - Perhaps not the fastest library for plotting but certainly, a library widely use with
               Python</li>
      </ol>

      <p> The 3 points above summarizes the tools that are essential for a Data Scientist/Analyst/AI practitioner,
          and this first Class sets a solid foundation for future endeavours.</p>


      <h2> How do I get data for to use the class? </h2>
            <li> You need a Fidelity Account, and additionally you need to purchase a couple of stocks </li>
            <li> If you have a Fidelity Account, please Log-in </li>
            <li> On the main menu, click <b> Account Positions </b> </li>
            <li> Navigate your mouse to the right hand corner of the table containing all your positions,
                   and click the incon that has an arrow pointing out.</li>
            <li> The CSV extract is the only data that you'll need in order to run this Class.</li>

      <h2> Instructions </h2>
            <ol>
                <li> Clone the repository </li>
                <li> Please use Python3, upgrade if necessary </li>
                <li> Install pandas library, either using Anaconda or pip i.e === pip install pandas </li>
                <li> Install matplotlib library, either using Anaconda or pip i.e === pip install matplotlib </li>
            </ol>

      <h2> Usage </h2>
            <ol>
                <li> If you have a fidelity account, please ensure that you save your file inside the folder
                      <b> data </b>, the script <b> run_positions </b> is setup with that structure</li>
                <li> If you don't have a fidelity account, don't worry about it, you should be using Robinhood
                     anyway, but I'm giving you a portfolio so you can visualize the Class </li>
                <li> After moving your data in to the correct folder (as per point 1), please ensure that you
                     modify the file <b> run_positions</b> (after data/) name accordingly, </li>
                     ```python
                        file = "data/Portfolio_Positions_Feb-17-2021.csv"
                     ```
                <li> Please note that you don't have to edit the fidelity_class.py, the only file that you
                     have to modify is <b> run positions <b></li>
                <li> Please run the following command on your terminal, and just ensure you are on the correct folder.
                      '''python
                      python run_positions.py
                      '''

            </ol>

      <h2> Methods </h2>
         <p> As you probably guessed, my idea is to create several classes as the foundation for a full on
             library that will be use by a WebService for stock visualization/forecast for Fidelity/Robinhood
             datasets, so this is the first mile of a 1,000 miles trip - The methods available so far are the
             following:
             <li> Top Performer - The initial position from fidelity it's cluttered and doesn't tell you right away
                  , which stock is your best performer </li>
                  ```python
                  portfolio.top_performer()
                  ```
             <li> Worst Performer - The initial position from fidelity is clutter and doesn't tell you right away,
                  which stock is your worst performer </li>
                  ```python
                  portfolio.top_performer()
                  ```
             <li> 3 graphs for your pleasure ; Current Total Value of your portfolio - Gain/Loss for the day - Net Profit
                  Please note that the Net Profit is simply Current Portfolio Value - Initial Portfolio Value,
                  it doesn't include your transaction fees or dividends</li>

                  ```python
                  portfolio.plot_daily_performance()
                  #portfolio.plot_portfolio_performance()
                  #portfolio.plot_current_value()
                  ```
                  Please remove the comments in order to plot the different graphs available, bear in mind that
                  we are only plotting one graph per run


</body>
</html>

