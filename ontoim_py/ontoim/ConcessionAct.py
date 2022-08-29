from __future__ import annotations

from typing import TYPE_CHECKING, List

from ontopia_py.l0.Activity import Activity

from ..ns import *

if TYPE_CHECKING:
    from ontoim_py.ontoim.ConcessionActType import ConcessionActType
    from ontopia_py.cov.Organization import Organization
    from ontopia_py.l0.Agent import Agent
    from ontopia_py.ro.TimeIndexedRole import TimeIndexedRole
    from ontopia_py.transparency.TransparencyResource import \
        TransparencyResource
    from rdflib import Graph, Literal


class ConcessionAct(Activity):
    __type__ = ONTOIM["ConcessionAct"]

    hasActReferent: List[TimeIndexedRole] = None
    hasBeneficiary: List[Agent] = None
    hasConcessionActType: List[ConcessionActType] = None
    hasOrganization: List[Organization] = None
    hasTransparencyResource: List[TransparencyResource] = None
    actTitle: List[Literal] = None
    actDate: Literal = None
    actNumber: Literal = None
    paymentAmount: Literal = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.hasActReferent:
            for hasActReferent in self.hasActReferent:
                g.add(
                    (self.uriRef, ONTOIM["hasActReferent"], hasActReferent.uriRef))

        if self.hasBeneficiary:
            for hasBeneficiary in self.hasBeneficiary:
                g.add(
                    (self.uriRef, ONTOIM["hasBeneficiary"], hasBeneficiary.uriRef))

        if self.hasConcessionActType:
            for hasConcessionActType in self.hasConcessionActType:
                g.add(
                    (self.uriRef, ONTOIM["hasConcessionActType"], hasConcessionActType.uriRef))

        if self.hasOrganization:
            for hasOrganization in self.hasOrganization:
                g.add(
                    (self.uriRef, ONTOIM["hasOrganization"], hasOrganization.uriRef))

        if self.hasTransparencyResource:
            for hasTransparencyResource in self.hasTransparencyResource:
                g.add(
                    (self.uriRef, ONTOIM["hasTransparencyResource"], hasTransparencyResource.uriRef))
        
        if self.actTitle:
            for actTitle in self.actTitle:
                g.add((self.uriRef, ONTOIM["actTitle"], actTitle))

        if self.actDate:
            g.add((self.uriRef, ONTOIM["actDate"], self.actDate))

        if self.actNumber:
            g.add((self.uriRef, ONTOIM["actNumber"], self.actNumber))

        if self.paymentAmount:
            g.add((self.uriRef, ONTOIM["paymentAmount"], self.paymentAmount))