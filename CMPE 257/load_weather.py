from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)



if __name__ == '__main__':
    df1 = pd.read_csv('weather.csv')
    df1.dataframeName = 'weather.csv'

    # "University of California Statewide Integrated Pest Management Program"
    # "How to Manage Pests: California Weather Data"
    # "Retrieve data in comma delimited data file format"
    # " "
    # "Weather database request:  "
    # " "
    # "Time Period: January 1, 2002 to October 3, 2017, retrieved on October 4, 2019"
    # " (5755 days)"
    # " "
    # "To save this text, you can:"
    # "Select SAVE AS and TEXT from the top menu of your browser, or"
    # "copy and paste the data to a new document in a word processor"
    # "and save it as text."
    # " "
    # "Note: Only 92% of requested data were available from station SAN_DIEGO.A.    See Retrieval Table."
    # " "
    # "                     Retrieval Table"
    # "                     Stations used to fill in missing data"
    # " "
    # "                     Data Values  Data Values  Data Values  Data Values  Data Values"
    # "                        from         from         from         from        Missing"
    # "Variable             Station      Backup 1     Backup 2     Averages"
    # "Precipitation         5452          199           74           30            0        "
    # "                     SAN_DIEGO.A  MIRAMAR.A    OTAY_LAKE.A  VISTA.C      "
    # "Air Temps, max/min    5208          358          136           53            0        "
    # "                     SAN_DIEGO.A  MIRAMAR.A    OTAY_LAKE.A  SN_DIEGO.A   "
    # "Soil Temps, max/min   5084          526          110            0           35        "
    # "                     SAN_DIEGO.A  MIRAMAR.A    OTAY_LAKE.A  none         "
    # "Rel. Humidity         5229            0            0            0          526        "
    # "                     SAN_DIEGO.A  none         none         none         "
    # "ETo                   5486            0            0            0          269        "
    # "                     SAN_DIEGO.A  none         none         none         "
    # "Solar Radiation       5327          275          114           39            0        "
    # "                     SAN_DIEGO.A  MIRAMAR.A    OTAY_LAKE.A  SN_DIEGO.A   "
    # "Wind Speed & Dir      5352            0            0            0          403        "
    # "                     SAN_DIEGO.A  none         none         none         "
    # " "
    # "Variable   Description                   Units"
    # "   1       Database name                 "
    # "   2       Date: year,month,day          yyyymmdd"
    # "   3       Observation time              hhmm"
    # "   4       Precipitation, amount         Inches"
    # "   5       Precipitation, type           (coded)"
    # "   6       Air temperature, maximum      Fahrenheit"
    # "   7       Air temperature, minimum      Fahrenheit"
    # "   8       Air temperature, observed     Fahrenheit"
    # "   9       Weather conditions            (coded)"
    # "  10       Wind, direction               N,NE,E,SE,S,SW,W,NW, 0=calm"
    # "  11       Wind, speed                   Miles per hour"
    # "  12       Bulb temperature, wet         Fahrenheit"
    # "  13       Bulb temperature, dry         Fahrenheit"
    # "  14       Soil temperature, maximum     Fahrenheit"
    # "  15       Soil temperature, minimum     Fahrenheit"
    # "  16       Pan evaporation               Inches"
    # "  17       Solar radiation               Langleys"
    # "  18       Reference evapotranspiration  Inches"
    # "  19       Relative humidity, minimum    Percent"
    # "  20       Relative humidity, maximum    Percent"
    # " "



    nRow, nCol = df1.shape
    print(f'There are {nRow} rows and {nCol} columns')

    print(list(df1.columns.values))

    plt.scatter(df1['index'], df1['Air max'])
    plt.title("Air Max Temperature")
    plt.show()


    plt.scatter(df1['index'], df1['Soil max'])
    plt.title("Soil Max Temperature")
    plt.show()
