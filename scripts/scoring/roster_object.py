################################################################################
# description: The object in this file is what should be returned by any
# score generator. It holds a score atribute for every player.
# contributors: Connor Stone
# date: 04-03-2016
################################################################################


class Roster(object):

    def __init__(self, players):

        self.players = {}
        self.scores = {}
        
        for p in players:
            self.players[p['Id']] = p
            self.scores[p['Id']] = -1

    def SetScore(self, player_id, score):

        try:
            self.scores[player_id] = score
        except:
            raise ValueError('player_id not in roster')


    def GetScore(self, player_id):
        
        try:
            return self.scores[player_id]
        except:
            raise ValueError('player_id not in roster')


    def GetIds(self):
        
        return self.players.keys()

        
    def AddPlayer(self, player):

        if not player['Id'] in self.players:
            self.players[player['Id']] = player
            self.scores[player['Id']] = -1

            
    def RemovePlayer(self, player):

        try:
            del players[player]
        except:
            raise ValueError('player_id not in roster')    


    def IsScored(self):

        for s in self.scores:
            if self.scores[s] = -1:
                return False
        else:
            return True
