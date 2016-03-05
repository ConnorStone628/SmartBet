################################################################################
# Description: All lineup generators inherit this object so as to create a
# uniform interface. A new lineup generator will override the "GenerateLineup"
# function in this object.
# Authors: Connor Stone
# Date: 02-03-2016
################################################################################

from lineup_object import Lineup

# Base class for all lineup generators, which attempt to form the highest
# scoring team possible.
#-------------------------------------------------------------------------------
class LineupGenerator(object):

    # Initialize the generator
    # roster: a roster object which contains a dictionary of players and scores
    # positions: A list of strings identifying the positions in a lineup
    # constraints: a dictionary object that contains all the information which
    #    limits the allowable lineup choices.
    #-------------------------------------------------------------------------------
    def __init__(self, roster, positions, constraints):

        self.roster = roster
        self.constraints = constraints
        self.lineup = Lineup(positions)
        
    # Analyzes the roster to create a lineup
    #-------------------------------------------------------------------------------
    def GenerateLineup(self):

        return self.lineup

    # Replace the current roster with a new one
    # roster: a roster object which contains a dictionary of players and scores    
    #-------------------------------------------------------------------------------
    def SetRoster(self, roster):

        self.roster = roster

    # Replace the current constraints with a new set
    # constraints: a dictionary object that contains all the information which
    #    limits the allowable lineup choices.
    #-------------------------------------------------------------------------------
    def SetConstraints(self, constraints):

        self.constraints = constraints

    # Returns the current roster object
    #-------------------------------------------------------------------------------
    def GetRoster(self):

        return self.roster

    # Returns the current constraint dictionary
    #-------------------------------------------------------------------------------
    def GetConstraints(self):

        return self.constraints
