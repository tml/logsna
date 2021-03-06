###############################################################################
#
# Copyright (c) 2012 Ruslan Spivak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

__author__ = 'Ruslan Spivak <ruslan.spivak@gmail.com>'

import time
import logging

_DEFAULT_FMT = '%(levelname)-8s [%(asctime)s] %(name)s: %(message)s'


class Formatter(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None):
        super(Formatter, self).__init__(fmt or _DEFAULT_FMT, datefmt)
        # A user-configurable function to convert the creation time to a tuple.
        # It's used by Format.formatTime method and default is time.localtime()
        # We set it to convert time to a struct_time in UTC
        self.converter = time.gmtime

    def formatException(self, exc_info):
        text = super(Formatter, self).formatException(exc_info)
        # Prepend ! mark to every line
        text = '\n'.join(('! %s' % line) for line in text.splitlines())
        return text
