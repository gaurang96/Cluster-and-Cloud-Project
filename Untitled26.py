def map_function1(arrays):
    #print(arrays)
    formats = '%a %b %d %H:%M:%S %z %Y'
    date = datetime.strptime(arrays['key'][1],formats).date()
    positve_neutral_negative = 0
    if arrays['key'][0] < -.05:
        positve_neutral_negative = -1
    if arrays['key'][0] > .05:
        positve_neutral_negative = 1
    
    return ((date, positve_neutral_negative))


database_timeseries = client['twitter_time_series']
import pandas as pd
from datetime import datetime
formats = '%a %b %d %H:%M:%S %z %Y'
time_series=(database_timeseries.get_view_result('_design/view_date', 'view_date',
    raw_result=True))

zip_file = map(map_function1, time_series['rows'])
#print(list(zip_file))
time_series_dataframe = pd.DataFrame(list(zip_file), columns=['date', 'positive_neutral_negative'])

time_series_dataframe_json = json.loads(time_series_dataframe.groupby('date').agg('count').to_json())
