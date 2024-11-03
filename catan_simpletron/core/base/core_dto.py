from abc import ABC, abstractmethod

"""
    Base abstract class for dtos  
"""
class CoreDto(ABC):
    @abstractmethod
    def validate(self) -> None:
        """Validate the given DTO."""
        pass