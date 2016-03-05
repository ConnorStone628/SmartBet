################################################################################
# description: The object in this file is what should be returned by any
# score generator. It holds a score attribute for every player.
# contributors: Connor Stone
# date: 04-03-2016
################################################################################

# Holds all of the players and their information for a given day
#-------------------------------------------------------------------------------
class Roster(object):

    # Initializes the roster object with a dictionary of players and scores
    # players: A dictionary of players for the day, indexed by their unique id
    #-------------------------------------------------------------------------------
    def __init__(self, players):

        self.players = players
        self.scores = {}
        
        for p in players:
            self.scores[p['Id']] = -1

    # Sets the roster score for a player
    # player_id: the unique id for a player
    # score: a numeric value to assign for that player
    #-------------------------------------------------------------------------------
    def SetScore(self, player_id, score):

        try:
            self.scores[player_id] = score
        except:
            raise ValueError('player_id not in roster')

    # Retrieves the score for a player
    # player_id: the unique id for a player    
    #-------------------------------------------------------------------------------
    def GetScore(self, player_id):
        
        try:
            return self.scores[player_id]
        except:
            raise ValueError('player_id not in roster')

    # Retrieves the information dictionary for a player
    # player_id: the unique id for a player            
    #-------------------------------------------------------------------------------
    def GetPlayer(self, player_id):

        try:
            return self.players[player_id]
        except:
            raise ValueError('player_id not in roster')
            
    # Returns a list of all the player Id's in the roster
    #-------------------------------------------------------------------------------
    def GetIds(self):
        
        return self.players.keys()

    # Adds a player to the roster
    # player: A dictionary of information about a player
    #-------------------------------------------------------------------------------
    def AddPlayer(self, player):

        if not player['Id'] in self.players:
            self.players[player['Id']] = player
            self.scores[player['Id']] = -1
        else:
            raise ValueError('player already in roster')            

    # Removes the player from the roster
    # player_id: the unique id for a player            
    #-------------------------------------------------------------------------------
    def RemovePlayer(self, player_id):

        try:
            del players[player_id]
        except:
            raise ValueError('player_id not in roster')    

    # Checks if all the players have an associated score
    #-------------------------------------------------------------------------------
    def IsScored(self):

        for s in self.scores:
            if self.scores[s] = -1:
                return False
        else:
            return True
