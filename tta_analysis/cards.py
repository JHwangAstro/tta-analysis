""" Defines card properties.
"""

from typing import Tuple

import attr


@attr.s(auto_attribs=True)
class Card(object):
    name: str
    line: str
    color: str
    age: int
    rock: int = 0
    science: int = 0
    income: dict = attr.Factory(dict)
    resources: dict = attr.Factory(dict)
    happiness: int = 0
    strength: int = 0
    ca: int = 0
    ma: int = 0
    yellow: int = 0
    blue: int = 0
    colonization: int = 0


###############################################################################
# Production buildings.
###############################################################################

# Farms
agriculture = Card(
    name="agriculture",
    line="farm",
    color="brown",
    age=0,
    rock=2,
    science=0,
    income=dict(food=1)
)

irrigation = Card(
    name="irrigation",
    line="farm",
    color="brown",
    age=1,
    rock=4,
    science=3,
    income=dict(food=2)
)

selective_breeding = Card(
    name="selective_breeding",
    line="farm",
    color="brown",
    age=2,
    rock=6,
    science=5,
    income=dict(food=3)
)

mechanized_agriculture = Card(
    name="mechanized_agriculture",
    line="farm",
    color="brown",
    age=3,
    rock=8,
    science=7,
    income=dict(food=5)
)

# Mines
bronze = Card(
    name="bronze",
    line="mine",
    color="brown",
    age=0,
    rock=2,
    science=0,
    income=dict(rock=1)
)

iron = Card(
    name="iron",
    line="mine",
    color="brown",
    age=1,
    rock=5,
    science=5,
    income=dict(rock=2)
)

coal = Card(
    name="coal",
    line="mine",
    color="brown",
    age=2,
    rock=8,
    science=7,
    income=dict(rock=3)
)

oil = Card(
    name="oil",
    line="mine",
    color="brown",
    age=3,
    rock=11,
    science=9,
    income=dict(rock=5)
)

###############################################################################
# Urban buildings.
###############################################################################

# Labs
philosophy = Card(
    name="philosophy",
    line="lab",
    color="grey",
    age=0,
    rock=3,
    science=0,
    income=dict(science=1)
)

alchemy = Card(
    name="alchemy",
    line="lab",
    color="grey",
    age=1,
    rock=6,
    science=4,
    income=dict(science=2)
)

scientific_method = Card(
    name="scientific_method",
    line="lab",
    color="grey",
    age=2,
    rock=8,
    science=6,
    income=dict(science=3)
)

computers = Card(
    name="computers",
    line="lab",
    color="grey",
    age=3,
    rock=11,
    science=8,
    income=dict(science=5)
)

# Libraries
religion = Card(
    name="religion",
    line="temple",
    color="grey",
    age=0,
    rock=3,
    science=0,
    income=dict(culture=1),
    happiness=1
)

theology = Card(
    name="theology",
    line="temple",
    color="grey",
    age=1,
    rock=5,
    science=3,
    income=dict(culture=1),
    happiness=2
)

organized_religion = Card(
    name="organized_religion",
    line="temple",
    color="grey",
    age=2,
    rock=7,
    science=4,
    income=dict(culture=1),
    happiness=3
)

# Libraries
printing_press = Card(
    name="printing_press",
    line="library",
    color="grey",
    age=1,
    rock=3,
    science=3,
    income=dict(science=1, culture=1)
)

journalism = Card(
    name="journalism",
    line="library",
    color="grey",
    age=2,
    rock=8,
    science=6,
    income=dict(science=2, culture=2)
)

multimedia = Card(
    name="multimedia",
    line="library",
    color="grey",
    age=3,
    rock=11,
    science=9,
    income=dict(science=3, culture=3)
)

# Theaters
drama = Card(
    name="drama",
    line="theater",
    color="grey",
    age=1,
    rock=4,
    science=3,
    income=dict(culture=2),
    happiness=1
)

opera = Card(
    name="opera",
    line="theater",
    color="grey",
    age=2,
    rock=8,
    science=7,
    income=dict(culture=2),
    happiness=1
)

movies = Card(
    name="movies",
    line="theater",
    color="grey",
    age=3,
    rock=11,
    science=10,
    income=dict(culture=4),
    happiness=1
)

# Arenas
bread_and_circuses = Card(
    name="bread_and_circuses",
    line="arena",
    color="grey",
    age=1,
    rock=3,
    science=3,
    happiness=2,
    strength=1
)

team_sports = Card(
    name="team_sports",
    line="arena",
    color="grey",
    age=2,
    rock=5,
    science=5,
    happiness=3,
    strength=2
)

professional_sports = Card(
    name="professional_sports",
    line="arena",
    color="grey",
    age=3,
    rock=7,
    science=7,
    happiness=4,
    strength=4
)

###############################################################################
# Military.
###############################################################################

# Infantry
warriors = Card(
    name="warriors",
    line="infantry",
    color="red",
    age=0,
    rock=2,
    science=0,
    strength=1
)

swordsmen = Card(
    name="swordsmen",
    line="infantry",
    color="red",
    age=1,
    rock=3,
    science=4,
    strength=2
)

riflemen = Card(
    name="riflemen",
    line="infantry",
    color="red",
    age=2,
    rock=5,
    science=6,
    strength=3
)

modern_infantry = Card(
    name="modern_infantry",
    line="infantry",
    color="red",
    age=3,
    rock=7,
    science=10,
    strength=5
)

# Cavalry
knights = Card(
    name="knights",
    line="cavalry",
    color="red",
    age=1,
    rock=3,
    science=5,
    strength=2
)

cavalrymen = Card(
    name="cavalrymen",
    line="cavalry",
    color="red",
    age=2,
    rock=5,
    science=6,
    strength=3
)

tanks = Card(
    name="tanks",
    line="cavalry",
    color="red",
    age=3,
    rock=7,
    science=9,
    strength=5
)

# Artillery
cannon = Card(
    name="cannon",
    line="artillery",
    color="red",
    age=2,
    rock=5,
    science=6,
    strength=3
)

rockets = Card(
    name="rockets",
    line="artillery",
    color="red",
    age=3,
    rock=7,
    science=8,
    strength=5
)

# Air Forces
air_forces = Card(
    name="air_forces",
    line="air_forces",
    color="red",
    age=3,
    rock=7,
    science=12,
    strength=5
)

###############################################################################
# Progress
###############################################################################

# Civil
code_of_laws = Card(
    name="code_of_laws",
    line="civil",
    color="blue",
    age=1,
    science=6,
    ca=1
)

justice_system = Card(
    name="justice_system",
    line="civil",
    color="blue",
    age=2,
    science=7,
    ca=1,
    blue=3
)

civil_service = Card(
    name="civil_service",
    line="civil",
    color="blue",
    age=3,
    science=10,
    ca=2
)

# Civil
warfare = Card(
    name="warfare",
    line="military",
    color="blue",
    age=1,
    science=5,
    ma=1,
    strength=1
)

strategy = Card(
    name="strategy",
    line="military",
    color="blue",
    age=2,
    science=8,
    ma=2,
    strength=3
)

military_theory = Card(
    name="military_theory",
    line="military",
    color="blue",
    age=3,
    science=11,
    ma=3,
    strength=5
)

# Colonization
cartography = Card(
    name="cartography",
    line="colonization",
    color="blue",
    age=1,
    science=4,
    strength=1,
    colonization=2
)

navigation = Card(
    name="navigation",
    line="colonization",
    color="blue",
    age=2,
    science=6,
    strength=2,
    colonization=3
)

satellites = Card(
    name="satellites",
    line="colonization",
    color="blue",
    age=3,
    science=8,
    strength=3,
    colonization=4
)


@attr.s(auto_attribs=True)
class ConstructionCard(Card):
    line: str = "construction"
    color: str = "blue"
    urban_discount: Tuple[int, int, int, int] = ()
    wonder_steps: int = 1


masonry = ConstructionCard(
    name="masonry",
    age=1,
    science=3,
    urban_discount=(0, 1, 1, 1),
    wonder_steps=2
)

architecture = ConstructionCard(
    name="architecture",
    age=2,
    science=6,
    urban_discount=(0, 1, 2, 2),
    wonder_steps=3
)

engineering = ConstructionCard(
    name="engineering",
    age=3,
    science=9,
    urban_discount=(0, 1, 2, 3),
    wonder_steps=4
)


@attr.s(auto_attribs=True)
class GovernmentCard(Card):
    line: str = "government"
    color: str = "orange"
    revolution_cost: int = 0


monarchy = GovernmentCard(
    name="monarchy",
    age=1,
    science=8,
    ca=5,
    ma=3,
    revolution_cost=2
)

theocracy = GovernmentCard(
    name="theocracy",
    age=1,
    science=6,
    ca=4,
    ma=3,
    strength=1,
    happiness=1,
    revolution_cost=1
)

constitutional_monarchy = GovernmentCard(
    name="constitutional_monarchy",
    age=2,
    science=12,
    ca=6,
    ma=4,
    revolution_cost=6
)

republic = GovernmentCard(
    name="republic",
    age=2,
    science=11,
    ca=7,
    ma=2,
    revolution_cost=2
)

democracy = GovernmentCard(
    name="democracy",
    age=3,
    science=17,
    income=dict(culture=3),
    ca=7,
    ma=3,
    revolution_cost=9
)

communism = GovernmentCard(
    name="communism",
    age=3,
    science=18,
    income=dict(rock=1),
    happiness=-1,
    ca=7,
    ma=5,
    revolution_cost=1
)

fundamentalism = GovernmentCard(
    name="fundamentalism",
    age=3,
    science=16,
    income=dict(science=-2),
    strength=5,
    ca=6,
    ma=5,
    revolution_cost=5
)

card_dict = {
    card.name: card
    for card in (
        agriculture,
        irrigation,
        selective_breeding,
        mechanized_agriculture,
        bronze,
        iron,
        coal,
        oil,

        philosophy,
        alchemy,
        scientific_method,
        computers,
        religion,
        theology,
        organized_religion,
        printing_press,
        journalism,
        multimedia,
        drama,
        opera,
        movies,
        bread_and_circuses,
        team_sports,
        professional_sports,

        warriors,
        swordsmen,
        riflemen,
        modern_infantry,
        knights,
        cavalrymen,
        tanks,
        cannon,
        rockets,
        air_forces,

        code_of_laws,
        justice_system,
        civil_service,
        warfare,
        strategy,
        military_theory,
        cartography,
        navigation,
        satellites,
        masonry,
        architecture,
        engineering,

        monarchy,
        theocracy,
        constitutional_monarchy,
        republic,
        democracy,
        communism,
        fundamentalism
    )
}


def snake_to_camel(s: str) -> str:
    """ Converts a string from snake case to CamelCase.
    """
    split_str = s.split("_")

    return "".join(
        (
            "".join([first_letter.upper()] + other_letters)
            for blob in split_str
            for first_letter, *other_letters in (blob,)
        )
    )


camelcase_card_dict = {
    snake_to_camel(name): card
    for name, card in card_dict.items()
}
