"""
This file is part of Ludolph: Doorman plugin

See the LICENSE file for copying permission.
"""
import time
from doorman.doorman import Doorman

#from ludolph_doorman import __version__
from ludolph.command import CommandError, command
from ludolph.plugins.plugin import LudolphPlugin


class LudolphDoorman(LudolphPlugin):
    """
    Ludolph: Doorman, plugin commands.
    """
#    __version__ = __version__

    # noinspection PyUnusedLocal
    @command
    def door_state(self, msg):
        """
        Door state.

        Usage: door-state
        """
        d = Doorman()
        return 'Door state is %s' % d.door_state