import itertools
"""
    Ex6 - Economic-Algorithms
    Name - Moti Dahari
    Id - 308212570
    Github link - https://github.com/motidahari/Economic-Algorithms
"""
agents = ami = tami = rami = None


class OrderlyDivision:
    def __init__(self, values: list, playerB=None):
        self.order = '>'
        self.values = self.mergeSortByPreference(values)
        if playerB is not None:
            self.playerB = playerB
            self.ratioCalculation()
        else:
            self.playerB = None
            self.ratioCalcValues = None

    def getValues(self) -> float:
        if len(self.values) == 0:
            return []
        return self.values

    def getRatioCalcValues(self) -> float:
        if len(self.ratioCalcValues) == 0:
            return []
        return self.values

    def getpPlayerB(self):
        if self.playerB is None:
            return None
        return self.playerB

    def getPreferenceByValue(self, value: int) -> float:
        x = range(len(self.values))
        for idx, v in enumerate(self.values):
            # print('idx = {idx} , v = {v}'.format(idx=idx, v=v))
            if v[0] == value:
                return v[1]
        raise Exception("Error while search specific value in values")

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
        if len(self.values) != len(self.playerB.getValues()):
            raise Exception(
                "Error while call to ratioCalculation, arrays is not are the same size")

        arr = []
        # print(self.values)
        # print(self.playerB.getValues())
        for idx, v in enumerate(self.values):
            obj = []
            valP1 = v[0]
            preferenceP1 = v[1]
            preferenceP2 = self.playerB.getPreferenceByValue(valP1)
            obj.append(valP1)

            try:
                obj.append(round(preferenceP1/preferenceP2, 2))
            except:
                obj.append(1)

            arr.append(obj)
        array = self.mergeSortByPreference(arr)
        self.ratioCalcValues = array

    def validateRatio(self, playerB) -> bool:
        # self.ratioCalculation(playerB)
        print(self.values)

    def __str__(self) -> str:
        string = ''
        string += 'Player values:\n\n'
        string += 'values:\nValue:\tPreference:\n'
        string += '\n'.join(['\t'.join([str(cell)
                                        for cell in row]) for row in self.values]) + '\n\n'

        if self.playerB is not None:
            string += 'playerB:\nValue:\tPreference:\n'
            string += '\n'.join(['\t'.join([str(cell)
                                            for cell in row]) for row in playerB.getValues()]) + '\n\n'

        if self.ratioCalcValues is not None:

            string += 'ratioCalcValues from playerA to PlayerB:\n'
            string += 'Value:\tPreference:\n'
            string += '\n'.join(['\t'.join([str(cell)
                                            for cell in row]) for row in self.ratioCalcValues]) + '\n\n'

        return string


if __name__ == "__main__":
    playerB = OrderlyDivision([[10, 0], [20, 1], [30, 0.6], [40, 0.3]])
    playerA = OrderlyDivision(
        [[40, 1], [30, 0], [20, 0.4], [10, 0.7]], playerB)
    print(playerA)
    # print(playerB)
