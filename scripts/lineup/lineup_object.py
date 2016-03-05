################################################################################
# description: The object in this file is what should be returned by any
# lineup generator. It describes where each player is on the team.
# contributors: Connor Stone
# date: 22-12-2015
################################################################################

# stores information about a lineup
#-------------------------------------------------------------------------------
class Lineup(object):

    # initializes the lineup with a set of positions representing the layout for the game type
    # positions: List of unique strings representing the different positions (iterable of str)
    # initiallineup: dictionary indexed by the "positions" variable. Each element is a
    #     dictionary of information about that player (dictionary of dictionaries)
    # returns: nothing
    #-------------------------------------------------------------------------------
    def __init__(self, positions, initiallineup = None):

        self.positions = positions
        if initiallineup != None:
            self.players = initiallineup
        else:
            # initialize an empty playlist
            self.players = {}
            for p in positions:
                self.players[p] = None

    # Replaces the player at a given position
    # position: position to replace (str)
    # newplayer: all information about the new player (dictioary)
    # returns: 0 for success, 1 for failure
    #-------------------------------------------------------------------------------
    def ChangePlayer(self, position, newplayer):
        
        # reject if player is already in lineup
        for p in self.players:
            if self.players[p] == None:
                continue
            elif self.players[p]['Id'] == newplayer['Id']:
                raise ValueError('newplayer already on team')

        self.players[position] = newplayer
        
        return 0

    # used to access the information for the player at a given position
    # position: which player to look at (str)
    # returns: player information (dictionary)
    #-------------------------------------------------------------------------------
    def GetPlayer(self, position):
        
        return self.players[position]

    # Gives a copy of the lineup
    # returns: dictioary of players (dictioary of dictioaries)
    #-------------------------------------------------------------------------------
    def GetPlayers(self):
        
        return copy(self.players)

    # calculates the total score of the lineup
    # returns: total score
    #-------------------------------------------------------------------------------
    def Score(self):
        
        totalscore = 0
        
        # sum the score
        for p in self.players:
            totalscore += self.players[p]['Score']
            
        return totalscore

    # calculates the salary/cost of the team
    # returns: total cost
    #-------------------------------------------------------------------------------
    def Cost(self):

        totalcost = 0

        # sum the salary
        for p in self.players:
            totalcost += self.players[p]['Salary']
            
        return totalcost

    # produces a formatted string to show the lineup
    # returns: string to be printed
    #-------------------------------------------------------------------------------
    def __str__(self):
        
        output = ''

        # construct string of player names
        for p in self.players:
            if self.players[p] == None:
                continue
            output += p + ': ' + self.players[p]['First Name'] + ' ' + self.players[p]['Last Name'] + ', '

        output += '\nTotal salary: ' + str(self.Salary()) + '\n'
        output += 'Total Score: ' + str(self.Score()) + '\n'
        
        return output

    # determines if another lineup is the same
    # otherlineup: lineup object to be compared (lineup)
    # returns: True if equivalent, false otherwise
    #-------------------------------------------------------------------------------
    def __eq__(self, otherlineup):
        
        otherplayers = otherlineup.GetPlayers()

        # check for non equivalent players in each position
        for p in self.players:
            if self.players[p]['Id'] != otherplayers[p]['Id']:
                return False
                
        return True        
