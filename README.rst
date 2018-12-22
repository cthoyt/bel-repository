BEL Repository |build|
======================
A utility for loading data from repositories of BEL documents with PyBEL [1]_.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bel_repository`` can be installed from PyPI with the following command:

.. code-block:: bash

   $ pip install bel_repository

The latest version can be installed from GitHub with:

.. code-block:: bash

   $ pip install git+https://github.com/cthoyt/bel-repository.git

Usage
-----
.. code-block:: python

    from bel_repository import BELRepository
    path = '/path/to/folder/with/bel/'
    r = BELRepository(path)
    graphs = r.get_graphs()


References
----------
.. [1] Hoyt, C. T., *et al.* (2017). `PyBEL: a computational framework for Biological Expression
       Language <https://doi.org/10.1093/bioinformatics/btx660>`_. Bioinformatics (Oxford, England), 34(4), 703–704.

.. |build| image:: https://travis-ci.com/cthoyt/bel-repository.svg?branch=master
    :target: https://travis-ci.com/cthoyt/bel-repository

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bel_repository.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/bel_repository.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/bel_repository.svg
    :alt: License