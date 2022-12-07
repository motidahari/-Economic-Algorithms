import itertools
"""
    Ex6 - Economic-Algorithms
    Name - Moti Dahari
    Id - 308212570
    Github link - https://github.com/motidahari/Economic-Algorithms
"""
agents = ami = tami = rami = None


class OrderlyDivision:
    def __init__(self, values: list):
        self.order = '>'
        self.values = self.mergeSortByPreference(values)

    def getValues(self) -> list:
        if len(self.values) == 0:
            return []
        return self.values

    def getItems(self) -> list:
        if len(self.items) == 0:
            return []
        return self.items

    def setValuesOtherPlayer(self, otherPlayer=None) -> None:
        if otherPlayer is not None:
            self.otherPlayer = otherPlayer
            self.ratioCalculation()
        else:
            self.otherPlayer = None
            self.ratioCalcValues = None

    def getRatioCalcValues(self) -> list:
        if len(self.ratioCalcValues) == 0:
            return []
        return self.ratioCalcValues

    def getOtherPlayer(self):
        if self.otherPlayer is None:
            return None
        return self.otherPlayer

    def getPreferenceByValue(self, value: int) -> float:
        x = range(len(self.values))
        for idx, v in enumerate(self.values):
            # print('idx = {idx} , v = {v}'.format(idx=idx, v=v))
            if v[0] == value:
                return v[1]
        raise Exception("Error while search specific value in values")

    def getPreferenceByValueFromRatioCalculation(self, value: int) -> float:
        x = range(len(self.ratioCalcValues))
        for idx, v in enumerate(self.values):
            # print('idx = {idx} , v = {v}'.format(idx=idx, v=v))
            if v[0] == value:
                return v[1]
        raise Exception("Error while search specific value in values")

    def checkOrderlyDivision(self) -> bool:
        otherFlayer = self.getOtherPlayer()
        if (otherFlayer == None):
            raise Exception("Error - other player is not exist")

        for idx, v in enumerate(self.ratioCalcValues):
            item = v[0]
            valueA = v[1]
            valueB = otherFlayer.getPreferenceByValueFromRatioCalculation(item)
            if (valueB > valueA):
                return False
        return True

    def mergeSortByPreference(self, arr, order='>') -> list:
        if len(arr) > 1:
            # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
            # Sort the two halves
            self.mergeSortByPreference(sub_array1)
            self.mergeSortByPreference(sub_array2)
            # Initial values for pointers that we use to keep track of where we are in each array
            i = j = k = 0

            # Until we reach the end of either start or end, pick larger among
            # elements start and end and place them in the correct position in the sorted array
            while i < len(sub_array1) and j < len(sub_array2):
                # print('{val1} < {val2}   |    {valid}'.format(
                #     val1=sub_array1[i][1], val2=sub_array2[j][1], valid=sub_array1[i][1] < sub_array2[j][1]))
                # print('condition: ', sub_array1[i][1] < sub_array2[j][1])

                if order == '>':
                    if sub_array1[i][1] > sub_array2[j][1]:
                        arr[k] = sub_array1[i]
                        i += 1
                    else:
                        arr[k] = sub_array2[j]
                        j += 1

                else:
                    if sub_array1[i][1] < sub_array2[j][1]:
                        arr[k] = sub_array1[i]
                        i += 1
                    else:
                        arr[k] = sub_array2[j]
                        j += 1
                k += 1

            # When all elements are traversed in either arr1 or arr2,
            # pick up the remaining elements and put in sorted array
            while i < len(sub_array1):
                # print('sub_array1[{i}] {val}'.format(val=sub_array1[i], i=i))
                arr[k] = sub_array1[i]
                i += 1
                k += 1

            while j < len(sub_array2):
                # print('sub_array2[{j}] {val}'.format(val=sub_array2[j], j=j))
                arr[k] = sub_array2[j]
                j += 1
                k += 1
        # print('arr', arr)
        return arr

    def ratioCalculation(self) -> None:
        if len(self.values) != len(self.otherPlayer.getValues()):
            raise Exception(
                "Error while call to ratioCalculation, arrays is not are the same size")

        arr = []
        # print(self.values)
        # print(self.playerB.getValues())
        for idx, v in enumerate(self.values):
            obj = []
            valP1 = v[0]
            preferenceP1 = v[1]
            preferenceP2 = self.otherPlayer.getPreferenceByValue(valP1)
            obj.append(valP1)

            try:
                obj.append(preferenceP1/preferenceP2)
            except:
                obj.append(float('inf'))

            arr.append(obj)
        array = self.mergeSortByPreference(arr)
        self.ratioCalcValues = array
        self.items = []
        for i in self.ratioCalcValues:
            self.items.append(i[0])

    def __str__(self) -> str:
        string = ''
        string += 'Player values:\n\n'
        string += 'Player values:\nValue:\tPreference:\n'
        string += '\n'.join(['\t'.join([str(cell)
                                        for cell in row]) for row in self.values]) + '\n\n'
        # if self.otherPlayer is not None:
        #     string += 'OtherPlayer:\nValue:\tPreference:\n'
        #     string += '\n'.join(['\t'.join([str(cell)
        #                                     for cell in row]) for row in self.otherPlayer.getValues()]) + '\n\n'

        if self.ratioCalcValues is not None:

            string += 'ratioCalcValues from playerA to PlayerB:\n'
            string += 'Value:\tPreference:\n'
            string += '\n'.join(['\t'.join([str(cell)
                                            for cell in row]) for row in self.ratioCalcValues]) + '\n\n'
        string += 'Player items: {items}\n'.format(items=self.items)

        return string

    def getString(self) -> str:
        string = ''
        string += 'Player values:\n\n'
        string += 'Player values:\nValue:\tPreference:\n'
        string += '\n'.join(['\t'.join([str(cell)
                                        for cell in row]) for row in self.values]) + '\n\n'
        # if self.otherPlayer is not None:
        #     string += 'OtherPlayer:\nValue:\tPreference:\n'
        #     string += '\n'.join(['\t'.join([str(cell)
        #                                     for cell in row]) for row in self.otherPlayer.getValues()]) + '\n\n'

        if self.ratioCalcValues is not None:

            string += 'ratioCalcValues from playerA to PlayerB:\n'
            string += 'Value:\tPreference:\n'
            string += '\n'.join(['\t'.join([str(cell)
                                            for cell in row]) for row in self.ratioCalcValues]) + '\n\n'
        string += 'Player items: {items}\n ********************************************\n\n'.format(
            items=self.items)

        return string

    def getSumByItems(self, list: list) -> float:
        sum = 0
        for item in list:
            for val in self.values:
                if (item == val[0]):
                    sum += val[1]
        return sum


def algo(playerA: OrderlyDivision, playerB: OrderlyDivision):
    result = ''
    # step a
    playerA.setValuesOtherPlayer(playerB)
    playerB.setValuesOtherPlayer(playerA)
    result += playerA.getString()
    result += playerB.getString()
    # result += '********************************************\n\n'

    check = playerA.checkOrderlyDivision()
    if (check == True):
        return True
    result += 'checkOrderlyDivision = false\n'
    # step b
    sumPlayerA = playerA.getSumByItems(playerA.getItems())
    sumPlayerB = 0
    items = playerA.getItems()
    itemsPlayerA = items
    itemsPlayerB = []
    # step c,d
    for item in range(len(items) - 1, -1, -1):
        sumPlayerA = playerA.getSumByItems(itemsPlayerA)
        sumPlayerB = playerB.getSumByItems(itemsPlayerB)
        itemVal = items[item]
        priceItemPlayerA = playerA.getPreferenceByValue(itemVal)
        priceItemPlayerB = playerA.getOtherPlayer().getPreferenceByValue(itemVal)
        if (sumPlayerA == sumPlayerB):
            break
        if (sumPlayerA > sumPlayerB) and (sumPlayerB + priceItemPlayerB > sumPlayerA - priceItemPlayerA):
            checkA = sumPlayerA - priceItemPlayerA
            checkB = sumPlayerB + priceItemPlayerB
            result += 'sumPlayerA: {sumPlayerA}\n'.format(
                sumPlayerA=sumPlayerA)
            result += 'sumPlayerB: {sumPlayerB}\n'.format(
                sumPlayerB=sumPlayerB)
            splitItem = round(abs(checkA - checkB) / 2, 2)
            result += 'checkA(sumPlayerA - priceItemPlayerA): {checkA}\n'.format(
                checkA=round(checkA, 2))
            result += 'checkB(sumPlayerB + priceItemPlayerB): {checkB}\n'.format(
                checkB=round(checkB, 2))

            result += 'item: {item} , splitItem: {splitItem}\n'.format(
                item=items[item], splitItem=splitItem)
            result += 'splitItem: {splitItem}\n\n'.format(splitItem=splitItem)
            sumPlayerA -= priceItemPlayerA - splitItem
            sumPlayerB += priceItemPlayerB - splitItem
            itemsPlayerB.append(itemVal)

            break
        else:
            itemsPlayerA.remove(itemVal)
            itemsPlayerB.append(itemVal)
            sumPlayerA -= priceItemPlayerA
            sumPlayerB += priceItemPlayerB

    result += 'result:\n itemsPlayerA: {itemsPlayerA}, totalPriceA: {sumPlayerA}\n itemsPlayerB: {itemsPlayerB}, totalPriceB: {sumPlayerB}\n'.format(itemsPlayerA=itemsPlayerA, sumPlayerA=round(sumPlayerA, 2),
                                                                                                                                                     itemsPlayerB=itemsPlayerB, sumPlayerB=round(sumPlayerB, 2))
    return result


if __name__ == "__main__":
    playerA = OrderlyDivision([[40, 1], [30, 0], [20, 0.4], [10, 0.7]])
    playerB = OrderlyDivision([[10, 0], [20, 1], [30, 0.6], [40, 0.3]])
    print(algo(playerA, playerB))
