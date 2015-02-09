import os


ITERATION_CAP = 50
PYTHON = 'c:\\python27\\python'
PAGERANK_MAP = '..\\data\\pagerank_map.py'
PAGERANK_REDUCE = '..\\data\\pagerank_reduce.py'
PROCESS_MAP = '..\\data\\process_map.py'
PROCESS_REDUCE = '..\\data\\process_reduce.py'
GNP_INPUT = '..\\local_test_data\\GNPn100p05'
GNP_MIDDLE = '..\\local_test_data\\GNPn100p05Middle'
GNP_OUTPUT = '..\\local_test_data\\GNPn100p05Output'
INPUT_CHAR = '<'
OUTPUT_CHAR = '>'
PIPE_CHAR = '|'
SORT = 'sort'

INPUT_FIRST_COMMAND = [PYTHON, PAGERANK_MAP, INPUT_CHAR, GNP_INPUT]
INPUT_AFTER_COMMAND = [PYTHON, PAGERANK_MAP, INPUT_CHAR, GNP_MIDDLE]
PIPE_TO_PAGERANK_REDUCE = [PIPE_CHAR, SORT, PIPE_CHAR, PYTHON, PAGERANK_REDUCE]
PIPE_TO_PROCESS_MAP = [PIPE_CHAR, PYTHON, PROCESS_MAP]
PIPE_TO_PROCESS_REDUCE = [PIPE_CHAR, SORT, PIPE_CHAR, PYTHON, PROCESS_REDUCE]
OUTPUT_COMMAND = [OUTPUT_CHAR, GNP_OUTPUT]


def test_gnp_2_iterations():
    command_body = PIPE_TO_PAGERANK_REDUCE + PIPE_TO_PROCESS_MAP + PIPE_TO_PROCESS_REDUCE
    first_command = INPUT_FIRST_COMMAND + command_body + OUTPUT_COMMAND
    after_command = INPUT_AFTER_COMMAND + command_body + OUTPUT_COMMAND
    os.system(' '.join(first_command))
    os.system('del {}'.format(GNP_MIDDLE))
    os.system('copy {} {} >nul'.format(GNP_OUTPUT, GNP_MIDDLE))
    os.system(' '.join(after_command))
    os.system('del {}'.format(GNP_MIDDLE))
    os.system('copy {} {} >nul'.format(GNP_OUTPUT, GNP_MIDDLE))
    with open(GNP_INPUT) as enron_input_file:
        input_lines = enron_input_file.readlines()
    with open(GNP_OUTPUT) as enron_output_file:
        output_lines = enron_output_file.readlines()
        assert len(input_lines) == len(output_lines), '{} is the wrong length'.format(GNP_OUTPUT)


def test_gnp_final_20_lines():
    command_body = PIPE_TO_PAGERANK_REDUCE + PIPE_TO_PROCESS_MAP + PIPE_TO_PROCESS_REDUCE
    first_command = INPUT_FIRST_COMMAND + command_body + OUTPUT_COMMAND
    after_command = INPUT_AFTER_COMMAND + command_body + OUTPUT_COMMAND
    os.system(' '.join(first_command))
    os.system('del {}'.format(GNP_MIDDLE))
    os.system('copy {} {} >nul'.format(GNP_OUTPUT, GNP_MIDDLE))
    done = False
    iteration = 1
    while not done:
        iteration += 1
        assert iteration <= ITERATION_CAP, 'Iteration cap exceeded'
        os.system(' '.join(after_command))
        os.system('del {}'.format(GNP_MIDDLE))
        os.system('copy {} {} >nul'.format(GNP_OUTPUT, GNP_MIDDLE))
        with open(GNP_OUTPUT) as enron_output_file:
            lines = enron_output_file.readlines()
            assert lines, '{} is blank'.format(GNP_OUTPUT)
            done = lines[0].startswith('FinalRank')
            if done:
                assert 20 == len(enron_output_file.readlines()), \
                    'Final {} does not have 20 lines'.format(GNP_OUTPUT)
            else:
                assert lines[0].startswith('NodeId'), \
                    'Interim {} does not start with "NodeId"'.format(GNP_OUTPUT)
