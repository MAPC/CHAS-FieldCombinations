# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

####This script combines CHAS data to determine population at 30-50% AMI by race/ethnicity
import pandas as pd
###the first part is for county level data (Middlesex and Worceter counties)
County = pd.read_csv (r'K:\DataServices\Projects\Data_Requests\2020\HabitatforHumanity_CHASRaceEthnicity\CHAS_Data_2012_2016\Table1_County.csv')
print (County)

sum_AI = County["T1_est16"] + County["T1_est57"] + County["T1_est98"] + County["T1_est140"] + County["T1_est181"] + County["T1_est222"]
County["AI"] = sum_AI

sum_AS = County["T1_est15"] + County["T1_est56"] + County["T1_est97"] + County["T1_est139"] + County["T1_est180"] + County["T1_est221"]
County["AS"] = sum_AS

sum_AA = County["T1_est14"] + County["T1_est55"] + County["T1_est96"] + County["T1_est138"] + County["T1_est179"] + County["T1_est220"]
County["AA"] = sum_AA

sum_Lat = County["T1_est18"] + County["T1_est59"] + County["T1_est100"] + County["T1_est142"] + County["T1_est183"] + County["T1_est224"]
County["Lat"] = sum_Lat

sum_PI = County["T1_est17"] + County["T1_est58"] + County["T1_est99"] + County["T1_est141"] + County["T1_est182"] + County["T1_est223"]
County["PI"] = sum_PI

sum_Wh = County["T1_est13"] + County["T1_est54"] + County["T1_est95"] + County["T1_est137"] + County["T1_est178"] + County["T1_est219"]
County["Wh"] = sum_Wh

sum_Other = County["T1_est19"] + County["T1_est60"] + County["T1_est101"] + County["T1_est143"] + County["T1_est184"] + County["T1_est225"]
County["Other"] = sum_Other

def MOE_gen(data, colnames):
    # data: A dataframe containing the MoE columns to be combined.
    # colnames: A list of strings that correspond to the names of MoE columns 
    #     to be combined.
    # Returns "moecomb", a series which can be added to dataframe "data."
    # Method from https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf
    
    # Obtain MoE of each component estimate (this came in the data frame).
    # Square the MoE of each component dataframe.
    sqrnames = list()
    for j in range(len(colnames)):
        sqrname_t = colnames[j] + '_sqrd'
        data[sqrname_t] = data[colnames[j]].pow(2.0)
        sqrnames.append(sqrname_t)
        
    # Sum the squared MoEs.
    data['sum_sqrs'] = 0
    for j in range(len(colnames)):
        data['sum_sqrs'] = data['sum_sqrs'] + data[sqrnames[j]]
        
    # Take the square root of the sum of the squared MoEs.
    moecomb = data['sum_sqrs'].pow(1./2.)
    
    # Drop added columns
    sqrnames.append('sum_sqrs')
    data = data.drop(columns = sqrnames)
    
    return(moecomb)

County['AI_me'] = MOE_gen(County, ['T1_moe16', 'T1_moe57', 'T1_moe98', 'T1_moe140', 'T1_moe181', 'T1_moe222'])
County['AS_me'] = MOE_gen(County, ['T1_moe15', 'T1_moe56', 'T1_moe97', 'T1_moe139', 'T1_moe180', 'T1_moe221'])
County['AA_me'] = MOE_gen(County, ['T1_moe15', 'T1_moe55', 'T1_moe96', 'T1_moe138', 'T1_moe179', 'T1_moe220'])
County['Lat_me'] = MOE_gen(County, ['T1_moe18', 'T1_moe59', 'T1_moe100', 'T1_moe142', 'T1_moe183', 'T1_moe224'])
County['PI_me'] = MOE_gen(County, ['T1_moe17', 'T1_moe58', 'T1_moe99', 'T1_moe141', 'T1_moe182', 'T1_moe223'])
County['Wh_me'] = MOE_gen(County, ['T1_moe13', 'T1_moe54', 'T1_moe95', 'T1_moe137', 'T1_moe178', 'T1_moe219'])
County['Other_me'] = MOE_gen(County, ['T1_moe19', 'T1_moe60', 'T1_moe101', 'T1_moe143', 'T1_moe184', 'T1_moe225'])

####Create a new dataframe with just the results
CountyResults = County[['name', 'T1_est1', 'AI', 'AI_me', 'AS', 'AS_me', 'AA', 'AA_me', 'Lat', 'Lat_me', 'PI', 'PI_me', 'Wh', 'Wh_me', 'Other', 'Other_me']]

###download the ouput
CountyResults.to_csv(r'K:\DataServices\Projects\Data_Requests\2020\HabitatforHumanity_CHASRaceEthnicity\Output\CountyResults.csv')



###the second part is for municipal level data (in Middlesex and Worceter counties)
Municipal = pd.read_csv (r'K:\DataServices\Projects\Data_Requests\2020\HabitatforHumanity_CHASRaceEthnicity\CHAS_Data_2012_2016\Table1.csv')
print (Municipal)

sum_AI = Municipal["T1_est16"] + Municipal["T1_est57"] + Municipal["T1_est98"] + Municipal["T1_est140"] + Municipal["T1_est181"] + Municipal["T1_est222"]
Municipal["AI"] = sum_AI

sum_AS = Municipal["T1_est15"] + Municipal["T1_est56"] + Municipal["T1_est97"] + Municipal["T1_est139"] + Municipal["T1_est180"] + Municipal["T1_est221"]
Municipal["AS"] = sum_AS

sum_AA = Municipal["T1_est14"] + Municipal["T1_est55"] + Municipal["T1_est96"] + Municipal["T1_est138"] + Municipal["T1_est179"] + Municipal["T1_est220"]
Municipal["AA"] = sum_AA

sum_Lat = Municipal["T1_est18"] + Municipal["T1_est59"] + Municipal["T1_est100"] + Municipal["T1_est142"] + Municipal["T1_est183"] + Municipal["T1_est224"]
Municipal["Lat"] = sum_Lat

sum_PI = Municipal["T1_est17"] + Municipal["T1_est58"] + Municipal["T1_est99"] + Municipal["T1_est141"] + Municipal["T1_est182"] + Municipal["T1_est223"]
Municipal["PI"] = sum_PI

sum_Wh = Municipal["T1_est13"] + Municipal["T1_est54"] + Municipal["T1_est95"] + Municipal["T1_est137"] + Municipal["T1_est178"] + Municipal["T1_est219"]
Municipal["Wh"] = sum_Wh

sum_Other = Municipal["T1_est19"] + Municipal["T1_est60"] + Municipal["T1_est101"] + Municipal["T1_est143"] + Municipal["T1_est184"] + Municipal["T1_est225"]
Municipal["Other"] = sum_Other

Municipal['AI_me'] = MOE_gen(Municipal, ['T1_moe16', 'T1_moe57', 'T1_moe98', 'T1_moe140', 'T1_moe181', 'T1_moe222'])
Municipal['AS_me'] = MOE_gen(Municipal, ['T1_moe15', 'T1_moe56', 'T1_moe97', 'T1_moe139', 'T1_moe180', 'T1_moe221'])
Municipal['AA_me'] = MOE_gen(Municipal, ['T1_moe15', 'T1_moe55', 'T1_moe96', 'T1_moe138', 'T1_moe179', 'T1_moe220'])
Municipal['Lat_me'] = MOE_gen(Municipal, ['T1_moe18', 'T1_moe59', 'T1_moe100', 'T1_moe142', 'T1_moe183', 'T1_moe224'])
Municipal['PI_me'] = MOE_gen(Municipal, ['T1_moe17', 'T1_moe58', 'T1_moe99', 'T1_moe141', 'T1_moe182', 'T1_moe223'])
Municipal['Wh_me'] = MOE_gen(Municipal, ['T1_moe13', 'T1_moe54', 'T1_moe95', 'T1_moe137', 'T1_moe178', 'T1_moe219'])
Municipal['Other_me'] = MOE_gen(Municipal, ['T1_moe19', 'T1_moe60', 'T1_moe101', 'T1_moe143', 'T1_moe184', 'T1_moe225'])


MunicipalResults = Municipal[['name', 'T1_est1', 'AI', 'AI_me', 'AS', 'AS_me', 'AA', 'AA_me', 'Lat', 'Lat_me', 'PI', 'PI_me', 'Wh', 'Wh_me', 'Other', 'Other_me']]


###download the ouput
MunicipalResults.to_csv(r'K:\DataServices\Projects\Data_Requests\2020\HabitatforHumanity_CHASRaceEthnicity\Output\MunicipalResults.csv')
