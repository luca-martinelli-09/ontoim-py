from __future__ import annotations

from typing import TYPE_CHECKING, Union

from ontopia_py.l0.Activity import Activity

from ..ns import *

if TYPE_CHECKING:
    from ontopia_py.clv.SpatialObject import SpatialObject
    from ontopia_py.cpv.Family import Family
    from ontopia_py.cpv.Person import Person
    from ontopia_py.ti.TemporalEntity import TemporalEntity
    from rdflib import Graph, Literal


class DemographicObservation(Activity):
    __type__ = ONTOIM["DemographicObservation"]

    hasTemporalEntity: TemporalEntity = None
    hasDemographicReference: Union(Person, Family) = None
    hasSpatialDelimitation: SpatialObject = None
    observationValue: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasTemporalEntity:
            g.add(
                (self.uriRef, ONTOIM["hasTemporalEntity"], self.hasTemporalEntity.uriRef))

        if self.hasDemographicReference:
            g.add((self.uriRef, ONTOIM["hasDemographicReference"],
                  self.hasDemographicReference.uriRef))

        if self.hasSpatialDelimitation:
            g.add(
                (self.uriRef, ONTOIM["hasSpatialDelimitation"], self.hasSpatialDelimitation.uriRef))

        if self.observationValue:
            g.add(
                (self.uriRef, ONTOIM["observationValue"], self.observationValue))
