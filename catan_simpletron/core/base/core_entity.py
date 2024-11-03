from abc import ABC, abstractmethod

"""
    Base abstract class for entities 
"""
class CoreEntity(ABC):
    def __init__(self, value: str) -> None:
        self.value = value
        

    def __repr__(self) -> str:
        return self.value
    
    def __format__(self, format_spec: str) -> str:
        return format(f'{self.value}', format_spec)
    
    @abstractmethod
    def is_valid(self, value: any) -> bool:
        """ Check if entity is valid  """