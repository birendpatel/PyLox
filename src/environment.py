# Copyright (C) 2021 Biren Patel
# MIT License
# Environment data structure for associating variable names with their values.
# This is really just a tree of maps, where each map is capable of referencing
# back to its immediate parent environment. Since python doesn't have pointers,
# there's a bit of gymnastics involved.

from src.error import ErrorHandler, RuntimeError

class Environment():
    def __init__(self, parent):
        self.parent = parent
        self.map = {}

    def insert(self, key, val):
        """/
        insert a k-v pair into the environment. if the key already exists, the
        environment overrides the current value for global variables.
        """
        self.map[key] = val

    def search(self, key):
        """\
        access a k-v pair from the environment. if it does not exist, search
        the parent environments. if it does not exist in the entire environment
        chain, a runtime error is invoked.
        """
        try:
            return self.map[key]
            #todo: search parent environment
        except KeyError:
            raise RuntimeError
