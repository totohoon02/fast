from typing import List

from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Cloud Days",
        country="FR",
        description="맑음"
    ),
    Explorer(
        name="Noad Shipper",
        country="DE",
        description="비오는날좋음"
    ),
]


# 3.9 이상만 가능..
def get_all() -> List[Explorer]:
    return _explorers


def get_one(name: str) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer

    return None


