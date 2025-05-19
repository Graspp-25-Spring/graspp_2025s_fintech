import functionsNakada
import pandas as pd

mydf_ICTPolicy = functionsNakada.importWB("ITU_ICT", "ITU_ICT_G5_DIG_ECON", "2011", "2024")
mydf_FarmCredit = functionsNakada.importWB("FAO_IC", "FAO_IC_23068", "2000", "2024")
mydf_Value_AgProduction = functionsNakada.importWB("FAO_MK", "FAO_MK_22016", "2000", "2024")
mydf_Value_AgProcessing = functionsNakada.importWB("FAO_MK", "FAO_MK_22077", "2000", "2024")
mydf_Fertilizer = functionsNakada.importWB("WB_WDI", "WB_WDI_AG_CON_FERT_ZS", "2000", "2024")

asianCountries = ['VNM','LAO','THA','KHM','MYS','SGP','MMR','PHL','BRN','IDN',
                  'BGD','IND','PAK','NPL','LKA','BTN']

# asianCountries = ['AFG','ARM','AZE','BHR','BGD','BTN','BRN','KHM',
#                   'CHN','GEO','IND','IDN','IRN','IRQ','ISR','JPN','JOR','KAZ','PRK',
#                   'KOR','KWT','KGZ','LAO','LBN','MYS','MDV','MNG','MMR','NPL','OMN',
#                   'PAK','PSE','PHL','QAT','SAU','SGP','LKA','SYR','TJK','THA','TLS',
#                   'TUR','TKM','ARE','UZB','VNM','YEM']

mydf_ICTPolicy_filtered = functionsNakada.filterWB(mydf_ICTPolicy, asianCountries, ["REF_AREA", "TIME_PERIOD", "OBS_VALUE"], ["areaCode", "year", "ICTPolicy"])
mydf_FarmCredit_filtered = functionsNakada.filterWB(mydf_FarmCredit, asianCountries, ["REF_AREA", "TIME_PERIOD","OBS_VALUE"], ["areaCode", "year", "FarmCredit"])
mydf_Value_AgProduction_filtered = functionsNakada.filterWB(mydf_Value_AgProduction, asianCountries, ["REF_AREA", "TIME_PERIOD","OBS_VALUE"], ["areaCode", "year", "ProductionValue"])
mydf_Value_AgProcessing_filtered = functionsNakada.filterWB(mydf_Value_AgProcessing, asianCountries, ["REF_AREA", "TIME_PERIOD","OBS_VALUE"], ["areaCode", "year", "ProcessingValue"])
mydf_Fertilizer_filtered = functionsNakada.filterWB(mydf_Fertilizer, asianCountries, ["REF_AREA", "TIME_PERIOD","OBS_VALUE"], ["areaCode", "year", "Fertilizer"])

mydf_ICTPolicy_indexed = functionsNakada.setIndexWB(mydf_ICTPolicy_filtered, ["areaCode", "year"])
mydf_FarmCredit_indexed = functionsNakada.setIndexWB(mydf_FarmCredit_filtered, ["areaCode", "year"])
mydf_Value_AgProduction_indexed = functionsNakada.setIndexWB(mydf_Value_AgProduction_filtered, ["areaCode", "year"])
mydf_Value_AgProcessing_indexed = functionsNakada.setIndexWB(mydf_Value_AgProcessing_filtered, ["areaCode", "year"])
mydf_Fertilizer_indexed = functionsNakada.setIndexWB(mydf_Fertilizer_filtered, ["areaCode", "year"])

    
mydf_MergedAll = functionsNakada.merge_dataframes([mydf_FarmCredit_indexed, mydf_ICTPolicy_indexed, 
                       mydf_Value_AgProduction_indexed, mydf_Value_AgProcessing_indexed, 
                       mydf_Fertilizer_indexed], ["areaCode", "year"])
cols_to_convert = [col for col in mydf_MergedAll.columns if col != 'areaCode']
mydf_MergedAll[cols_to_convert] = mydf_MergedAll[cols_to_convert].apply(pd.to_numeric, errors='coerce')

functionsNakada.exportCSV(mydf_ICTPolicy_indexed, 'ICTPolicy')
functionsNakada.exportCSV(mydf_FarmCredit_indexed, 'FarmCredit')
functionsNakada.exportCSV(mydf_Value_AgProduction_indexed, 'AgProduction')
functionsNakada.exportCSV(mydf_Value_AgProcessing_indexed, 'AgProcessing')
functionsNakada.exportCSV(mydf_Fertilizer_indexed, 'Fertilizer')
functionsNakada.exportCSV(mydf_MergedAll, 'MergedAll')




