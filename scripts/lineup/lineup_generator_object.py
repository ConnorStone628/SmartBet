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
    # parameters: a dictionary object that contains all the information which
    #    limits the allowable lineup choices. For example, the 'Budget' item
    #    is the maximum total salary allowed.
    #-------------------------------------------------------------------------------
    def __init__(self, roster, positions, params):

        self.roster = roster
        self.positions = positions
        self.params = params
        self.lineup = Lineup(positions)

        # Check that the roster and positions objects do not conflict
        player_positions = []
        for i in self.roster.GetIds():
            player_positions.append(self.roster.GetPlayer(i)['Position'])
            
        if len(set(player_positions).symmetric_difference(set(p.strip('0123456789') for p in positions))) != 0:
            raise ValueError('Roster and positions objects do not have the same positions.')
        
    # Analyzes the roster to create a lineup
    #-------------------------------------------------------------------------------
    def GenerateLineup(self):

        return self.lineup

    # Returns the roster object
    #-------------------------------------------------------------------------------
    def GetRoster(self):

        return self.roster

    # Returns the parameter dictionary
    #-------------------------------------------------------------------------------
    def GetParams(self):

        return self.params

    # Returns the current lineup
    #-------------------------------------------------------------------------------        
    def GetLineup(self):

        return self.lineup
