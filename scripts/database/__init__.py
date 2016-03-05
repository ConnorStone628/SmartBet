################################################################################
# Description: Provides a high level interface for all database methods.
# Authors: Connor Stone
# Date: 02-03-2016
################################################################################

from interface_methods import get as _get
from interface_methods import write as _write


class Database:

    def __init__(self, location, readonly = True):
        self.location = location
        self.readonly = readonly

    # Retrieve information from the database
    def Get(*args, **kwargs):
        return _get(*args, **kwargs)

    # Write information to the database
    def Write(*args, **kwargs):
        return _Write(*args, **kwargs)
