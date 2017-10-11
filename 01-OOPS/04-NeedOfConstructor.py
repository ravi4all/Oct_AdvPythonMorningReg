class Player:

    names = []
    score = []

    def printName(self, n,s):
        # Player.names.append(n)
        # Player.score.append(s)
        # print("Player Name : {} Player Score : {}".format(Player.names, Player.score))
        self.names.append(n)
        self.score.append(s)
        print("Player Name : {} Player Score : {}".format(self.names, self.score))

obj = Player()
obj.printName('Sachin',78)
obj.printName('Rahul',72)


obj_1 = Player()
obj_1.printName('Kohli',102)
