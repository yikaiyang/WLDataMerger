import pandas as pd
import plotly.express as px
import re

# Specifies whether surrounding quotation marks: " " are removed.
removeQuotationMarksOption = True

# Specifies whether S U appendixes after each station shall be purged.
# Naming variants of stations will be combined. (e.g Stubentor U and Stubentor)
removeAppendixesOption = True
numberDecimalPlaces = 6

removeQuotationMarks = lambda x: x.str.replace('"', '')
removeAppendixes = lambda x: re.sub(removeAppendixesRegexStr, '', x)
removeAppendixesRegexStr = ' S$| U$| S U$| S,| U,| S U,| SU$| SU,'
removeInvalidCharRegex = lambda x: re.sub(removeInvalidCharRegexStr, '', x)
removeInvalidCharRegexStr = '<|>'


replaceDelimiterRegex = lambda x: re.sub(replaceDelimiterRegexStr, ', ', x)
replaceDelimiterRegexStr = ' / | - '


dfHP = pd.read_csv("./wienerlinien-ogd-haltepunkte.csv", delimiter=';', skiprows=0)
dfHS = pd.read_csv('./wienerlinien-ogd-haltestellen.csv', delimiter=';', skiprows=0)


dfHP= dfHP.dropna(axis=0, how="any")
dfHP.drop(['StopText','Municipality', 'MunicipalityID'], axis=1, inplace=True)
dfHS = dfHS.dropna(axis=0, how="any")


dfResult = pd.merge(dfHP, dfHS, suffixes=['_hp', '_hs'], on= 'DIVA', how='inner')
dfResult['Platforms'] = dfResult.apply(lambda x: [x['Longitude_hp'] ,x['Latitude_hp']], axis=1)

dfResult = dfResult.apply({
    'StopID': str,
    'PlatformText': lambda x: replaceDelimiterRegex(removeInvalidCharRegex(removeAppendixes(x))),
    'DIVA': str,
    'Municipality': str,
    'MunicipalityID': str,
    'Latitude_hp': lambda x: x,
    'Longitude_hp': lambda x: x,
    'Latitude_hs': lambda x: x,
    'Longitude_hs': lambda x: x,
    'Platforms': lambda x: x,
}).groupby(['DIVA']).agg({
    'PlatformText': lambda x: x.iloc[0],
    'StopID': lambda x: list(x),
    'Municipality': lambda x: x.iloc[0],
    'MunicipalityID': lambda x: x.iloc[0],
    'Latitude_hs': lambda x: x.iloc[0],
    'Longitude_hs': lambda x: x.iloc[0],
    'Platforms': lambda x: list(x)
})

dfResult = dfResult.rename(columns={'Latitude_hs': 'Latitude', 'Longitude_hs': 'Longitude'})
dfResult.to_csv('./wienerlinien-ogd-haltepunkte_merged.csv', index = False, sep=';')


# Uncomment to plot station locations on interactive map

# def showMap():
#     fig = px.scatter_mapbox(dfResult, lat="Latitude", lon="Longitude", hover_name="PlatformText", hover_data=["Longitude", "Latitude"])
#     fig.update_layout(mapbox_style="open-street-map")
#     fig.show()
# showMap() 

dfResult.to_csv('./wienerlinien-ogd-haltepunkte_merged.csv', index = False, sep=';')
dfResult.to_json('./wienerlinien-ogd-haltepunkte_merged.json', orient = 'records')
