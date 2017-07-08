import Main as m
import csv

class CacheCreator:
    def __init__(self):
        with open('/Users/sumelinadar/Documents/programs/cache/input/cache_file.tsv', 'w') as f:
            writer = csv.writer(f, delimiter='\t', lineterminator='\n')
            writer.writerow(m.Main().headers)

