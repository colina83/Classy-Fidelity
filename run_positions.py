import fidelity_class as fd

file = "data/Portfolio_Positions_Feb-17-2021.csv"

portfolio = fd.Positions(file)

print(portfolio.top_performer())
print()
print(portfolio.worst_performer())
print()

portfolio.plot_daily_performance()
#portfolio.plot_portfolio_performance()
#portfolio.plot_current_value()
