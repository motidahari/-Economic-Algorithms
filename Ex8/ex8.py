

def conditional_utilitarian(total: float, subjects: list[str], preferences: list[list[str]]):
    """
        :param total: Amount to donate.
        :param subjects: Subject names.
        :param preferences: List of preferences of every citizen.
        :return citizen_donate: The donate of each citizen by subject
        :return total_donate: Total donate by subject
    """
    # initialization
    amount_support = {}  # Number of supporters by subject.
    total_donate = {}  # The amount of the donation.
    for i in subjects:
        amount_support[i] = 0
        total_donate[i] = 0

    # Counting the donations
    for i in preferences:
        for j in i:
            amount_support[j] += 1

    citizen_donate = []  # List of all donations by citizen.
    one_donate = total/(len(preferences))  # The amount each citizen donate.

    for i in preferences:
        max = 0
        temp_donate = {}
        for j in i:
            # Checks which is the preferred subject among what the citizen has chosen
            if amount_support[j] > max:
                max = amount_support[j]
                temp_donate = {}
                temp_donate[j] = 0
            elif amount_support[j] == max:
                temp_donate[j] = 0

        one_citizen_donate = one_donate/len(temp_donate)
        # Adds the citizen donate.
        for j in temp_donate.keys():
            temp_donate[j] = one_citizen_donate
            total_donate[j] += one_citizen_donate
        citizen_donate.append(temp_donate)

    return citizen_donate, total_donate


def run(values: list[str], donations: list[list[str]], sum: float, number: int):

    print("Example {number} \n------------------".format(number=number))
    j = 1
    for i in donations:
        print('player number {j} : {i}'.format(j=j, i=i))
        j += 1
    print("\nTotal donate - {sum}\n".format(sum=sum))
    donates, total = conditional_utilitarian(sum, values, donations)
    print("=============================")
    print("\nDonate of each citizen by subject -\n")
    j = 1
    for i in donates:
        print('player number {j} : {i}'.format(j=j, i=i))
        j += 1
    print("\nTotal donate by subject - \n {total}".format(total=total))
    print("=============================\n\n")


if __name__ == "__main__":
    values = []
    donations = []
    sums = []

    sub1 = ["a", "b", "c", "d"]
    don1 = [["a", "b"], ["a", "c"], ["a", "d"], ["b", "c"], ["a"]]
    sum1 = 500

    sub2 = ["a", "b", "c", "d"]
    don2 = [["d", "b"], ["a", "c"], ["a", "d"], ["b", "c"], ["a"]]
    sum2 = 500

    sub3 = ["a", "b", "c", "d"]
    don3 = [["a", "b", "c", "d"], ["a", "b"], [
        "b", "c"], ["c", "d"], ["a", "d"]]
    sum3 = 800

    sub4 = ["a", "b", "c", "d"]
    don4 = [["a", "b"], ["b", "c"], [
        "a", "b", "c", "d"], ["a", "d"], ["b", "d"]]
    sum4 = 800

    values = [sub1, sub2, sub3, sub4]
    donations = [don1, don2, don3, don4]
    sums = [sum1, sum2, sum3, sum4]

    for x in range(len(values)):
        run(values[x], donations[x], sums[x], x+1)

    # run(sub1, don1, sum1, 1)
