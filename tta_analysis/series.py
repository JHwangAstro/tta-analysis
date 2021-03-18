""" Defines the Series class used to analyze batches of games.
"""

import functools
import os
from typing import Dict, Tuple

import arcbound as ab
import attr
import pandas as pd
import plotnine

from tta_analysis.cards import camelcase_card_dict
from tta_analysis.game import Game


@ab.graph
@attr.s(auto_attribs=True, hash=False)
class Series(object):
    """ Combines the logs from many games and aggregates the results.

    Can either be instantiated with a tuple of explicitly defined paths to the
    game logs to be read or with a folder path, in which each .yaml file will
    be used to create a game.
    """
    game_files: Tuple[str, ...]
    base_dir: str = "./"
    player: str = "yellow"

    @classmethod
    def from_folder(cls, base_dir: str, **kwargs):
        """ Sets game files to all files in the base directory provided.
        """
        game_files = tuple(
            f
            for f in os.listdir(base_dir)
            if os.path.isfile(os.path.join(base_dir, f))
            if os.path.splitext(f)[1] == ".yaml"
        )

        return cls(game_files=game_files, base_dir=base_dir, **kwargs)

    ###########################################################################
    # Load game logs and create games.
    ###########################################################################

    @property
    @functools.lru_cache()
    @ab.auto_arcs()
    def games(
        self,
        game_files: Tuple[str, ...],
        base_dir: str,
        player: str
    ) -> Dict[str, Game]:
        """ Mapping of games to file name.
        """
        return {
            os.path.splitext(game_file)[0]: Game(
                game_file=game_file,
                base_dir=base_dir,
                player=player
            )
            for game_file in game_files
        }

    @ab.auto_arcs()
    def check_games(self, games: Dict[str, Game]) -> None:
        """ Checks that each game can be loaded properly. This functionality
        should be rewritten as error handling in tta_analyses.game.Game.

        Attempts to parse the log for each game.
        """
        for game in games.values():
            print(game.game_file)
            game.record_json.get("final_score")

        return None

    ###########################################################################
    # Aggregate data from games.
    ###########################################################################

    @property
    @ab.auto_arcs()
    def actions_df(self, games: Dict[str, Game]) -> pd.DataFrame:
        """ Dataframe of all actions taken across the series of games. 
        """
        return pd.DataFrame(
            (
                dict(
                    game=name,
                    round_number=turn.round_number,
                    age=turn.age,
                    card=action.card,
                    ca=action.ca,
                    action=action.action
                )
                for name, game in games.items()
                for turn in game.turns
                if turn.player_turn
                for action in turn.actions
            )
        )

    @property
    @ab.auto_arcs()
    def actions_grouped_df(self, actions_df: pd.DataFrame) -> pd.DataFrame:
        """ Aggregates counts and average CA's spent on each card across the
        series of games.
        """
        return (
            actions_df
            [actions_df.action=="select"]
            .assign(ca=lambda df: df.ca.apply(int))
            .groupby("card")
            .agg({"round_number": "size", "ca": "mean"})
            .reset_index()
            .rename({"round_number": "count"}, axis=1)
            .assign(
                age=lambda df: tuple(
                    card_obj.age if card_obj is not None else 0
                    for card in df.card
                    for card_obj in (camelcase_card_dict.get(card),)
                )
            )
            .assign(
                color=lambda df: tuple(
                    card_obj.color if card_obj is not None else 0
                    for card in df.card
                    for card_obj in (camelcase_card_dict.get(card),)
                )
            )
            .assign(
                line=lambda df: tuple(
                    card_obj.line if card_obj is not None else 0
                    for card in df.card
                    for card_obj in (camelcase_card_dict.get(card),)
                )
            )
        )

    @property
    @ab.auto_arcs()
    def card_selection_df(
        self,
        actions_grouped_df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        """
        return (
            actions_grouped_df
            [
                (actions_grouped_df["count"] > 0)
                & (actions_grouped_df["color"] != 0)
            ]
            .sort_values(["color", "line", "age", "count"])
            [["color", "line", "card", "age", "count", "ca"]]
        )

    @property
    @ab.auto_arcs()
    def series_state_df(self, games: Dict[str, Game]) -> pd.DataFrame:
        """
        """
        return pd.concat(
            game.state_df
            .assign(game_name=name)
            .assign(game_id=i)
            for i, (name, game) in enumerate(games.items())
        )

    @ab.arcs(series_state_df="series_state_df")
    def plot_series(
        self,
        y: str,
        series_state_df: pd.DataFrame
    ) -> plotnine.ggplot:
        """
        """
        aes_kwargs = dict(
            x="round_number",
            y=y,
            color="factor(game_id)",
            group="factor(game_id)"
        )

        return (
            plotnine.ggplot(series_state_df)
            + plotnine.aes(**aes_kwargs)
            + plotnine.geom_point()
            + plotnine.geom_line()
            + plotnine.theme_light()
            + plotnine.scale_x_continuous(breaks=range(1, 20, 1))
        )
