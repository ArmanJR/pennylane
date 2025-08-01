# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""
This module contains optimizers for the standard :mod:`QNode` class, which uses the NumPy interface.
"""

# Python optimizers that are available in PennyLane
# listed in alphabetical order to avoid circular imports
from .adagrad import AdagradOptimizer
from .adam import AdamOptimizer
from .adaptive import AdaptiveOptimizer
from .gradient_descent import GradientDescentOptimizer
from .momentum import MomentumOptimizer
from .momentum_qng import MomentumQNGOptimizer
from .nesterov_momentum import NesterovMomentumOptimizer
from .qng import QNGOptimizer
from .qnspsa import QNSPSAOptimizer
from .riemannian_gradient import RiemannianGradientOptimizer
from .rms_prop import RMSPropOptimizer
from .rotoselect import RotoselectOptimizer
from .rotosolve import RotosolveOptimizer
from .shot_adaptive import ShotAdaptiveOptimizer
from .spsa import SPSAOptimizer
from .qng_qjit import QNGOptimizerQJIT

# Optimizers to display in the docs
__all__ = [
    "AdagradOptimizer",
    "AdamOptimizer",
    "AdaptiveOptimizer",
    "GradientDescentOptimizer",
    "MomentumOptimizer",
    "MomentumQNGOptimizer",
    "NesterovMomentumOptimizer",
    "RMSPropOptimizer",
    "QNGOptimizer",
    "QNSPSAOptimizer",
    "RiemannianGradientOptimizer",
    "RotosolveOptimizer",
    "RotoselectOptimizer",
    "ShotAdaptiveOptimizer",
    "SPSAOptimizer",
    "QNGOptimizerQJIT",
]
