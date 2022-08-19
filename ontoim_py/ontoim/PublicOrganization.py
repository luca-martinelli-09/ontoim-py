from __future__ import annotations

from ontopia_py.cov.PublicOrganization import PublicOrganization

from ..ns import *
from .Organization import Organization


class PublicOrganization(Organization, PublicOrganization):
    __type__ = ONTOIM["PublicOrganization"]
