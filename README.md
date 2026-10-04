# Generic Buy Now, Pay Later Project
Groups should generate their own suitable `README.md`.

Note to groups: Make sure to read the `README.md` located in `./data/README.md` for details.

# Members
`Paulina Leal Mosqueda` |
`Nhi Ngo` | 
`Sarah Ong` |
`Catherine Van Gerrevink` |
`Zikra Zuhuree` |

# Running the Files
Files should be run in the order described below.
1. `01_consumers_preprocess.ipynb` - preprocesses consumer data
2. `02_merchant_preprocess.ipynb` - preprocesses merchant data
3. `03_transactions_preprocess.ipynb` - preprocesses transaction data and joins with consumer and merchant data
4. `04_external_preprocess.ipynb` - preprocesses external ABS dataset and merges with BNPL data
5. `05_external_final_merge.ipynb` - preprocesses external RBA dataset and merges with previous dataset

## External Data: ABS Census 

### notebook: `04_external_preprocess.ipynb`

### Purpose: Build census-based features (such as median household income) that can be joined to customer/merchant/transaction data. Motivation for these features is based on typical trends of BNPL users being younger, or having lower average income. 

### Files 
| `2021Census_G02_AUST_SA2.csv` | Medians: age, personal/family/household income, rent, mortgage repayments; avg household size; avg persons per bedroom |
| `2021Census_G04A_AUST_SA2.csv`, `2021Census_G04B_AUST_SA2.csv` | Age by single year (joined on `SA2_CODE_2021`) |
| `POA_2021_AUST_GDA2020.shp` | Postcode boundaries |
| `SA2_2021_AUST_GDA2020.shp` | SA2 boundaries |
| `data/curated/df_transactions`, `df_merchants` | Internal data to merge with |



