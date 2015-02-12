import pagerank_map
import pagerank_reduce
import process_map
import process_reduce


MAX_ITERATIONS = 15


def test_1_iteration():
    with open('../local_test_data/EmailEnron') as input_file:
        inputs = list(input_file)
        len_input_file = len(inputs)
        for function in pagerank_map, pagerank_reduce, process_map, process_reduce:
            inputs = list(function.run(inputs))
            if 'map' in function.__name__:
                inputs.sort()
    assert len(inputs) == len_input_file, 'First output is the incorrect length'


def test_2_iterations():
    with open('../local_test_data/EmailEnron') as input_file:
        inputs = list(input_file)
        len_input_file = len(inputs)
        for _ in range(4):
            for function in pagerank_map, pagerank_reduce, process_map, process_reduce:
                inputs = list(function.run(inputs))
                if 'map' in function.__name__:
                    inputs.sort()
    assert len(inputs) == len_input_file, 'Second output is the incorrect length'


def test_max_iterations():
    with open('../local_test_data/EmailEnron') as input_file:
        inputs = list(input_file)
        len_input_file = len(inputs)
        for _ in range(MAX_ITERATIONS):
            for function in pagerank_map, pagerank_reduce, process_map, process_reduce:
                inputs = list(function.run(inputs))
                if 'map' in function.__name__:
                    inputs.sort()
            if inputs[0].startswith('Final'):
                break
    assert inputs[0].startswith('Final'), 'Final ranks not output'
    with open('../sols/EmailEnron') as solution_file:
        solutions = list(solution_file)
    assert len(inputs) == len(solutions), 'Final output is the incorrect length'
    print '\n'.join(inputs)
    assert all([solutions[i] in inputs[i] for i in range(len(solutions))]), 'Final output is incorrect'
