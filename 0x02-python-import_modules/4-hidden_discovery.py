#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    import types

def print_module_names(module_path):
    with open(module_path, 'rb') as file:
        code = compile(file.read(), module_path, 'exec')

    for instr in dis.get_instructions(code):
        if instr.opname == 'LOAD_NAME' and not instr.argval.startswith('__'):
            print(instr.argval)

if __name__ == "__main__":
    module_path = 'hidden_4.pyc'
    print_module_names(module_path)
