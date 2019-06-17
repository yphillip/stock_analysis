from rule_one_investing \
    import calc_moving_average, calc_exp_moving_average, calc_portfolio_value


def test_calc_moving_average():
    assert calc_moving_average([1,2], steps=2) == [0, 1.5]
    assert calc_moving_average([1,2], steps=1) == [1, 2]
    assert calc_moving_average([1,2,3], steps=1) == [1, 2, 3]
    assert calc_moving_average([1,2,3], steps=2) == [0, 1.5, 2.5]
    assert calc_moving_average([1,2,3], steps=3) == [0, 0, 2]


def test_calc_exp_moving_average():
    assert [round(val,2) for val in calc_exp_moving_average([14,13,14,12,13,12], steps=5)] == [0,0,0,0,13.2,12.8]
    assert [round(val,2) for val in calc_exp_moving_average([14,13,14,12,13,12,11], steps=5)] == [0,0,0,0,13.2,12.8,12.2]


def test_calc_portfolio_value():
    trades = [
        ('BUY', 1.00),  # buy 100 shares, $0 in wallet
        ('SELL', 2.00),  # sell 100 shares, $200 in wallet
        ('BUY', 1.50),  # buy 133 shares, $0.50 in wallet
        ('SELL', 3.00)  # sell 133 shares, $399.50 in wallet
    ]
    s_wallet = 100
    assert calc_portfolio_value(trades[0:1], starting_wallet=s_wallet) == 0
    assert calc_portfolio_value(trades[0:2], starting_wallet=s_wallet) == 200
    assert calc_portfolio_value(trades[0:3], starting_wallet=s_wallet) == 0.50
    assert calc_portfolio_value(trades[0:4], starting_wallet=s_wallet) == 399.50


def main():
    test_calc_moving_average()


if __name__ == "__main__":
    main()

