# what if subproblem is unsolvable?
knownresults = {}
coinList = [1,2,5]
for coin in coinList:
    knownresults[coin] = 1


def qn(coinlist, target, knownresults):
    minCoin = target
    if target in knownresults:
        return knownresults[target]
    else:
        for i in [c for c in coinlist if c <= target]:
            knownresults[target] = min(minCoin, 
                                       qn(coinlist, target-i, knownresults) +1)
            minCoin = knownresults[target]

    return knownresults[target]

for target in xrange(1,20):
    print "given %s doller(s), need %s coin(s)" % (
        target, qn(coinList, target, knownresults))
