################################################################################
# description: Handles all calls to the database, this wraps all methods of
# calling for information or writting new information.
# contributors: Connor Stone
# Date: 29-02-2016
################################################################################

class Interface:

    def __init__(self, readonly = True):
        self.readonly = readonly
