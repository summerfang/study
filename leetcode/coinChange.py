from itertools import combinations_with_replacement

def count_change(coins, n, change):
    # step 1: sort the coins
    # step 2: maximum number you can choose for smallest coin is sum / smallest coin, say it is max_i
    max_i =  int(change / min(coins))  if  change % min(coins) == 0 else int(change / min(coins)) + 1

    count = 0
    # step 3: calcluate select i belong to (0, max_i) for each coin
    for i in range(1, max_i + 1):
        combinations = list(combinations_with_replacement(coins, i))
        for x in combinations:
            if change == sum(x):
                count += 1
                print(x)

    return count    
    # step 4: sum up all the possible combinations, if summary is equal to sum, then count + 1, push the combination to a dict

if __name__ == '__main__':
    coins = [1, 2, 3]
    n = len(coins)
    change = 10
    print(count_change(coins, n, change))