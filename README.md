# 🤔 Research Question (Tentative)
New: What is the impact of mobile cellular subscriptions on food supply in ASEAN and South Asian countries?

Old: To what extent is having a digital presence linked with improvements in financial inclusion and outcomes among the agricultural poor?

-> Link to original research question brainstorming [(here)](https://docs.google.com/presentation/d/1NucYbSjfVlvDEOBGqh_Ji_7gGyhjJVdJAMbRCjujQzY/edit?usp=sharing)

Empirical Model:

$$
\log(\text{Food Supply})_{it} = \beta_0 + \beta_1 \log(\text{Mobile Subscriptions})_{it} + \beta_2 X_{it} + \epsilon_{it}
$$


# 🤝 Our lovely Team Members (Alphabetical order)
- Heeyoung Kwon  
- Isabela Paredes  
- Nakada Shunichi  
- Rachel Ho  
- Wanzi Wang  
# 📒 Notebooks
1) Milestone One - [Notebook here](https://github.com/Graspp-25-Spring/graspp_2025s_fintech/blob/main/notebooks/Milestone_1.ipynb)
2) Milestone Two - [Notebook here](https://github.com/Graspp-25-Spring/graspp_2025s_fintech/blob/main/notebooks/Milestone_2.ipynb)
                 - [Visualization here](https://github.com/Graspp-25-Spring/graspp_2025s_fintech/blob/main/notebooks/Visualizations_One.ipynb)


# 💻 Data Files
1) Milestone One - [processed CSV here](https://github.com/Graspp-25-Spring/graspp_2025s_fintech/blob/main/data/processed/wb_merged.csv)
2) Milestone Two - [processed CSV here](https://github.com/Graspp-25-Spring/graspp_2025s_fintech/blob/main/data/processed/merged_5.csv)


# 💭 Hypotheses regarding the data
1.	Access to electricity, higher rates of fixed broadband and mobile cellular subscriptions correlate with higher use of financial services via traditional financial institutions (FI) and mobile money.
2.	Access to electricity, higher rates of fixed broadband and mobile cellular subscriptions correlate with higher fertilizer consumption and value-add for agriculture.
3.	Owning a mobile money account is not directly correlated to access to financial institutions. (In certain regions, e.g. Indonesia, this is the case—mobile money had much more penetration than banks.)
4.	Ownership of mobile money account and/or access to financial institutions are correlated with higher fertilizer consumption and value-add for agriculture. (Perhaps more importantly, we want to know by what degree this is true.)
5.	Access to financial institutions is higher among urban rather than rural populations (Perhaps more importantly, we want to know by what degree this is true.)
6.	Areas with higher population densities are likely to have higher access to financial services.
7.	Areas with higher population densities are likely to have higher fertilizer consumption and value-add for agriculture.
8.	GDP per capita (+), poverty headcount (-), higher life expectancy at birth (+), and population densities (+) are correlated with higher financial access. (in the direction indicated in parentheses)
9.	GDP per capita (+), poverty headcount (-), higher life expectancy at birth (+), and population densities (+) are correlated with higher fertilizer consumption and value-add for agriculture. (in the direction indicated in parentheses)


# 📈 Current Datasets
**X Variables (Not all will be used, many for purpose of painting larger picture**
| Variable Name | Dataset | Indicator ID | Indicator Link | Cleaned? |
|---------------|---------|--------------|----------------|----------|
| Fixed Broadband Subscriptions (per 100 people) | WDI | IT.NET.BBND.P2 | https://data.worldbank.org/indicator/IT.NET.BBND.P2?view=chart | Y |
| Mobile Cellular Subscriptions (per 100 people) | WDI | IT.CEL.SETS.P2 | https://data.worldbank.org/indicator/IT.CEL.SETS.P2?view=chart | Y |
| Access to Electricity, rural (% of Rural Pop.) | WDI | EG.ELC.ACCS.RU.ZS | https://data.worldbank.org/indicator/EG.ELC.ACCS.RU.ZS | Y |
| Account (% age 15+) | Findex | 'account.t.d' | | N |
| Account, female (% age 15+) | Findex | 'account.t.d.1' | | N |
| Account, male (% age 15+) | Findex | 'account.t.d.2' | | N |
| Account, rural (% age 15+) | Findex | 'account.t.d.9' | | N |
| Account, urban (% age 15+) | Findex | 'account.t.d.10' | | N |
| Financial institution account (% age 15+) | Findex | 'fin1.t.d' | | N |
| Financial institution account, female (% age 15+) | Findex | 'fin1.t.d.1' | | N |
| Financial institution account, male (% age 15+) | Findex | 'fin1.t.d.2' | | N |
| Financial institution account, rural (% age 15+) | Findex | 'fin1.t.d.9' | | N |
| Financial institution account, urban (% age 15+) | Findex | 'fin1.t.d.10' | | N |
| Mobile money account (% age 15+) | Findex | 'mobileaccount.t.d' | | N |
| Mobile money account, female (% age 15+) | Findex | 'mobileaccount.t.d.1' | | N |
| Mobile money account, male (% age 15+) | Findex | 'mobileaccount.t.d.2' | | N |
| Mobile money account, rural (% age 15+) | Findex | 'mobileaccount.t.d.9' | | N |
| Mobile money account, urban (% age 15+) | Findex | 'mobileaccount.t.d.10' | | N |
| Own a mobile phone (% age 15+) | Findex | 'Own.phone' | | N |
| Owns a debit or credit card (% age 15+) | Findex | 'fin2.7.t.d' | | N |
| Owns a debit or credit card, female (% age 15+) | Findex | 'fin2.7.t.d.1' | | N |
| Owns a debit or credit card, male (% age 15+) | Findex | 'fin2.7.t.d.2' | | N |
| Owns a debit or credit card, rural (% age 15+) | Findex | 'fin2.7.t.d.9' | | N |
| Owns a debit or credit card, urban (% age 15+) | Findex | 'fin2.7.t.d.10' | | N |

**Control Variables (Demographic)**
| Variable Name | Dataset | Indicator ID | Indicator Link | Cleaned? |
|---------------|---------|--------------|----------------|----------|
| Population, total | WDI | SP.POP.TOTL | https://data.worldbank.org/indicator/SP.POP.TOTL | Y |
| Urban population (% of total population)| WDI | SP.URB.TOTL.IN.ZS | https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS | Y |
| Rural population (% of total population)| WDI | SP.RUR.TOTL.ZS | https://data.worldbank.org/indicator/SP.RUR.TOTL.ZS | Y |
| Life expectancy at birth, total (years) | WDI | SP.DYN.LE00.IN | https://data.worldbank.org/indicator/SP.DYN.LE00.IN | Y |
| Mortality rate, infant (per 1,000 live births) | WDI | SP.DYN.IMRT.IN | https://data.worldbank.org/indicator/SP.DYN.IMRT.IN | Y |
| Population density (people per sq. km of land area) | WDI | EN.POP.DNST | https://data.worldbank.org/indicator/EN.POP.DNST | Y |
| Poverty headcount ratio at national poverty lines (% of population) | WDI | SI.POV.NAHC | https://data.worldbank.org/indicator/SI.POV.NAHC | Y |
| Population growth (annual %) | WDI | SP.POP.GROW | https://data.worldbank.org/indicator/SP.POP.GROW | Y | 
| Fertility rate, total (births per woman) | WDI | SP.DYN.TFRT.IN | https://data.worldbank.org/indicator/SP.DYN.TFRT.IN | Y |
| GDP per capita, PPP (constant 2021 international $) | WDI | NY.GDP.PCAP.PP.KD | https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD | Y |

**Y Variables**
| Variable Name | Dataset | Indicator ID | Indicator Link | Cleaned? |
|---------------|---------|--------------|----------------|----------|
| Credit to Agriculture| WB_FAO|FAO_IC_23068|https://data360.worldbank.org/en/indicator/FAO_IC_23068| Y |
|Value Added (Agriculture, Forestry and Fishing)| WB_FAO|FAO_MK_22016|https://data360.worldbank.org/en/api?indicatorid=FAO_MK_22016&datasetid=FAO_MK#/Data/get_data360_data| Y |
|Value Added (Manufacture of food and beverages)| WB_FAO | FAO_MK_22077|https://data360.worldbank.org/en/api?indicatorid=FAO_MK_22077&datasetid=FAO_MK#/Data/get_data360_data| Y |
|Fertilizer consumption (kilograms per hectare of arable land)| WB_FAO |WB_WDI_AG_CON_FERT_ZS|https://data360.worldbank.org/en/api? indicatorid=WB_WDI_AG_CON_FERT_ZS&datasetid=WB_WDI#/Data/get_data360_data| Y |
| Use of Financial Services, Number of mobile money transactions (during the reference year) | Financial Access Survey, IMF | IMF_FAS_FCMT | https://data.imf.org/en/Data-Explorer?datasetUrn=IMF.STA:FAS(4.0.0)&INDICATOR=FA66N | N |
| Use of Financial Services, Value of mobile money transactions (during the reference year) | Financial Access Survey, IMF | IMF_FAS_FCMTV | https://data.imf.org/en/Data-Explorer?datasetUrn=IMF.STA:FAS(4.0.0)&INDICATOR=FA65 | N |
| Use of Financial Services, Number of active mobile money accounts | Financial Access Survey, IMF | IMF_FAS_FCMAA | https://data.imf.org/en/Data-Explorer?datasetUrn=IMF.STA:FAS(4.0.0)&INDICATOR=FA63N | N |
