from __future__ import with_statement
import cProfile

from uploader import do_main


with open('AWSkeys.txt') as aws_key_file:
    team_id, access_key, secret_key = aws_key_file.read().split(',')
cProfile.run('do_main(team_id, access_key, secret_key)', sort='time')
