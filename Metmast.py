

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

Met1= pd.read_csv('C:/Users/snuñez/Pictures/h.csv',header=0)#default route
Met1=Met1.fillna(' ') #Delete NA or NAN


at=(Met1[0:3]) #Select 3 firts rows to  create header
at=list(at.sum()) #Create header


Met1.columns=at #Rename columns

Met1 = Met1.iloc[3: , :] #ignore the  name rows 


Met1.index = pd.Index(range(1, len(Met1) + 1))  #Rename Index

Met1=Met1.astype(str) # is beter start with string to convert in others
Met1.iloc[:, 2:74]=Met1.iloc[:, 2:70].astype(float) #Transform to float al numeric data

Met1['TIMESTAMPTS '] = pd.to_datetime(Met1['TIMESTAMPTS '], dayfirst=True, format= "%d/%m/%Y %H:%M")

Met1['Hour'] = pd.DatetimeIndex(Met1['TIMESTAMPTS ']).hour.astype(int) #Create columns indicating to separate date 
Met1['Day'] = pd.DatetimeIndex(Met1['TIMESTAMPTS ']).day.astype(int) #" " 
Met1['Month'] = pd.DatetimeIndex(Met1['TIMESTAMPTS ']).month.astype(int) # " "
Met1['Year'] = pd.DatetimeIndex(Met1['TIMESTAMPTS ']).year.astype(int) # " "

Met1=Met1[['TIMESTAMPTS ', 'Hour', 'Day', 'Month', 'Year', 'Ane120m_Minm/sMin', 'Ane120m_Maxm/sMax', 'Ane120m_Avgm/sAvg', 'Ane120m_Stdm/sStd', 'Ane50m_Minm/sMin', 'Ane50m_Maxm/sMax', 'Ane50m_Avgm/sAvg', 'Ane50m_Stdm/sStd', 'Vane120m_MinDegMin', 'Vane120m_MaxDegMax', 'CTRL_WVT1_AvgsWVc', 'Vane120m_DDegWVc', 'Vane120m_StdDegWVc', 'Vane50m_MinDegMin', 'Vane50m_MaxDegMax', 'CTRL_WVT2_AvgsWVc', 'Vane50m_DDegWVc', 'Vane50m_StdDegWVc', 'Temp120m_MinCMin', 'Temp120m_MaxCMax', 'Temp120m_AvgCAvg', 'Temp120m_StdCStd', 'RH120m_Min%Min', 'RH120m_Max%Max', 'RH120m_Avg%Avg', 'RH120m_Std%Std', 'Barom1m_MinhPaMin', 'Barom1m_MaxhPaMax', 'Barom1m_AvghPaAvg', 'Barom1m_StdhPaStd', 'AirDensity_MinKg/m3Min', 'AirDensity_MaxKg/m3Max', 'AirDensity_AvgKg/m3Avg', 'AirDensity_StdKg/m3Std', 'Batt_MinVMin', 'Batt_MaxVMax', 'Batt_AvgVAvg', 'Batt_StdVStd', 'Logg_Temp_MinCMin', 'Logg_Temp_MaxCMax', 'Logg_Temp_AvgCAvg', 'Logg_Temp_StdCStd', 'LitBatt_MinVMin', 'LitBatt_MaxVMax', 'LitBatt_AvgVAvg', 'LitBatt_StdVStd', 'Precip2m_Max Max', 'Precip2m_Min Min', 'Precip2m_Avg Avg', 'Precip2m_Std Std', 'AlaDoor_Max Max', 'AlaDoor_Min Min', 'AlaDoor_Avg Avg', 'AlaDoor_Std Std', 'AlaSPD_Max Max', 'AlaSPD_Min Min', 'AlaSPD_Avg Avg', 'AlaSPD_Std Std', 'Cab_Temp_Min Min', 'Cab_Temp_Max Max', 'Cab_Temp_Avg Avg', 'Cab_Temp_Std Std', 'Rain3m_MinmmMin', 'Rain3m_MaxmmMax', 'Rain3m_AvgmmAvg', 'Rain3m_StdmmStd', 'Rain3m_TotmmTot', 'WVTCount_Tot Tot']]
#Reorganize the order of the colmns


#plt.plot(Met1['TIMESTAMPTS '],Met1['Ane120m_Minm/sMin'])
#plt.plot(Met1['TIMESTAMPTS '],Met1['Ane120m_Maxm/sMax'])
#plt.plot(Met1['TIMESTAMPTS '],Met1['Ane120m_Avgm/sAvg'])
#plt.xticks(fontsize=7,rotation=90)
#plt.yticks(fontsize=7)
#plt.xlabel(" ")
#plt.ylabel("m/s",fontsize=7)
#plt.legend(['Vel min','Vel max','Vel avg'])
#plt.title('Wind speed m/s')
#plt.show()

A1 = Met1['Ane120m_Minm/sMin'].mean()
A2 = Met1['Ane120m_Maxm/sMax'].max()
A3 = Met1['Ane120m_Avgm/sAvg'].mean()


print('El promedio de velocidad mínima es: ', round(A1,2), ' m/s')
print('El promedio de velocidad máxima es: ', round(A2,2), ' m/s')
print('El promedio de velocidad es: ', round(A3,2), ' m/s' )