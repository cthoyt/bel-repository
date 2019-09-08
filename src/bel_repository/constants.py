# -*- coding: utf-8 -*-

"""Constants for BEL repositories."""

from pybel import from_nodelink_file, from_pickle, to_nodelink_file, to_pickle
from .utils import to_summary_json_path

__all__ = [
    'IO_MAPPING',
    'OUTPUT_KWARGS',
    'LOCAL_SUMMARY_EXT',
]

LOCAL_SUMMARY_EXT = 'summary.json'

IO_MAPPING = {
    'nodelink.json': (to_nodelink_file, from_nodelink_file),
    'pickle': (to_pickle, from_pickle),
    LOCAL_SUMMARY_EXT: (to_summary_json_path, None),
}

OUTPUT_KWARGS = {
    'nodelink.json': dict(indent=2, sort_keys=True),
}
