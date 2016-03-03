################################################################################
# Description: Provides a high level interface for all database methods.
# Authors: Connor Stone
# Date: 02-03-2016
################################################################################


class Database:

    def __init__(self, readonly = True):
        self.readonly = readonly
