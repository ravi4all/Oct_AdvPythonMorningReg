class Player:

    # __init__ - Constructor
    def __init__(self, team):
        self.team = team
        self.names = []
        self.score = []

    def printName(self, n,s):
        self.names.append(n)
        self.score.append(s)
        self.teamScore = sum(self.score)
        print("Player Name : {} Player Score : {}".format(self.names, self.score))
        print("Team : ",self.team)

    def printTeamScore(self):
        print(self.team, ":", self.teamScore)

obj = Player('India')
obj.printName('Sachin',78)
obj.printName('Rahul',72)
obj.printTeamScore()


obj_1 = Player('Aus')
obj_1.printName('Smith',102)
obj_1.printTeamScore()
