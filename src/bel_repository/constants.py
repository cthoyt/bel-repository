# -*- coding: utf-8 -*-

"""Constants for BEL repositories."""

from pybel import from_json_path, from_pickle, to_json_path, to_pickle

__all__ = [
    'IO_MAPPING',
    'OUTPUT_KWARGS',
]

IO_MAPPING = {
    'json': (to_json_path, from_json_path),
    'pickle': (to_pickle, from_pickle),
}

OUTPUT_KWARGS = {
    'json': dict(indent=2),
}
