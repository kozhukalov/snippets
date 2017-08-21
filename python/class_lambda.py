#!/usr/bin/env python


class A(object):

    a = lambda self: self.b()

    def __init__(self):
        self.b = lambda self: None
