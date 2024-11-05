

class MnemonicAssigner:
    def __init__(self):
        self.address_counter = 0        
        self.address_placer = 99       
        self.address_assigner = {}    
        self.jump_locations = {}       
    
    def parse_sml_mnemonics(self, filename: str) -> dict:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue
                
                parts = line.split()
                mnemonic = parts[0]
                argument = parts[1] if len(parts) > 1 else None
                jumper = parts[2] if len(parts) > 2 else None

                # Dynamic variable handling
                if self.is_memory_operation(mnemonic):
                    self.assign_variable_address(argument)

                # Handle jump labels
                if self.is_jump_label(jumper):
                    level_y = parts[3]
                    self.jump_locations[level_y] = self.address_counter

                # Dynamic jump resolution 
                if self.is_jump_resolve(mnemonic) and self.is_jump_label(jumper) and jumper not in self.address_assigner:
                    self.address_assigner[jumper] = self.address_counter
                    target_label = argument
                    self.resolve_jump(filename, target_label)

                self.address_counter += 1

        # Resolve any remaining jumps
        for label, counter in self.jump_locations.items():
            if label not in self.address_assigner:
                self.address_assigner[label] = counter

        return self.address_assigner

    def assign_variable_address(self, variable: str):
        """
        Assign an address to a variable if not already assigned.
        """
        if variable and variable not in self.address_assigner:
            self.address_assigner[variable] = self.address_placer
            self.address_placer -= 1

    def resolve_jump(self, filename: str, target_label: str):
        """
        Find the target line for a jump and assign it an address.
        """
        temp_counter = 0
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue

                parts = line.split()
                mnemonic = parts[0]
                argument = parts[1] if len(parts) > 1 else None
                jumper = parts[2] if len(parts) > 2 else None 
                label_to_find = parts[3] if len(parts) > 3 else None 

                if label_to_find == target_label:
                    self.address_assigner[target_label] = temp_counter
                    break

                temp_counter += 1

    # utilities
    def is_jump_label(self, label):
        return label == "goto"
    
    def is_jump_resolve(self, mnemo):
        return mnemo == "JZ"
    
    def is_memory_operation(self, mnemonic):
        memory_operations = ["Read", "Store", "LoadM"]
        return mnemonic in memory_operations

