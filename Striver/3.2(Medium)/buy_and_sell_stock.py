from engine import Engine

test_cases = [(([10,1,5,6,7,1],), 6), (([10,8,7,5,2],), 0)]
run = Engine(test_cases)

'''
Problem Link:
https://neetcode.io/problems/buy-and-sell-crypto/question
'''

# ---Solutions----------------------------------------------------------------------------------------


# ---1----DP------------------------------------------------------------------------------------------
"""
iterate over the array
assign the current element to buy_price if it is SMALLER
in the next iteration, check profit
compare with max profit
return max profit
"""


def max_profit_two_pointer(prices: list[int]) -> int:
    max_profit = 0
    buy_price = prices[0]

    for price in prices:
        max_profit = max(price - buy_price, max_profit)
        buy_price = min(price, buy_price)

    return max_profit



# ----Two Pointer-----------------------------------------------------------------------------
"""
Set l = 0
iterate over the array with r
if price at r is lower than price at l
assign the value of r to l
at other points, compute profit and compare with max_profit
return max_profit
"""


def max_profit_dp(prices: list[int]) -> int:
    l = 0
    max_profit = 0

    for r, price in enumerate(prices):
        if price < prices[l]:
            l = r
        else:
            max_profit = max(max_profit, price - prices[l])

    return max_profit


run.v8(max_profit_dp)
run.v8(max_profit_two_pointer)

run.compare(max_profit_dp, max_profit_two_pointer)