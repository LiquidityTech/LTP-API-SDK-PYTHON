from dataclasses import dataclass, fields
from typing import Generic, TypeVar, Optional, Any, List, get_origin

T = TypeVar('T')

@dataclass
class ApiResponse(Generic[T]):
    code: int
    message: str
    data: Optional[T] = None

    def print_response(self, title: str = "API Response"):
        """
        Format and print response content
        
        Args:
            title: Response title
        """
        print(f"\n=== {title} ===")
        print(f"Code: {self.code}")
        print(f"Message: {self.message}")
        
        if self.data is not None:
            print("\nData:")
            # Handle list type
            if isinstance(self.data, list):
                for i, item in enumerate(self.data):
                    print(f"\nItem {i + 1}:")
                    if hasattr(item, '__dataclass_fields__'):
                        for field in fields(item):
                            value = getattr(item, field.name)
                            if value is not None and value != "":
                                print(f"  {field.name}: {value}")
                    else:
                        print(f"  {item}")
            # Handle dictionary type
            elif isinstance(self.data, dict):
                for key, value in self.data.items():
                    if isinstance(value, list):
                        print(f"\n{key}:")
                        for i, item in enumerate(value):
                            print(f"  Item {i + 1}:")
                            if hasattr(item, '__dataclass_fields__'):
                                for field in fields(item):
                                    val = getattr(item, field.name)
                                    if val is not None and val != "":
                                        print(f"    {field.name}: {val}")
                            else:
                                print(f"    {item}")
                    else:
                        print(f"  {key}: {value}")
            # Handle single object type
            elif hasattr(self.data, '__dataclass_fields__'):
                for field in fields(self.data):
                    value = getattr(self.data, field.name)
                    if value is not None and value != "":
                        print(f"  {field.name}: {value}")
            else:
                print(f"  {self.data}") 