# -*- coding: utf-8 -*-

"""Constants for BEL repositories."""

import json
from typing import Any, Mapping

from pybel import BELGraph, from_json_path, from_pickle, to_json_path, to_pickle

__all__ = [
    'IO_MAPPING',
    'OUTPUT_KWARGS',
    'LOCAL_SUMMARY_EXT',
    'to_summary_json',
]

LOCAL_SUMMARY_EXT = 'summary.json'


def to_summary_json_path(graph: BELGraph, path: str) -> None:
    """Write a summary JSON of the graph."""
    with open(path, 'w') as file:
        json.dump(to_summary_json(graph), file)


IO_MAPPING = {
    'json': (to_json_path, from_json_path),
    'pickle': (to_pickle, from_pickle),
    LOCAL_SUMMARY_EXT: (to_summary_json_path, None)
}

OUTPUT_KWARGS = {
    'json': dict(indent=2),
}


def to_summary_json(graph: BELGraph) -> Mapping[str, Any]:
    """Get a summary JSON of the graph."""
    rv = dict(
        Title=graph.name,
        Authors=graph.authors,
        **graph.summary_dict()
    )
    rv['Number of URL Namespaces'] = len(graph.namespace_url)
    rv['Number of Regex Namespaces'] = len(graph.namespace_pattern)
    rv['Number of URL Annotations'] = len(graph.annotation_url)
    rv['Number of Regex Annotations'] = len(graph.annotation_pattern)
    rv['Number of Local Annotations'] = len(graph.annotation_list)
    return rv
