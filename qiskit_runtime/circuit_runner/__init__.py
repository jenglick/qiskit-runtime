# This code is part of qiskit-runtime.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Qiskit circuit runner module
============================

.. currentmodule:: qiskit_runtime.circuit_runner

Result class
--------------

.. autosummary::
   :toctree: ../stubs/

    RunnerResult

Distributions
-------------

.. autosummary::
   :toctree: ../stubs/

    ProbDistribution
    QuasiDistribution
"""

from .result import RunnerResult
from .probability import ProbDistribution
from .quasi import QuasiDistribution
