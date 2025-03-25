from dataclasses import dataclass
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

@dataclass
class PageEntity(Generic[T]):
    """Paginated data entity"""
    page: int
    pageSize: int
    pageNum: int
    totalSize: int
    list: List[T] 