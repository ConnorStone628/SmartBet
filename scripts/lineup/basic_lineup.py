################################################################################
# Description: Given the current day's roster, will determine a suitable
# lineup using only score and cost information. 
# Authors: Connor Stone
# Date: 04-03-2016
################################################################################

from lineup_generator_object import LineupGenerator
from lineup_object import Lineup
from random import randint
from copy import deepcopy

# Creates a near optimal lineup based only on score and cost information
#-------------------------------------------------------------------------------
class BasicLineup(LineupGenerator):

    # Calls the lineup generator a few times and picks the best result
    #-------------------------------------------------------------------------------
    def GenerateLineup(self):

        currentbest = Lineup(self.positions)

        # calls the background lineup generator a few times and picks the best
        try:
            for i in range(10):
                print '.'
                self.lineup = Lineup(self.positions)
                newlineup = self._GenerateLineup()
                # Check which is better
                if newlineup.Score() >= currentbest.Score():
                    currentbest = newlineup
        # If you end it early, it will just take the best it has
        except KeyboardInterrupt:
            pass
        self.lineup = currentbest
        
        return currentbest
    
    # Randomly searches to find groups that are acceptable and have high score
    #-------------------------------------------------------------------------------
    def _GenerateLineup(self):
        
        # Numeric string elements, to be removed from position values
        numic = '0123456789'
        # Get the players in a dictionary indexed by position
        groups = self.roster.GetGroupedAttributes(None)
        # Get the budget or make it unlimited
        budget = self.params['Budget'] if 'Budget' in self.params else 1e1000

        # Randomly generate a lineup
        for p in self.positions:
            # Try as many random players as neccessary to get a unique player for each position 
            while not self.lineup.ChangePlayer(p, groups[p.strip(numic)][randint(0,len(groups[p.strip(numic)])-1)]): pass

        # Determine the number of itterations
        itter = self.params['Itter'] if 'Itter' in self.params else 10000

        # Randomly swap players and keep better combinations
        for i in range(itter):
            # Determine the score of the original lineup
            oldscore = 0 if self.lineup.Cost() > budget else self.lineup.Score()
            # Number of positions to be swapped
            ntoswap = (i % 4) + 2
            # Which positions to be swapped
            swaps = list(self.positions[randint(0,len(self.positions)-1)] for p in range(ntoswap))
            # Create a copy to manipulate
            new_lineup = deepcopy(self.lineup)

            # Make random swaps
            for p in swaps:
                while not new_lineup.ChangePlayer(p, groups[p.strip(numic)][randint(0,len(groups[p.strip(numic)])-1)]): pass

            # Determine the score of the new lineup
            newscore = 0 if new_lineup.Cost() > budget else new_lineup.Score()

            # Replace the lineup if the new one is better
            if newscore >= oldscore: self.lineup = new_lineup

        return self.lineup
