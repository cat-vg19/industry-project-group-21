# Generic Buy Now, Pay Later Project
Groups should generate their own suitable `README.md`.

Note to groups: Make sure to read the `README.md` located in `./data/README.md` for details.

# Members
`Paulina Leal Mosqueda` |
`Nhi Ngo` | 
`Sarah Ong` |
`Catherine Van Gerrevink` |
`Zikra Zuhuree`

# Running the Files
Files should be run in the order described below.
**1. Preprocessing** (`notebooks/`)
1. `01_consumers_preprocess.ipynb` - preprocesses consumer data
2. `02_merchant_preprocess.ipynb` - preprocesses merchant data
3. `03_transactions_preprocess.ipynb` - preprocesses transaction data and joins it with consumer and merchant data
4. `04_external_preprocess.ipynb` - preprocesses the external ABS datasets and merges them with the BNPL data
5. `05_external_final_merge.ipynb` - preprocesses the external RBA dataset and merges it with the previous dataset
6. `06_exploratory_analysis.ipynb` - exploratory analysis and geospatial visualisations

**3. Fraud labels** (`models/`)

7. `01_Label_merchants.ipynb` - labels merchants as fraud or not fraud (`merchant_fraud_labels.parquet`)
8. `02_Label_consumer.ipynb` - labels consumer transactions as fraud or not fraud (`consumer_fraud_labels.parquet`)
9. `03_Create_is_fraud.ipynb` - combines both labels into the `is_fraud` column (`transactions_with_is_fraud_full`)
10. `04_Model_predict.ipynb` - simple model to predict whether a future transaction may be fraud.
11. `iterative/01_label_merchant_iter.ipynb` - iterative and bootstrap self-training for the merchant labels.

**4. Ranking** (`notebooks/`)

12. `07_vol_rankings.ipynb` - first ranking based on take rate, dollar value and number of transactions, with a
    train/test split by date. Its metrics and split dates are reused in `10_feature_analysis`.
13. `08_start-ranking.ipynb` - first ranking using the `is_essential` feature.
14. `09_modelling.ipynb` - builds the consumer feature table (`consumer_features`), including the demographic tags,
    and models the effect of the RBA cash rate.
15. `10_feature_analysis.ipynb` - analyses which features separate merchants and justifies the ones used in the ranking.
16. `11_final_ranking.ipynb` - builds the final ranking: top 100 merchants overall and top 10 merchants per segment.
17. `12_summary.ipynb` - summary of the approach, results, issues and limitations.