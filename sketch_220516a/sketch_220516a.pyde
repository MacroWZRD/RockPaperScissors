class player():
    #store object name, score, tick
    def __init__(self, name, score, tick):
        self.name = name
        self.score = score
        self.tick = tick
    #add 1 to player score
    def add_score(self):
        self.score += 1
    #reset the player score
    def reset_score(self):
        self.score = 0
    #return the stored object values
    def value(self):
        return self.name, self.score, self.tick
