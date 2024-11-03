import argparse
from memory_domain.usecases.load_instruction_usecase import LoadInstruction
from infastracture.sml_parser_impl import SMLParserImpl
from presentation.dependency_container import DepedencyContainer
from presentation.cli_utils import print_usage, print_welcome

class SimpletronDriver:
    _memory_controller = DepedencyContainer.get_memory_controller()
    _processor_controller = DepedencyContainer.get_processor_controller()
    _loader = LoadInstruction(parser=SMLParserImpl())
    _argument_parser = argparse.ArgumentParser(description="Run the Simpletron program.")
                      
    @classmethod 
    def start(cls):
        cls._argument_parser_setup(cls)
        args = cls._argument_parser.parse_args()

        if args.filename is None:
            print_usage()
            return
    
        sml_file_path = f"sml/{args.filename}"
        
        try:
            # Execute the loading of the SML file
            cls._loader.execute(sml_file_path, cls._memory_controller)
        except Exception as e:
            print(f"Error loading instructions from {sml_file_path}: {e}")
            return

        print_welcome();
        if args.step:
            cls._processor_controller.run_step_by_step() 
        else:
            cls._processor_controller.run_single_step()  

    def _argument_parser_setup(cls):
        cls._argument_parser.add_argument("filename", nargs='?', help="The name of the SML file to run.")
        cls._argument_parser.add_argument("-s", "--step", action="store_true", help="Run the program step by step.")


if __name__ == "__main__":
    SimpletronDriver.start()
