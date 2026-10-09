# External Data: ABS Census 

Source URL: https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=SA2&header=S

notebook: `04_external_preprocess.ipynb`

## Purpose: Build census-based features (such as median household income) that can be joined to customer/merchant/transaction data. Motivation for these features is based on typical trends of BNPL users being younger, or having lower average income. 

### Files 
| `2021Census_G02_AUST_SA2.csv` | Medians: age, personal/family/household income, rent, mortgage repayments; avg household size; avg persons per bedroom |
| `2021Census_G04A_AUST_SA2.csv`, `2021Census_G04B_AUST_SA2.csv` | Age by single year (joined on `SA2_CODE_2021`) |
| `POA_2021_AUST_GDA2020.shp` | Postcode boundaries |
| `SA2_2021_AUST_GDA2020.shp` | SA2 boundaries |
| `data/curated/df_transactions`, `df_merchants` | Internal data to merge with |

# External Data: SEIFA (POA) data

Source URL: https://services-ap1.arcgis.com/ypkPEy1AmwPKGNNv/ArcGIS/rest/services

notebook: `05_external_final_merge.ipynb`

## Purpose: Build macroeconomic-based features. Imported the POA data which highlighted the postal codes of all the areas within Australia to see which consumers were purchasing what from where. This was in order to establish a demographic base in terms of socio-economic standard and done by mapping all the postcodes onto the merchant dataset to see which transactions took place in what regions.

### Files:
| `ABS_Socio_Economic_Indexes_for_Areas_SEIFA_by_2021_POA` | Ranks areas according to relative socio-economic disadvantage by postcode (POA) |

# External Data: RBA and POA data

Source URL: https://www.rba.gov.au/statistics/cash-rate/

notebook: `05_external_final_merge.ipynb`

## Purpose: Imported the RBA data which shows the monthly interest rates across the 2021-2022 calendar year to see how merchants are affected by changing prices and if this affects the consumer base heavily.

### Files:
| `Cash Rate Target _ RBA.html` | Interest rates and relative change in Australia for a given date |