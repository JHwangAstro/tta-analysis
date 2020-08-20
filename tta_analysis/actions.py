"""
"""

from typing import Union

import arcbound as ab
import attr


@attr.s(auto_attribs=True)
class SelectAction(object):
    ca: int
    card: str
    action: str = "select"


@attr.s(auto_attribs=True)
class ElectAction(object):
    card: str
    ca: int = 1
    action: str = "elect"


actions_to_obj = dict(
    select=SelectAction,
    elect=ElectAction
)


def create_action(action: str, *action_args):
    """
    """
    return actions_to_obj.get(action)(*action_args)


actions = (
    "discard",
    "aggress",
    "prepare",
    "reveal",
    "offer",
    "declare",
    "give",
    "take",
    "colonize",
    "cancel",
    "resign",

    "select",
    "elect",
    "play",
    "grow",
    "lose",
    "begin",
    "destroy",
    "finish",
    "build",
    "develop",
    "upgrade",
    "special",

    "revolution",
    "tactic",
    "adopt"
)

Action = Union[SelectAction]
