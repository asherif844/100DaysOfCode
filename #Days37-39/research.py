import csv
import os
import collections
import operator
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'date,actual_mean_temp,actual_min_temp,actual_max_temp,'
    'average_min_temp,average_max_temp,record_min_temp,record_max_temp,'
    'record_min_temp_year,record_max_temp_year,actual_precipitation,'
    'average_precipitation,record_precipitation'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        count = []
        mean_temp = []
        date = []
        max_temp = 0
        max_date = 0
        b = []
        for id, row in enumerate(reader, start=1):
            record = parse_row(row)
            data.append(record)
            count.append(id)
            d = {record.actual_mean_temp, record.date}
            mean_temp.append((record.actual_mean_temp))
            date.append((record.date))
            b.append(d)
            if record.actual_mean_temp > max_temp:
                max_temp = record.actual_mean_temp
                max_date = record.date
        max_count = max(count)
        sum_mean_temp = sum(mean_temp)
        average_actual_mean_temp = f'{round(sum_mean_temp/max_count, 2)} F'
        b = sorted(b, key=lambda x: 1)

    return average_actual_mean_temp, max_date, max_temp, data, b


def parse_row(row):
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])

    record = Record(
        **row
    )

    return record


def hot_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_max_temp)
