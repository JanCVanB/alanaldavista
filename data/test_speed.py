from __future__ import with_statement
import cProfile
import pstats

import pagerank_map
import pagerank_reduce
import process_map
import process_reduce


for input_name in 'EmailEnron', 'GnPn100p05':
    with open('../local_test_data/%s' % input_name) as input_file:
        next_input = list(input_file)
        for module in pagerank_map, pagerank_reduce, process_map, process_reduce:
            module_name = module.__name__
            stats_file_name = '%s_%s_stats' % (input_name, module_name)
            cProfile.run('next_input = list(%s.run(next_input))' % module_name, stats_file_name)
            p = pstats.Stats(stats_file_name)
            p.strip_dirs().sort_stats('time').print_stats()
            print '-' * 160
