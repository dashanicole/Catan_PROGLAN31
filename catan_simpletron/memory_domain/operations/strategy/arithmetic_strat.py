from .processor_operation_strat import ProcessorOperationStrategy
from abc import abstractmethod

class ArithmeticOperationStrategy(ProcessorOperationStrategy):
    @abstractmethod
    def execute(self, processor_controller, operation: str, address: str): pass

    @abstractmethod
    def add_m(self, processor_controller, address: str): pass
       
    @abstractmethod
    def sub_m(self, processor_controller, address: str): pass
      
    @abstractmethod
    def mul_m(self, processor_controller, address: str): pass
    
    @abstractmethod
    def div_m(self, processor_controller, address: str): pass

    
