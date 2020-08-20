"""
"""

from typing import Tuple, Union

import arcbound as ab
import attr

from .actions import Action, create_action, actions_to_obj


@attr.s(auto_attribs=True)
class Income(object):
    """ Player income at end of turn.
    """
    food: int
    rock: int
    science: int
    culture: int


@attr.s(auto_attribs=True)
class Resources(object):
    """ Player resources at end of turn.
    """
    food: int
    rock: int
    science: int
    culture: int


@attr.s(auto_attribs=True)
class Population(object):
    """ Player population distribution at end of turn.
    """
    employed: int
    idle: int
    bank: int


@attr.s(auto_attribs=True, hash=False)
class PlayerTurn(object):
    """ Defines a player's turn from a provided log.
    """
    round_number: int
    age: int
    log: dict
    player: str

    @property
    def player_turn(self) -> bool:
        """ Identifies if the turn is a player turn as opposed to an opponent
        turn. Player turns have more detail.
        """
        return True

    @property
    @ab.auto_arcs()
    def income(self, log: dict) -> Income:
        """ Player income at end of turn.
        """
        income_log = log.get("income")

        return (
            Income(*income_log) if income_log is not None else
            None
        )

    @property
    @ab.auto_arcs()
    def resources(self, log: dict) -> Resources:
        """ Player resources at end of turn.
        """
        return Resources(*log.get("resources"))

    @property
    @ab.auto_arcs()
    def population(self, log: dict) -> Population:
        """ Player population distribution at end of turn.
        """
        return Population(*log.get("population"))

    @property
    @ab.auto_arcs()
    def strength(self, log: dict) -> int:
        """ Player strength at end of turn.
        """
        return log.get("strength")

    @property
    @ab.auto_arcs()
    def draws(self, log: dict) -> int:
        """ Number of event cards drawn at end of turn.
        """
        return log.get("draw")

    @property
    @ab.auto_arcs()
    def actions(self, log: dict) -> Tuple[Action, ...]:
        """ Actions taken during the turn, and results of events from the
        previous turn to the start of this turn.
        """
        if log.get("actions") is not None:
            actions = tuple(
                create_action(action, *action_args)
                if isinstance(action_args, list) else
                create_action(action, action_args)
                for action_args in log.get("actions", ({},))
                if action_args is not None
                for action, action_args in action_args.items()
                if action in actions_to_obj
                # if k not in {"income", "resources", "population", "strength", "draw"}
            )

        else:
            actions = ()

        return actions


@attr.s(auto_attribs=True, hash=False)
class OpponentTurn(object):
    """
    """
    round_number: int
    age: int
    player: str

    @property
    def player_turn(self) -> bool:
        """ Identifies if the turn is a player turn as opposed to an opponent
        turn. Player turns have more detail.
        """
        return False


TurnType = Union[PlayerTurn, OpponentTurn]
