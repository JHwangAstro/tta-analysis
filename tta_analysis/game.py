""" The Game object reads in a single game's logs and recreates each round's
game state.
"""

import collections
import functools
import os
from typing import Callable, Tuple, TypeVar

import arcbound as ab
import attr
import pandas as pd
import plotnine
import yaml

from .actions import actions
from .turn import PlayerTurn, OpponentTurn, TurnType

RecordType = TypeVar("RecordType")
RoundRecordsType = TypeVar("RoundRecordsType")

AgeChange = collections.namedtuple("AgeChange", ("round", "turn"))


@ab.graph
@attr.s(auto_attribs=True, hash=False)
class Game(object):
    """ Reads in a single game's logs and recreates each round's game state.

    Input parameters:
        game_file: YAML file containing the game logs.
        base_dir: Directory containing finished game logs.
        player: Player color in the game.

    Properties:
        record_json: JSON of the game logs.

    Methods:
    """
    game_file: str
    base_dir: str = "./"
    player: str = "yellow"

    ###########################################################################
    # Parse the data and generate turn objects.
    ###########################################################################

    @property
    @ab.auto_arcs()
    def record_json(self, game_file: str, base_dir: str) -> RecordType:
        """ JSON summarizing the game logs. The actions are cast to a list of
        dictionaries.
        """
        colors = ("yellow", "green", "blue", "red")

        tab = "    "

        with open(os.path.join(base_dir, game_file)) as f:
            initial_data = functools.reduce(
                lambda data, color: (
                    data
                    .replace(f"{color}:", f"{color}:\n{tab}{tab}actions:")
                ),
                colors,
                f.read()
            )

            data = functools.reduce(
                lambda data, action: (
                    data.replace(f" {action}", f" {tab}- {action}")
                ),
                actions,
                initial_data
            )

            record = yaml.safe_load(data)

        return record

    @property
    @functools.lru_cache()
    @ab.auto_arcs()
    def round_records(self, record_json: RecordType) -> RoundRecordsType:
        """
        """
        return {k: v for k, v in record_json.items() if "round" in k}

    @property
    @ab.auto_arcs()
    def age_changes(
        self,
        round_records: RoundRecordsType
    ) -> Tuple[Tuple[int, AgeChange], ...]:
        """ Round and turn of age changes.
        """
        initial_age = AgeChange(1, 0)

        age_changes = (
            (initial_age,)
            + tuple(
                AgeChange(i + 1, j)
                for i, round_log in enumerate(round_records.values())
                for j, key in enumerate(round_log)
                if key == "age"
            )
        )

        return tuple(enumerate(age_changes))[::-1]

    @property
    @ab.auto_arcs()
    def game_length(self, round_records: RoundRecordsType) -> int:
        """ Number of rounds the game lasted.
        """
        return max(
            int(round_number.split("_")[-1])
            for round_number in round_records
        )

    @ab.arcs(age_changes="age_changes")
    def get_age(
        self,
        round_number: int,
        turn: int,
        age_changes: Tuple[AgeChange, ...]
    ) -> int:
        """ Returns the age the turn was taken on.

        Arguments:
            round_number: Round the turn was taken in.
            turn: Turn number within the round.
            age_changes: Age changes in the game.
        """
        return next(
            age
            for age, (age_round, age_turn) in age_changes
            if (
                (age_round < round_number + 1)
                | (age_round == round_number + 1) & (turn >= age_turn)
            )
        )

    @property
    @functools.lru_cache()
    @ab.arcs(
        player="player",
        round_records="round_records",
        get_age=ab.Arc("get_age", tag_only=True)
    )
    def turns(
        self,
        player: str,
        round_records: RoundRecordsType,
        # get_age: Callable[[int, int], int]
    ) -> Tuple[TurnType, ...]:
        """
        """
        return tuple(
            PlayerTurn(
                round_number=int(round_n.split("_")[-1]),
                age=self.get_age(i, j),
                log=actions,
                player=key
            )
            if key == player else
            OpponentTurn(
                round_number=int(round_n.split("_")[-1]),
                age=self.get_age(i, j),
                player=key
            )
            for i, (round_n, round_log) in enumerate(round_records.items())
            for j, (key, actions) in enumerate(round_log.items())
            if key != "age"
        )

    ###########################################################################
    # Transform the data into tables and plot.
    ###########################################################################

    @property
    @ab.auto_arcs()
    def state_df(self, turns: Tuple[TurnType, ...]) -> pd.DataFrame:
        """ Converts the turn data into a tabular format (pandas) for use in
        analysis and plotting.
        """
        return pd.DataFrame(
            (
                dict(
                    round_number=turn.round_number,
                    **attr.asdict(turn.income),
                    strength=turn.strength,
                    **attr.asdict(turn.population)
                )
                for turn in turns
                if turn.player_turn
                if turn.income is not None
            )
        )

    def create_state_plot(
        self,
        x: str,
        y: str,
        data: pd.DataFrame,
        aes_kwargs: Tuple[str, str] = None
    ) -> plotnine.ggplot:
        """
        """
        aes_kwargs = ({} if aes_kwargs is None else aes_kwargs)

        x_breaks = data[x]

        max_y = max(data[y])
        y_interval = int(max_y/20) + 1
        y_breaks = range(0, max_y + 1, y_interval)

        return (
            plotnine.ggplot(data)
            + plotnine.aes(x=x, y=y, **aes_kwargs)
            + plotnine.geom_line()
            + plotnine.geom_point()
            + plotnine.theme_light()
            + plotnine.scale_x_continuous(breaks=x_breaks)
            + plotnine.scale_y_continuous(breaks=y_breaks)
        )

    @property
    @ab.auto_arcs()
    def income_plot(
        self,
        state_df: pd.DataFrame,
        create_state_plot: Callable
    ) -> plotnine.ggplot:
        """
        """
        data = pd.melt(
            frame=state_df,
            id_vars=("round_number",),
            value_vars=("food", "rock", "science", "culture"),
            var_name="resource",
            value_name="value"
        ).sort_values("round_number")

        aes_kwargs = dict(color="resource", group="resource")

        return create_state_plot(
            x="round_number",
            y="value",
            data=data,
            aes_kwargs=aes_kwargs
        )

    @property
    @ab.auto_arcs()
    def strength_plot(
        self,
        state_df: pd.DataFrame,
        create_state_plot: Callable
    ) -> plotnine.ggplot:
        """
        """
        return create_state_plot(x="round_number", y="strength", data=state_df)

    @property
    @ab.auto_arcs()
    def population_plot(
        self,
        state_df: pd.DataFrame,
        create_state_plot: Callable
    ) -> plotnine.ggplot:
        """
        """
        data = pd.melt(
            frame=state_df,
            id_vars=("round_number",),
            value_vars=("employed", "idle", "bank"),
            var_name="population_type",
            value_name="population"
        ).sort_values("round_number")

        aes_kwargs = dict(
            color="population_type",
            group="population_type"
        )

        return create_state_plot(
            x="round_number",
            y="population",
            data=data,
            aes_kwargs=aes_kwargs
        )
