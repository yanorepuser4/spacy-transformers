# Stubs for torch.distributed.deprecated (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class dist_backend:
    UNDEFINED: int = ...
    TCP: int = ...
    MPI: int = ...
    GLOO: int = ...
    NCCL: int = ...

def is_available(): ...
def destroy_process_group() -> None: ...
def is_initialized(): ...
def init_process_group(backend: Any, init_method: str = ..., **kwargs: Any) -> None: ...
def init_master_worker(backend: Any, init_method: str = ..., **kwargs: Any) -> None: ...

class reduce_op:
    SUM: Any = ...
    PRODUCT: Any = ...
    MAX: Any = ...
    MIN: Any = ...

class group:
    WORLD: Any = ...

class _DistributedRequest:
    request: Any = ...
    def __init__(self, request: Any) -> None: ...
    def is_completed(self): ...
    def wait(self) -> None: ...

def get_rank(): ...
def get_world_size(): ...
def isend(tensor: Any, dst: Any): ...
def irecv(tensor: Any, src: Any): ...
def send(tensor: Any, dst: Any): ...
def recv(tensor: Any, src: Optional[Any] = ...): ...
def broadcast_multigpu(tensor_list: Any, src: Any, group: Any = ...): ...
def broadcast(tensor: Any, src: Any, group: Any = ...): ...
def all_reduce_multigpu(tensor_list: Any, op: Any = ..., group: Any = ...): ...
def all_reduce(tensor: Any, op: Any = ..., group: Any = ...): ...
def reduce_multigpu(tensor_list: Any, dst: Any, op: Any = ..., group: Any = ...): ...
def reduce(tensor: Any, dst: Any, op: Any = ..., group: Any = ...): ...
def all_gather_multigpu(output_tensor_lists: Any, input_tensor_list: Any, group: Any = ...): ...
def all_gather(tensor_list: Any, tensor: Any, group: Any = ...): ...
def gather(tensor: Any, **kwargs: Any): ...
def scatter(tensor: Any, **kwargs: Any): ...
def barrier(group: Any = ...): ...
def new_group(ranks: Optional[Any] = ...): ...