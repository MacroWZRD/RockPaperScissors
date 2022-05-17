class player():
    #store object name, score
    def __init__(self, name, score):
        self.name = name
        self.score = score
    #add 1 to player score
    def add_score(self):
        self.score += 1
    #reset the player score
    def reset_score(self):
        self.score = 0
    #return the stored object values
    def value(self):
        return self.name, self.score
    
def setup():
    size(700, 500)
    
def draw():
    
