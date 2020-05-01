# -*- coding: utf-8 -*-

"""Version information for :mod:`bel-repository`."""

__all__ = [
    'VERSION',
    'get_version',
]

VERSION = '0.1.3-dev'


def get_version() -> str:
    """Get the software version of :mod:`bel-repository`."""
    return VERSION
