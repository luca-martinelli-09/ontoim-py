from __future__ import annotations

from typing import TYPE_CHECKING

from ..ns import *
from .InvolvedEntity import InvolvedEntity
from ontopia_py.cpv.Person import Person

if TYPE_CHECKING:
    from rdflib import Graph

    from .InvolvedPersonStatus import InvolvedPersonStatus


class InvolvedPerson(InvolvedEntity, Person):
    __type__ = ONTOIM["InvolvedPerson"]

    hasInvolvedPersonStatus: InvolvedPersonStatus = None

    def _addProperties(self, g: Graph):
        super(InvolvedEntity)._addProperties(g)
        super(Person)._addProperties(g)

        if self.hasInvolvedPersonStatus:
            g.add((self.uriRef, ONTOIM["hasInvolvedPersonStatus"],
                  self.hasInvolvedPersonStatus.uriRef))