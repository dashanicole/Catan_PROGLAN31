from .processor_operation_strat import ProcessorOperationStrategy
from abc import abstractmethod

class LoadStoreOperationStrategy(ProcessorOperationStrategy):
    @abstractmethod
    def execute(self, processor_controller, operation: str, address: str): pass

    @abstractmethod
    def load_m(self, processor_controller, address: str): pass
      
    @abstractmethod
    def store(self, processor_controller, address: str): pass