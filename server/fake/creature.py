from typing import List

from model.creature import Creature

_creatures = [
    Creature(
        name="Cloud Days",
        country="FR",
        area="home",
        description="맑음",
        aka="homme"
    ),
    Creature(
        name="Noad Shipper",
        country="DE",
        area="home",
        description="비오는날좋음",
        aka="homme"
    ),
]


# 3.9 이상만 가능..
def get_all() -> List[Creature]:
    return _creatures


def get_one(name: str) -> Creature:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature

    return None
