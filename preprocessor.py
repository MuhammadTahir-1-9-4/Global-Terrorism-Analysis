import pandas as pd

def load_and_clean_data():

    # load dataset
    df = pd.read_csv('gtd.csv', encoding='ISO-8859-1', low_memory=False)
    
    # rename columns
    df.rename(columns={
        'iyear': 'Year', 'imonth': 'Month', 'iday': 'Day',
        'country_txt': 'Country', 'provstate': 'State', 'region_txt': 'Region',
        'attacktype1_txt': 'AttackType', 'targtype1_txt': 'TargetType', 
        'gname': 'GroupName', 'weaptype1_txt': 'WeaponType',
        'nkill': 'Killed', 'nwound': 'Wounded' 
    }, inplace=True)

    country_mapping = {
        'East Germany (GDR)': 'Germany',
        'West Germany (FRG)': 'Germany',
        'South Vietnam': 'Vietnam',
        'Zaire': 'Democratic Republic of the Congo',
        'Rhodesia': 'Zimbabwe',
        'Soviet Union': 'Russia',
        'Yugoslavia': 'Serbia',
        'Serbia-Montenegro': 'Serbia',
        'North Yemen': 'Yemen',
        'South Yemen': 'Yemen',
        "People's Republic of the Congo": 'Republic of the Congo',
        'Hong Kong': 'China',
        'Macau': 'China',
        'Falkland Islands': 'United Kingdom',
        'French Guiana': 'France',
        'Guadeloupe': 'France',
        'Martinique': 'France',
        'New Caledonia': 'France',
        'French Polynesia': 'France',
        'Wallis and Futuna': 'France',
        'West Bank and Gaza Strip': 'Palestine'
    }
    df['Country'] = df['Country'].replace(country_mapping)

    df = df[df['Country'] != 'International']


    # filter out invalid month or day values
    df = df[df['Month'] != 0]
    df = df[df['Day'] != 0]

    # fill NaN values in Killed and Wounded with 0 for calculation purpses
    df['Killed'] = df['Killed'].fillna(0)
    df['Wounded'] = df['Wounded'].fillna(0)

    # create a 'Casualties' column for combined analysis
    df['Casualties'] = df['Killed'] + df['Wounded']

    return df