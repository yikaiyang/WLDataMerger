# WLDataMerger
This repository provides a python script to merge the CSV Open Data resources [[1]](#1) provided by the Wiener Linien in preparation for easier access to the Realtime Monitor API [[2]](#2).

## Why?
To access the Realtime API by the Wiener Linien, it is necessary to transmit the station ids of the station to be viewed to the REST service. Each station can have multiple station ids (= platforms) in a 1:n relationship. However, the station ids are not listed in the file ``wienerlinien-ogd-haltestellen.csv`` [[3]](#3) (stations) directly, hence must be looked up in the file ``wienerlinien-ogd-haltepunkte.csv`` [[4]](#4) (platforms) for each station.

The aim of this project is to combine the two aforementioned CSV ressources and provide a single csv or json as output with all the necessary information to access the Realtime API.

## What does it do?
The script matches the DIVA columns in the files ``wienerlinien-ogd-haltestellen.csv`` and ``wienerlinien-ogd-haltepunkte.csv``. Subsequently, it merges corresponding entries, similarly to a left outer join. Invalid values (entries containing null entries) are pruned priorly. Multiple geopositonal locations assigned to a single station are aggregated as an array.

## Dependencies
<ul>
    <li>Python</li>
    <li>pandas</li>
    <li>plotly.express (Optional, if one wishes to view the output plotted on an interactive map) </li>
</ul>

## How to run
Make sure a python environment is installed on your system.
Download the linked csv files [[3]](#3), [[4]](#4) and place them in the same folder as the script.
Ensure that the csv files are named ``wienerlinien-ogd-haltepunkte.csv`` and ``wienerlinien-ogd-haltestellen.csv``. Otherwise change the file names in the script accordingly.
Install the dependencies specified in requirements.txt.

``pip install -r requirements.txt``

Run the script using the command:

``python ./data_merger.py``

## References
<a href="https://www.data.gv.at/katalog/dataset/wiener-linien-echtzeitdaten-via-datendrehscheibe-wien" id="1">[1] https://www.data.gv.at/katalog/dataset/wiener-linien-echtzeitdaten-via-datendrehscheibe-wien</a> 

<a href="https://www.data.gv.at/katalog/dataset/wiener-linien-echtzeitdaten-via-datendrehscheibe-wien/resource/ce15bc47-696f-4ff8-81f3-4ee0737d95de" id="2">[2] https://www.data.gv.at/katalog/dataset/wiener-linien-echtzeitdaten-via-datendrehscheibe-wien/resource/ce15bc47-696f-4ff8-81f3-4ee0737d95de</a> 

<a href="http://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltestellen.csv" id="3">[3] http://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltestellen.csv</a> 

<a href="http://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltepunkte.csv" id="4">[4] http://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltepunkte.csv</a> 


## License
MIT License

Datenquelle: Stadt Wien - https://data.wien.gv.at, Creative Commons Namensnennung 4.0 International
