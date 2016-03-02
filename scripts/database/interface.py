################################################################################
# description: Handles all calls to the database, this wraps all methods of
# calling for information or writting new information. The actual
# implimentation of the methods is written in the interface_methods folder.
# contributors: Connor Stone
# Date: 29-02-2016
################################################################################

class Interface:

    def __init__(self, readonly = True):
        self.readonly = readonly

    def Get(self, identifier):
        return 0

    def Write(self, identifier, data):
        return 0
