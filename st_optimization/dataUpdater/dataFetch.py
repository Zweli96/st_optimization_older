import pandas as pd
from datetime import datetime

from sample_volumes.models import Sample_Volumes, Facility, SampleType

VALID_SAMPLE_CODES = [1, 2, 3, 4]


def _get_dataset():

    try:
        df = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Excel files/sample_collection-20211207060137.csv')
        print('success fetching')
    except:
        return 'Error fetching'

    if df is not None:
        df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
        start_day = '2021-11-29'
        end_day = '2021-12-07'

        # Convert start / end dates to datetime
        start_day = pd.to_datetime(start_day)
        end_day = pd.to_datetime(end_day)

        return df[df['date'].between(start_day, end_day)]


def updateData():
    sample_volume_data = _get_dataset()

    sample_volumes_added = {total_added: 0, session_ids: []}

    sample_volumes_rejected = {total_rejected: 0, session_ids: []}

    if sample_volume_data is not None:
        for index, row in sample_volume_data.iterrows():
            new_sample_volume = Sample_Volumes()

            if int(row['sample'] in VALID_SAMPLE_CODES):
                new_sample_volume.sample_type = SampleType.objects.get(
                    sample_code=int(row['sample']))
            else:
                sample_volumes_rejected['total_rejected'] += 1
                sample_volumes_rejected['session_ids'].append(row['session'])
                continue
            if isinstance(row['collected'], (int, float)):
                new_sample_volume.volume = int(row['collected'])
            else:
                sample_volumes_rejected['total_rejected'] += 1
                sample_volumes_rejected['session_ids'].append(row['session'])
                continue

            new_sample_volume.facility = Facility.objects.get(
                facility_code=row['facility'])
            new_sample_volume.reported_date = row['date']
            new_sample_volume.reported_date = row['msisdn']

            new_sample_volume.save()
            sample_volumes_added['total_added'] += 1
            sample_volumes_added['session_ids'].append(row['session'])
            print("saving...\n" + new_sample_volume)
    else:
        return 'no data set'
