numberVoters = int(input("The number of voters : "))

candidates = ["Mohamed","Ahmed","Saleh","Ali"]
voters = []

class Voter:
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return f"{self.first} {self.second} {self.third}"

class Candidate:
    def __init__(self,numVotes):
        self.numVotes = numVotes

    def __str__(self):
        return f"Number of votes : {numberVoters}"

for i in range(numberVoters):
    first = input("Rank 1 : ")
    if first not in candidates:
        first = input("Rank 1 : ")

    second = input("Rank 2 : ")
    if (second not in candidates) or second==first:
        second = input("Rank 2 : ")

    third = input("Rank 3 : ")
    if third not in candidates or (third==first or third==second):
        third = input("Rank 3 : ")

    print()
    voters.append(Voter(first,second,third))



def win():

    win = False

    firstRanks = []

    for voter in voters:
        firstRanks.append(voter.first)

    votersByCandidate = [0,0,0,0]

    for firstRank in firstRanks:
        i = candidates.index(firstRank)
        votersByCandidate[i]+=1

    while not(win):
    


        for vote in votersByCandidate:
            if vote==0:
                j = votersByCandidate.index(vote)
                votersByCandidate.remove(vote)
                candidates.remove(candidates[j])

        minimum = min(votersByCandidate)
        index = votersByCandidate.index(minimum)

        minimumCandidate = candidates[index]

        for voter in voters:
            if voter.first == minimumCandidate:
                if voter.second in candidates:
                    s = voter.second
                    i = candidates.index(s)
                    votersByCandidate[i]+=1
                elif voter.third in candidates:
                    t = voter.third
                    i = candidates.index(t)                
                    votersByCandidate[i]+=1

        candidates.remove(minimumCandidate)
        votersByCandidate.remove(votersByCandidate[index])

        if max(votersByCandidate)>(numberVoters//2):
            win = True

    maximum = max(votersByCandidate)
    index = votersByCandidate.index(maximum)

    print(f"The winner is {candidates[index]} !")

win()