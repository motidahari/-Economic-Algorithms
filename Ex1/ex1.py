import itertools

"""
    Ex1 - Economic-Algorithms
    Name - Moti Dahari
    Id - 308212570
    Github link - https://github.com/motidahari/Economic-Algorithms
"""

agents = ami = tami = rami = None


class Agent:
    def __init__(self, values: list):
        self.values = values

    def value(self, option: int) -> float:
        return self.values[option]


def isParetoImprovement(agents: list, option1: int, option2: int) -> bool:

    result: bool = True

    if option1 == option2:
        return result

    for agent in agents:
        # print(agent.value(option1), '<', agent.value(option2),
        #       ' -> ', agent.value(option1) < agent.value(option2))
        if agent.value(option1) < agent.value(option2):
            return False
    return result


def generateTextInvokeFunctionIsParetoImprovement():
    print('Generate text for invoke test function -> isParetoImprovement')
    length = range(5)
    for op1 in length:
        for op2 in length:
            # print('assert isParetoImprovement(agents, {val1}, {val2}) == {result}'.format(
            #     agents=agents, val1=op1, val2=op2, result=isParetoImprovement(agents, op1, op2)))

            print()


def isParetoImprovementTest(agents: list):
    assert isParetoImprovement(agents, 0, 0) == True
    assert isParetoImprovement(agents, 0, 1) == False
    assert isParetoImprovement(agents, 0, 2) == False
    assert isParetoImprovement(agents, 0, 3) == False
    assert isParetoImprovement(agents, 0, 4) == False
    assert isParetoImprovement(agents, 1, 0) == False
    assert isParetoImprovement(agents, 1, 1) == True
    assert isParetoImprovement(agents, 1, 2) == False
    assert isParetoImprovement(agents, 1, 3) == False
    assert isParetoImprovement(agents, 1, 4) == False
    assert isParetoImprovement(agents, 2, 0) == False
    assert isParetoImprovement(agents, 2, 1) == True
    assert isParetoImprovement(agents, 2, 2) == True
    assert isParetoImprovement(agents, 2, 3) == False
    assert isParetoImprovement(agents, 2, 4) == False
    assert isParetoImprovement(agents, 3, 0) == False
    assert isParetoImprovement(agents, 3, 1) == False
    assert isParetoImprovement(agents, 3, 2) == False
    assert isParetoImprovement(agents, 3, 3) == True
    assert isParetoImprovement(agents, 3, 4) == False
    assert isParetoImprovement(agents, 4, 0) == False
    assert isParetoImprovement(agents, 4, 1) == False
    assert isParetoImprovement(agents, 4, 2) == False
    assert isParetoImprovement(agents, 4, 3) == False
    assert isParetoImprovement(agents, 4, 4) == True


def isParetoOptimal(agents: list, option: int, allOptions: list) -> bool:

    result: bool = True

    for op in allOptions:
        # print('op = ', op, ' | option = ', option,
        #       ' | isParetoImprovement -> ', isParetoImprovement(agents, op, option))
        if op != option and isParetoImprovement(agents, op, option):
            return False
    return result


def isParetoOptimalTest(agents: list):
    assert isParetoOptimal(agents, 0, (1, 2, 3, 4)) == True
    assert isParetoOptimal(agents, 0, (1, 2, 4, 3)) == True
    assert isParetoOptimal(agents, 0, (1, 3, 2, 4)) == True
    assert isParetoOptimal(agents, 0, (1, 3, 4, 2)) == True
    assert isParetoOptimal(agents, 0, (1, 4, 2, 3)) == True
    assert isParetoOptimal(agents, 0, (1, 4, 3, 2)) == True
    assert isParetoOptimal(agents, 0, (2, 1, 3, 4)) == True
    assert isParetoOptimal(agents, 0, (2, 1, 4, 3)) == True
    assert isParetoOptimal(agents, 0, (2, 3, 1, 4)) == True
    assert isParetoOptimal(agents, 0, (2, 3, 4, 1)) == True
    assert isParetoOptimal(agents, 0, (2, 4, 1, 3)) == True
    assert isParetoOptimal(agents, 0, (2, 4, 3, 1)) == True
    assert isParetoOptimal(agents, 0, (3, 1, 2, 4)) == True
    assert isParetoOptimal(agents, 0, (3, 1, 4, 2)) == True
    assert isParetoOptimal(agents, 0, (3, 2, 1, 4)) == True
    assert isParetoOptimal(agents, 0, (3, 2, 4, 1)) == True
    assert isParetoOptimal(agents, 0, (3, 4, 1, 2)) == True
    assert isParetoOptimal(agents, 0, (3, 4, 2, 1)) == True
    assert isParetoOptimal(agents, 0, (4, 1, 2, 3)) == True
    assert isParetoOptimal(agents, 0, (4, 1, 3, 2)) == True
    assert isParetoOptimal(agents, 0, (4, 2, 1, 3)) == True
    assert isParetoOptimal(agents, 0, (4, 2, 3, 1)) == True
    assert isParetoOptimal(agents, 0, (4, 3, 1, 2)) == True
    assert isParetoOptimal(agents, 0, (4, 3, 2, 1)) == True
    assert isParetoOptimal(agents, 1, (0, 2, 3, 4)) == False
    assert isParetoOptimal(agents, 1, (0, 2, 4, 3)) == False
    assert isParetoOptimal(agents, 1, (0, 3, 2, 4)) == False
    assert isParetoOptimal(agents, 1, (0, 3, 4, 2)) == False
    assert isParetoOptimal(agents, 1, (0, 4, 2, 3)) == False
    assert isParetoOptimal(agents, 1, (0, 4, 3, 2)) == False
    assert isParetoOptimal(agents, 1, (2, 0, 3, 4)) == False
    assert isParetoOptimal(agents, 1, (2, 0, 4, 3)) == False
    assert isParetoOptimal(agents, 1, (2, 3, 0, 4)) == False
    assert isParetoOptimal(agents, 1, (2, 3, 4, 0)) == False
    assert isParetoOptimal(agents, 1, (2, 4, 0, 3)) == False
    assert isParetoOptimal(agents, 1, (2, 4, 3, 0)) == False
    assert isParetoOptimal(agents, 1, (3, 0, 2, 4)) == False
    assert isParetoOptimal(agents, 1, (3, 0, 4, 2)) == False
    assert isParetoOptimal(agents, 1, (3, 2, 0, 4)) == False
    assert isParetoOptimal(agents, 1, (3, 2, 4, 0)) == False
    assert isParetoOptimal(agents, 1, (3, 4, 0, 2)) == False
    assert isParetoOptimal(agents, 1, (3, 4, 2, 0)) == False
    assert isParetoOptimal(agents, 1, (4, 0, 2, 3)) == False
    assert isParetoOptimal(agents, 1, (4, 0, 3, 2)) == False
    assert isParetoOptimal(agents, 1, (4, 2, 0, 3)) == False
    assert isParetoOptimal(agents, 1, (4, 2, 3, 0)) == False
    assert isParetoOptimal(agents, 1, (4, 3, 0, 2)) == False
    assert isParetoOptimal(agents, 1, (4, 3, 2, 0)) == False
    assert isParetoOptimal(agents, 2, (0, 1, 3, 4)) == True
    assert isParetoOptimal(agents, 2, (0, 1, 4, 3)) == True
    assert isParetoOptimal(agents, 2, (0, 3, 1, 4)) == True
    assert isParetoOptimal(agents, 2, (0, 3, 4, 1)) == True
    assert isParetoOptimal(agents, 2, (0, 4, 1, 3)) == True
    assert isParetoOptimal(agents, 2, (0, 4, 3, 1)) == True
    assert isParetoOptimal(agents, 2, (1, 0, 3, 4)) == True
    assert isParetoOptimal(agents, 2, (1, 0, 4, 3)) == True
    assert isParetoOptimal(agents, 2, (1, 3, 0, 4)) == True
    assert isParetoOptimal(agents, 2, (1, 3, 4, 0)) == True
    assert isParetoOptimal(agents, 2, (1, 4, 0, 3)) == True
    assert isParetoOptimal(agents, 2, (1, 4, 3, 0)) == True
    assert isParetoOptimal(agents, 2, (3, 0, 1, 4)) == True
    assert isParetoOptimal(agents, 2, (3, 0, 4, 1)) == True
    assert isParetoOptimal(agents, 2, (3, 1, 0, 4)) == True
    assert isParetoOptimal(agents, 2, (3, 1, 4, 0)) == True
    assert isParetoOptimal(agents, 2, (3, 4, 0, 1)) == True
    assert isParetoOptimal(agents, 2, (3, 4, 1, 0)) == True
    assert isParetoOptimal(agents, 2, (4, 0, 1, 3)) == True
    assert isParetoOptimal(agents, 2, (4, 0, 3, 1)) == True
    assert isParetoOptimal(agents, 2, (4, 1, 0, 3)) == True
    assert isParetoOptimal(agents, 2, (4, 1, 3, 0)) == True
    assert isParetoOptimal(agents, 2, (4, 3, 0, 1)) == True
    assert isParetoOptimal(agents, 2, (4, 3, 1, 0)) == True
    assert isParetoOptimal(agents, 3, (0, 1, 2, 4)) == True
    assert isParetoOptimal(agents, 3, (0, 1, 4, 2)) == True
    assert isParetoOptimal(agents, 3, (0, 2, 1, 4)) == True
    assert isParetoOptimal(agents, 3, (0, 2, 4, 1)) == True
    assert isParetoOptimal(agents, 3, (0, 4, 1, 2)) == True
    assert isParetoOptimal(agents, 3, (0, 4, 2, 1)) == True
    assert isParetoOptimal(agents, 3, (1, 0, 2, 4)) == True
    assert isParetoOptimal(agents, 3, (1, 0, 4, 2)) == True
    assert isParetoOptimal(agents, 3, (1, 2, 0, 4)) == True
    assert isParetoOptimal(agents, 3, (1, 2, 4, 0)) == True
    assert isParetoOptimal(agents, 3, (1, 4, 0, 2)) == True
    assert isParetoOptimal(agents, 3, (1, 4, 2, 0)) == True
    assert isParetoOptimal(agents, 3, (2, 0, 1, 4)) == True
    assert isParetoOptimal(agents, 3, (2, 0, 4, 1)) == True
    assert isParetoOptimal(agents, 3, (2, 1, 0, 4)) == True
    assert isParetoOptimal(agents, 3, (2, 1, 4, 0)) == True
    assert isParetoOptimal(agents, 3, (2, 4, 0, 1)) == True
    assert isParetoOptimal(agents, 3, (2, 4, 1, 0)) == True
    assert isParetoOptimal(agents, 3, (4, 0, 1, 2)) == True
    assert isParetoOptimal(agents, 3, (4, 0, 2, 1)) == True
    assert isParetoOptimal(agents, 3, (4, 1, 0, 2)) == True
    assert isParetoOptimal(agents, 3, (4, 1, 2, 0)) == True
    assert isParetoOptimal(agents, 3, (4, 2, 0, 1)) == True
    assert isParetoOptimal(agents, 3, (4, 2, 1, 0)) == True
    assert isParetoOptimal(agents, 4, (0, 1, 2, 3)) == True
    assert isParetoOptimal(agents, 4, (0, 1, 3, 2)) == True
    assert isParetoOptimal(agents, 4, (0, 2, 1, 3)) == True
    assert isParetoOptimal(agents, 4, (0, 2, 3, 1)) == True
    assert isParetoOptimal(agents, 4, (0, 3, 1, 2)) == True
    assert isParetoOptimal(agents, 4, (0, 3, 2, 1)) == True
    assert isParetoOptimal(agents, 4, (1, 0, 2, 3)) == True
    assert isParetoOptimal(agents, 4, (1, 0, 3, 2)) == True
    assert isParetoOptimal(agents, 4, (1, 2, 0, 3)) == True
    assert isParetoOptimal(agents, 4, (1, 2, 3, 0)) == True
    assert isParetoOptimal(agents, 4, (1, 3, 0, 2)) == True
    assert isParetoOptimal(agents, 4, (1, 3, 2, 0)) == True
    assert isParetoOptimal(agents, 4, (2, 0, 1, 3)) == True
    assert isParetoOptimal(agents, 4, (2, 0, 3, 1)) == True
    assert isParetoOptimal(agents, 4, (2, 1, 0, 3)) == True
    assert isParetoOptimal(agents, 4, (2, 1, 3, 0)) == True
    assert isParetoOptimal(agents, 4, (2, 3, 0, 1)) == True
    assert isParetoOptimal(agents, 4, (2, 3, 1, 0)) == True
    assert isParetoOptimal(agents, 4, (3, 0, 1, 2)) == True
    assert isParetoOptimal(agents, 4, (3, 0, 2, 1)) == True
    assert isParetoOptimal(agents, 4, (3, 1, 0, 2)) == True
    assert isParetoOptimal(agents, 4, (3, 1, 2, 0)) == True
    assert isParetoOptimal(agents, 4, (3, 2, 0, 1)) == True
    assert isParetoOptimal(agents, 4, (3, 2, 1, 0)) == True


def generateTextInvokeFunctionIsParetoOptimal():
    print('Generate text for invoke test function -> isParetoOptimal')
    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    for lst in permutations:
        removed: int = lst[0]
        newList = lst[1:]
        print('assert isParetoOptimal(agents, {val1}, {val2}) == {result}'.format(
            agents=agents, val1=removed, val2=newList, result=isParetoOptimal(agents, removed, newList)))
    print()


if __name__ == "__main__":
    ami = Agent([1, 2, 3, 4, 5])
    tami = Agent([3, 1, 2, 5, 4])
    rami = Agent([3, 5, 5, 1, 1])
    agents = [ami, tami, rami]
    isParetoImprovementTest(agents)
    isParetoOptimalTest(agents)
