def initialization(subjects: list[str]):
    """
        This function takes in a list of subjects and returns two dictionaries initialized to 0: 


    Args:
        subjects (list[str]): list of subjects

    Returns:
        countingDonations:   (number of supporters by subject).
        totalDonate:         (amount of the donation).
    """
    countingDonations = dict.fromkeys(
        subjects, 0)  # Number of supporters by subject.
    totalDonate = dict.fromkeys(subjects, 0)  # The amount of the donation.

    return countingDonations, totalDonate


def getDonationCount(preferences: list[list[str]], countingDonations: list[list[int]]):
    """
        This function returns an object with numeric values of the number of occurrences for each value. 
        It does this by iterating over the preferences list and incrementing the value in the countingDonations 
        dictionary for each preference.

    Args:
        preferences (list[list[str]]): donation preferences for each donor
        countingDonations (list[list[int]]): number of supporters by subject

    Returns:
        countingDonations (list[list[int]]): number of supporters by subject after counting
    """
    for row in preferences:  # run on every donor.
        for col in row:      # Running for each donation of a donor.
            countingDonations[col] += 1

    return countingDonations


def algo(preferences: list[list[str]], countingDonations: list[list[int]], totalDonate: list[list[int]], donationForOnePerson: float):
    """
        This function takes in the preferences, countingDonations, and totalDonate dictionaries and a donation amount for each citizen. 
        It returns a list of donations made by each citizen. 
        It does this by iterating over the preferences list and calculating the donation for each citizen based on the number of 
        times their preferred subject appears in the countingDonations dictionary.

    Args:
        preferences (list[list[str]]): donation preferences for each donor
        countingDonations (list[list[int]]): number of supporters by subject
        totalDonate (list[list[int]]): total donate from everyone
        donationForOnePerson (float): number of supporters by subject

    Returns:
        result: total donate from everyone
        totalDonate: Total donation from each donor
    """
    citizen_donate = []  # List of all donations by citizen.
    # The amount each citizen donate.

    for i in preferences:
        max = 0
        temp = {}
        for j in i:
            # Checks which is the preferred subject among what the citizen has chosen
            if countingDonations[j] > max:
                max = countingDonations[j]
                temp = {}
                temp[j] = 0
            elif countingDonations[j] == max:
                temp[j] = 0

        one_citizen_donate = donationForOnePerson/len(temp)
        # Adds the citizen donate.
        for j in temp.keys():
            temp[j] = one_citizen_donate
            totalDonate[j] += one_citizen_donate
        citizen_donate.append(temp)
    return citizen_donate, totalDonate


def conditional_utilitarian(total: float, subjects: list[str], preferences: list[list[str]]):
    """
        This function takes in the total sum of donations, the list of subjects, and the list of preferences. 
        It returns the donations made by each citizen by subject and the total donations made by each subject. 
        It does this by calling the initialization, getDonationCount, and algo functions and returning the resulting values.

    Args:
        total (float): total donations from all donation 
        subjects (list[str]): list of subjects
        preferences (list[list[str]]): donation preferences for each donor

    Returns:
        result: citizen_donate and totalDonate 
    """
    # initialization
    countingDonations, totalDonate = initialization(subjects)
    # Counting the donations by all donates
    countingDonations = getDonationCount(preferences, countingDonations)
    # Variable representing a donation for each donor
    donationForOnePerson = total/(len(preferences))

    return algo(preferences, countingDonations,
                totalDonate, donationForOnePerson)


def run(values: list[str], donations: list[list[str]], sum: float, number: int):
    """
        This function is used to test the script with example data. 
        It takes in a list of values (i.e. subjects), 
        a list of donations (i.e. preferences), 
        a sum (i.e. total) and a number (i.e. example number). 
        It prints the donations made by each citizen and the total donations made by each subject.

    Args:
        values (list[str]): list of subjects
        donations (list[list[str]]): list of donation preferences for each donor
        sum (float): sum of donations from all donation
        number (int): number of run
    """

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
    # run(sub4, don4, sum4, 1)

    for idx in range(len(values)):
        run(values[idx], donations[idx], sums[idx], idx+1)
