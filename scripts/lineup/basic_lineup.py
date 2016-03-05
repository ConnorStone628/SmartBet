################################################################################
# Description: Given the current day's roster, will determine a suitable
# lineup using only score and cost information. 
# Authors: Connor Stone
# Date: 04-03-2016
################################################################################

from lineup_generator_object import LineupGenerator
import numpy as np

# Creates a near optimal lineup based only on score and cost information
#-------------------------------------------------------------------------------
class BasicLineup(LineupGenerator):

    # Randomly searches to find groups that are acceptable and have high score
    #-------------------------------------------------------------------------------
    def GenerateLineup(self):

        ids = self.roster.GetIds()
        
        return self.lineup
