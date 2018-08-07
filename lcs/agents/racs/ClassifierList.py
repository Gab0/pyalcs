from __future__ import annotations

from typing import Optional

from lcs import TypedList, Perception
from . import Classifier


class ClassifierList(TypedList):

    def __init__(self, *args) -> None:
        super().__init__((Classifier,), *args)

    def form_match_set(self, situation: Perception) -> ClassifierList:
        matching = [cl for cl in self if cl.condition.does_match(situation)]
        return ClassifierList(*matching)

    def form_action_set(self, action: int) -> ClassifierList:
        matching = [cl for cl in self if cl.action == action]
        return ClassifierList(*matching)

    def apply_alp(self,
                  previous_situation: Perception,
                  action: int,
                  situation: Perception,
                  time: int,
                  population: ClassifierList,
                  match_set: ClassifierList) -> None:

        new_list = ClassifierList()
        new_cl: Optional[Classifier] = None
        was_expected_case = False
        delete_counter = 0

        for cl in self:
            cl.increase_experience()
            cl.set_alp_timestamp(time)

            if cl.does_anticipate_correctly(previous_situation, situation):
                # new_cl = expected_case(cl, previous_situation, time)
                # TODO: continue from here
                pass
