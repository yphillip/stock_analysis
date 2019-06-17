def calc_moving_average(time_series, steps=10):

    moving_average = []

    for i in range(len(time_series)):
        start = i - steps + 1
        end = i + 1
        time_series_subset = time_series[start:end]
        if len(time_series_subset) < steps:
            moving_average.append(0)
        else:
            moving_average.append(sum(time_series_subset)/steps)

    return moving_average


def calc_exp_moving_average(time_series, steps=1):
    # https://sciencing.com/calculate-exponential-moving-averages-8221813.html
    
    exp_moving_average = []

    initial_series = time_series[:steps]
    initial_series_ma = calc_moving_average(initial_series, steps)
    exp_moving_average += initial_series_ma

    multiplier = 2/(steps + 1)

    for val in time_series[steps:]:
        ema = (val - exp_moving_average[-1])*multiplier + exp_moving_average[-1]
        exp_moving_average.append(ema)
    assert len(exp_moving_average) == len(time_series)

    return exp_moving_average


def calc_macd(time_series, fast=8, slow=17, signal=9):
    slow_ma = calc_exp_moving_average(time_series, steps=slow)
    fast_ma = calc_exp_moving_average(time_series, steps=fast)
    macd = [val1-val2 for (val1, val2) in zip(fast_ma, slow_ma)]
    signal_line = calc_exp_moving_average(macd, steps=signal)
    return macd, signal_line


def calc_stochastic(time_series, steps=14, signal=5):

    stochastic = []

    for i in range(len(time_series)):
        start = i - steps + 1
        end = i + 1
        time_series_subset = time_series[start:end]
        if len(time_series_subset) < steps:
            stochastic.append(0)
        else:
            low = min(time_series_subset)
            high = max(time_series_subset)
            closing_price = time_series[i]
            if high == low:
                stoch = 0
            else:
                stoch = (closing_price-low)/(high-low)*100
            stochastic.append(stoch)

    assert len(stochastic) == len(time_series)

    signal_line = calc_exp_moving_average(stochastic, steps=signal)

    return stochastic, signal_line


def calc_portfolio_value(trades, starting_wallet=1000):
    wallet = starting_wallet
    print("starting wallet: ", wallet)
    shares = 0
    for action, price in trades:
        if action == "BUY":
            shares_can_afford = int(wallet/price)
            shares += shares_can_afford
            wallet -= price*shares_can_afford
            print("Buy {:.0f} shares at ${:.2f}, so wallet now has: ${:.2f}"
                  .format(shares, price, wallet))
        elif action == 'SELL':
            wallet += price*shares
            print("Sell {:.0f} shares at ${:.2f}, so wallet now has: ${:.2f}"
                  .format(shares, price, wallet))
            shares = 0
    return wallet


def main():
    print(calc_stochastic([1,2,3,4,5,6,7,8,9]*3, steps=5))


if __name__ == "__main__":
    main()
