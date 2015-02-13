from __future__ import with_statement
import cProfile

import pagerank_map
import pagerank_reduce
import process_map
import process_reduce


for input_name in 'EmailEnron', 'GnPn100p05':
    with open('../local_test_data/%s' % input_name) as input_file:
        next_input = list(input_file)
        for iteration in range(2):
            for module in pagerank_map, pagerank_reduce, process_map, process_reduce:
                print '%s %s - iteration %s' % (input_name, module.__name__, iteration + 1)
                cProfile.run('next_input = list(%s.run(next_input))' % module.__name__, sort='time')
                print '-' * 160
                if 'map' in module.__name__:
                    next_input.sort()
