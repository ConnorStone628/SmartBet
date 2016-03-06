################################################################################
# description: All scoring generators inherit this object to create a uniform
# interface. A new scoring generator shoudl override the "GenerateRoster"
# function.
# contributors: Connor Stone
# date: 06-03-2016
################################################################################

from roster_object import Roster

# Determines scores for all the given players and returns a Roster object with
# the scores.
#-------------------------------------------------------------------------------
class RosterGenerator(object):

    # Initializes the object with a list of players and constraint parameters
    # players: A dictionary of players for the day, indexed by their unique id
    # params: A dictionary of parameters to be used when determining the scores
    def __init__(self, players, params):

        self.roster = Roster(players)
        self.params = params

    # Analyzes the given players to determine their scores
    def GenerateRoster(self):

        return self.roster
