from datetime import datetime, timedelta, date
import pandas as pd

def str_to_datetime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
    
def get_hour_range(start, end):
    if type(start) is not datetime:
        start = str_to_datetime(start)
        
    if type(end) is not datetime:
        end = str_to_datetime(end)
    
    current = start
    hours = []

    while current < end + timedelta(days=1):
        hours.append(current)
        current += timedelta(hours=1)
    
    return hours
    
seasons = [
    (1, (date(2000, 1,  1),  date(2000, 3, 20))),
    (2, (date(2000, 3, 21),  date(2000, 6, 20))),
    (3, (date(2000, 6, 21),  date(2000, 9, 22))),
    (4, (date(2000, 9, 23),  date(2000, 12, 20))),
    (1, (date(2000, 12, 21),  date(2000, 12, 31)))
]    

def get_season(dt):
    dt = dt.date()
    dt = dt.replace(year=2000)
    
    return next(season for season, (start, end) in seasons if start <= dt <= end)

holidays = set([
    '2014-01-01',
    '2014-04-13',
    '2014-04-17',
    '2014-04-18',
    '2014-04-20',
    '2014-04-21',
    '2014-05-01',
    '2014-05-17',
    '2014-05-29',
    '2014-06-08',
    '2014-06-09',
    '2014-12-25',
    '2014-12-26',
    '2015-01-01',
    '2015-03-29',
    '2015-04-02',
    '2015-04-03',
    '2015-04-05',
    '2015-04-06',
    '2015-05-01',
    '2015-05-14',
    '2015-05-17',
    '2015-05-24',
    '2015-05-25',
    '2015-12-25',
    '2015-12-26',
    '2016-01-01',
    '2016-03-20',
    '2016-03-24',
    '2016-03-25',
    '2016-03-27',
    '2016-03-28',
    '2016-05-01',
    '2016-05-05',
    '2016-05-15',
    '2016-05-16',
    '2016-05-17',
    '2016-12-25',
    '2016-12-26',
    '2017-01-01',
    '2017-04-09',
    '2017-04-12',
    '2017-04-14',
    '2017-04-16',
    '2017-04-17',
    '2017-05-01',
    '2017-05-17',
    '2017-05-25',
    '2017-06-04',
    '2017-06-04',
    '2017-12-25',
    '2017-12-26',
    '2018-01-01',
    '2018-03-25',
    '2018-03-29',
    '2018-03-30',
    '2018-04-01',
    '2018-04-02',
    '2018-05-01',
    '2018-05-10',
    '2018-05-17',
    '2018-05-20',
    '2018-05-21',
    '2018-12-25',
    '2018-12-26'
])

def get_holiday(dt):
    return int(dt.strftime('%Y-%m-%d') in holidays)

datetime_feature = {
    'year': lambda d: d.year,
    'month': lambda d: d.month,
    'monthday': lambda d: d.day,
    'weekday': lambda d: d.weekday(),
    'hour': lambda d: d.hour,
    'season': get_season,
    'holiday': get_holiday,
}
    
def get_hour_features(start, end, features=['year', 'month', 'monthday', 'weekday', 'hour', 'season', 'holiday']):
    hours = get_hour_range(start, end)
    df = pd.DataFrame({'datetime': hours})
    df = df.set_index('datetime')
    
    for feature in features:
        df[feature] = df.index.map(datetime_feature[feature])
            
    return df