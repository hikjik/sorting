# 69988836

import random
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any, List, MutableSequence, Optional, TypeVar


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


def quick_sort(
    array: MutableSequence[CT],
    start: int = 0,
    end: Optional[int] = None,
) -> None:
    if end is None:
        end = len(array) - 1

    if start >= end:
        return

    i, j = start, end
    pivot = array[random.randint(start, end)]
    while i <= j:
        while array[i] < pivot:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort(array, start, j)
    quick_sort(array, i, end)


@dataclass
class Competitor(Comparable):
    name: str
    solved_tasks: int
    penalty: int

    def __lt__(self, other: "Competitor") -> bool:
        if self.solved_tasks != other.solved_tasks:
            return self.solved_tasks > other.solved_tasks
        if self.penalty != other.penalty:
            return self.penalty < other.penalty
        return self.name < other.name


def read_input() -> List[Competitor]:
    count = int(input())
    competitors: List[Competitor] = []
    for _ in range(count):
        name, solved_tasks, penalty = input().split()
        competitors.append(
            Competitor(
                name=name,
                solved_tasks=int(solved_tasks),
                penalty=int(penalty),
            )
        )
    return competitors


def print_output(competitors: List[Competitor]) -> None:
    for competitor in competitors:
        print(competitor.name)


if __name__ == "__main__":
    competitors = read_input()
    quick_sort(competitors)
    print_output(competitors)
