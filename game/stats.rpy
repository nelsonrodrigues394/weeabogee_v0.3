init python:
    class Level(object):
        def __init__(self, nome="", experience=0, level=1, maxLevel=10, maxExp=100):
            self.nome = nome
            self.experience = experience
            self.level = level
            self.maxLevel = maxLevel
            self.maxExp = maxExp

        def giveExp(self, exp):
            self.experience += exp
            if self.experience >= self.maxExp and self.level <= self.maxLevel:
                self.level += 1
                newMaxExp = self.maxExp * 2
                self.setMaxExp(newMaxExp)

        # SETTERS
        def setMaxExp(self, maxExp):
            self.maxExp = maxExp
            return self.maxExp

        def setMaxLevel(self, maxLevel):
            self.maxLevel = maxLevel
            return self.maxLevel

        def setNome(self, nome):
            self.nome = nome
            return self.nome

        def setExperience(self, exp):
            self.experience = exp
            return self.experience

        def setLevel(self, level):
            self.level = level
            return self.level

        # GETTERS
        def getMaxExp(self):
            return self.maxExp

        def getMaxLevel(self):
            return self.maxLevel

        def getNome(self):
            return self.nome

        def getExperience(self):
            return self.experience

        def getLevel(self):
            return self.level
        

        @property
        def string(self):
            return "%s: %d - EXP: %d"%(self.getNome(),self.getLevel(), self.getExperience())