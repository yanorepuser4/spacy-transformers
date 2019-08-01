# Stubs for torch.sparse (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def addmm(mat: Any, mat1: Any, mat2: Any, beta: int = ..., alpha: int = ...): ...
def mm(mat1: Any, mat2: Any): ...
def sum(input: Any, dim: Optional[Any] = ..., dtype: Optional[Any] = ...): ...