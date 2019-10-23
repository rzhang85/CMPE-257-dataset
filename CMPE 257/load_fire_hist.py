from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

if __name__ == '__main__':
    print("Load Data:")
    ### UCI Machine Learning Forest Fires Data Set
    # For more information, read [Cortez and Morais, 2007].
    # 1. X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
    # 2. Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
    # 3. month - month of the year: 'jan' to 'dec'
    # 4. day - day of the week: 'mon' to 'sun'
    # 5. FFMC - FFMC index from the FWI system: 18.7 to 96.20
    # 6. DMC - DMC index from the FWI system: 1.1 to 291.3
    # 7. DC - DC index from the FWI system: 7.9 to 860.6
    # 8. ISI - ISI index from the FWI system: 0.0 to 56.10
    # 9. temp - temperature in Celsius degrees: 2.2 to 33.30
    # 10. RH - relative humidity in %: 15.0 to 100
    # 11. wind - wind speed in km/h: 0.40 to 9.40
    # 12. rain - outside rain in mm/m2 : 0.0 to 6.4
    # 13. area - the burned area of the forest (in ha): 0.00 to 1090.84
    # (this output variable is very skewed towards 0.0, thus it may make
    # sense to model with the logarithm transform).

    nRowsRead = 1000  # specify 'None' if want to read whole file
    # Fires.csv has 1880465 rows in reality, but we are only loading/previewing the first 1000 rows
    df1 = pd.read_csv('cali_fire.csv')
    df1.dataframeName = 'cali_fire.csv'
    nRow, nCol = df1.shape
    print(f'There are {nRow} rows and {nCol} columns')

    print(list(df1.columns.values))

    his1 = plt.hist(df1["FIRE_YEAR"])
    plt.title("Year Histogram")
    plt.show()
    #
    plt.scatter(df1['LONGITUDE'], df1['LATITUDE'])
    plt.show()

    print(df1.loc[[10]])
    # plt.hist(df1['STATE'])
    # plt.title("State Histogram")
    # plt.show()
    #
    # plt.hist(df1['COUNTY'])
    # plt.title("County Histogram")
    # plt.show()


