from inspect import signature, getmembers, isfunction
import sys
import importlib.util

# Convenience python script to generate Python test script for a given Python script
# example: python base_template.py <target_file.py>

python_script = sys.argv[1]
spec = importlib.util.spec_from_file_location('target_module', python_script)
target_module = importlib.util.module_from_spec(spec)

sys.modules['target_module'] = target_module
spec.loader.exec_module(target_module)

functions = (getmembers(target_module, isfunction))
if len(functions) > 1:
    raise Exception('Target module has more than 1 function')

target_function = functions[0][1]
function_name = functions[0][0]
sig = signature(target_function)

params = sig.parameters

test_file = 'test_' + python_script

with open(test_file, 'w') as f:
    f.writelines([
        'from {} import *\n\n'.format(python_script.replace('.py', '')),
        'testcases = [\n\n]\n\n',
        'def test_{}():\n'.format(function_name),
        '    for testcase in testcases:\n',
        '        assert {}({}) == {}\n'.format(
            function_name, 
            ', '.join(['testcase[{}]'.format(i) for i in range(len(params))]), 
            'testcase[{}]'.format(len(params))
            )
        ])

print('Completed writing test file: {}'.format(test_file))
