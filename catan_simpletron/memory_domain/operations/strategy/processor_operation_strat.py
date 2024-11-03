from abc import ABC, abstractmethod

class ProcessorOperationStrategy(ABC):
    @abstractmethod
    def execute(self, processor_controller, operation: str, address: str): pass 