################################################################################
# description: Creates a roster by giving each player their average score.
# contributors: Connor Stone
# date: 06-03-2016
################################################################################

from roster_generator_object import RosterGenerator

# Gives a score to all the players in a given day
#-------------------------------------------------------------------------------
class BasicScoring(RosterGenerator):

    # Set the roster score as the average score
    #-------------------------------------------------------------------------------
    def GenerateRoster(self):

        for p in self.roster.GetIds():
            self.roster.SetScore(p, self.roster.GetPlayer(p)['Score'])

        return self.roster
