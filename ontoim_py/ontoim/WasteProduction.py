from __future__ import annotations

from typing import TYPE_CHECKING, List

from ontopia_py.l0.Activity import Activity

from ..ns import *

if TYPE_CHECKING:
    from ontopia_py.clv.SpatialObject import SpatialObject
    from ontopia_py.mu.Value import Value
    from ontopia_py.ti.TemporalEntity import TemporalEntity
    from rdflib import Graph

    from .WasteCategory import WasteCategory


class WasteProduction(Activity):
    __type__ = ONTOIM["WasteProduction"]

    hasValue: List[Value] = None
    hasTemporalEntity: TemporalEntity = None
    hasSpatialDelimitation: SpatialObject = None
    hasWasteCategory: WasteCategory = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasValue:
            for hasValue in self.hasValue:
                g.add((self.uriRef, MU["hasValue"], hasValue.uriRef))

        if self.hasTemporalEntity:
            g.add(
                (self.uriRef, TI["hasTemporalEntity"], self.hasTemporalEntity.uriRef))

        if self.hasSpatialDelimitation:
            g.add(
                (self.uriRef, ONTOIM["hasSpatialDelimitation"], self.hasSpatialDelimitation.uriRef))

        if self.hasWasteCategory:
            g.add(
                (self.uriRef, ONTOIM["hasWasteCategory"], self.hasWasteCategory.uriRef))
