from memory_domain.datasource.memory_datasource import MemoryDatasource
from memory_domain.repository.memory_repository import MemoryRepository
from memory_domain.repository.processor_repository import ProcessorRepository
from infastracture.memory_repository_impl import MemoryRepositoryImpl
from infastracture.memory_datasource_impl import MemoryDatasourceImpl
from infastracture.memory_processor_impl import ProcessorRepositoryImpl
from .memory_controller import MemoryController
from .processor_controller import ProcessorController
from memory_domain.entities import Memory, Processor


class DepedencyContainer:
    _memory: Memory = Memory()
    _processor: Processor = Processor()
    _memory.initialize_memory(10)
    
    _datasource: MemoryDatasource = MemoryDatasourceImpl(_memory)
    _repository: MemoryRepository = MemoryRepositoryImpl(_datasource)
    _memory_controller: MemoryController = MemoryController(_repository)

    _processor_repo: ProcessorRepository = ProcessorRepositoryImpl(_processor, _repository)
    _processor_controller: ProcessorController = ProcessorController(_processor_repo, _repository)

    @classmethod
    def get_memory_controller(cls) -> MemoryController:
        return cls._memory_controller

    @classmethod
    def get_processor_controller(self) -> ProcessorController:
        return self._processor_controller
    

    