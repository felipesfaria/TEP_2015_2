__author__ = 'felipesfaria'

import random
TESTS = 10.0**5

def RollDice(probabilties,sum):
    size = len(probabilties)
    roll = random.uniform(0,sum)
    sum = 0
    for i in range(0,size):
        sum+=probabilties[i]
        if(roll<=sum):
            return i

def Trio(probabilities,sum):
    firstRoll = RollDice(probabilities,sum)
    if(firstRoll != RollDice(probabilities,sum)):
        return False
    if(firstRoll != RollDice(probabilities,sum)):
        return False
    return True;

def TwoPairs(probabilities,sum):
    firstRoll = RollDice(probabilities,sum)
    if(firstRoll != RollDice(probabilities,sum)):
        return False
    thirdRoll = RollDice(probabilities,sum)
    if(thirdRoll != RollDice(probabilities,sum)):
        return False
    return True

def AdifC(probabilities,sum):
    firstRoll = RollDice(probabilities,sum)
    RollDice(probabilities,sum)
    if(firstRoll!=RollDice(probabilities,sum)):
        return 1
    return 0

def AdifCGivenAdifB(probabilities,sum):
    firstRoll = RollDice(probabilities,sum)
    if(firstRoll==RollDice(probabilities,sum)):
        return -1;
    if(firstRoll!=RollDice(probabilities,sum)):
        return 1
    return 0

def PrintCompareCondicionalProbabilityResult(type,l1,l2):
    print type
    print "P(A!=C)={}".format(l1[1]/float((l1[0]+l1[1])))
    print "P(A!=C | A!=B)={}".format(l2[1]/float((l2[0]+l2[1])))

def CompareCondicionalProbability():
    print "Compare Condicional Probability"
    honestDice = [1]*6
    honestSum = 6
    dishonestDice = [1]*5
    dishonestDice.append(5)
    dishonestSum = 10
    honestAdifC = [0,0]
    dishonestAdifC = [0,0]
    honestAdifCGivenAdifB = [0,0]
    dishonestAdifCGivenAdifB = [0,0]
    for i in range(int(TESTS)):
        honestAdifC[AdifC(honestDice,honestSum)]+=1
        result = AdifCGivenAdifB(honestDice,honestSum)
        if(result!=-1):
            honestAdifCGivenAdifB[result]+=1
            
        dishonestAdifC[AdifC(dishonestDice,dishonestSum)]+=1
        result = AdifCGivenAdifB(dishonestDice,dishonestSum)
        if(result!=-1):
            dishonestAdifCGivenAdifB[result]+=1

    PrintCompareCondicionalProbabilityResult("Honest",honestAdifC,honestAdifCGivenAdifB)
    print ""
    PrintCompareCondicionalProbabilityResult("Dishonest",dishonestAdifC,dishonestAdifCGivenAdifB)

def TestDice():
    print "Test Dice"
    honestDice = [1]*6
    honestSum = 6

    dishonestDice = [1]*5
    dishonestDice.append(5)
    dishonestSum = 10
    honestRolls = [0]*len(honestDice)
    dishonestRolls = [0]*len(dishonestDice)
    for i in range(int(TESTS)):
        honestRolls[RollDice(honestDice,honestSum)]+=1
        dishonestRolls[RollDice(dishonestDice,dishonestSum)]+=1
    for i in range(len(honestRolls)):
        honestRolls[i] = honestRolls[i]/TESTS
        dishonestRolls[i] = dishonestRolls[i]/TESTS
    print "Honest"
    print honestRolls
    print "Dishonest"
    print dishonestRolls


def TrioOrTwoPairs():
    print "TrioOrTwoPairs"
    honestDice = [1]*6
    honestSum = 6

    dishonestDice = [1]*5
    dishonestDice.append(5)
    dishonestSum = 10
    honestWins = [0,0]
    dishonestWins = [0,0]
    for i in range(int(TESTS)):
        if(Trio(honestDice,honestSum)):
            honestWins[0]+=1
        if(TwoPairs(honestDice,honestSum)):
            honestWins[1]+=1
        if(Trio(dishonestDice,dishonestSum)):
            dishonestWins[0]+=1
        if(TwoPairs(dishonestDice,dishonestSum)):
            dishonestWins[1]+=1

    print("honest")
    print("Trio: {}\t TwoPairs:{}".format(honestWins[0]/TESTS,honestWins[1]/TESTS))

    print("dishonest")
    print("Trio: {}\t TwoPairs:{}".format(dishonestWins[0]/TESTS,dishonestWins[1]/TESTS))

CompareCondicionalProbability()