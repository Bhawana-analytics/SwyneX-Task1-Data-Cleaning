# SwyneX Task 1 — Data Cleaning Project

## Project Overview

This project focuses on cleaning and preparing the Online Retail dataset using Python and Pandas.

The objective is to identify and handle data quality issues, including duplicate records, missing values, inconsistent text formatting, and data type validation, while preserving valid business records.

## Tools and Technologies

- Python
- Pandas
- Excel
- Visual Studio Code

## Dataset

The project uses the Online Retail dataset, which contains transaction details such as invoice numbers, product codes, descriptions, quantities, invoice dates, unit prices, customer IDs, and countries.


## Data Cleaning Steps

1. Loaded the original Excel dataset using Pandas.
2. Inspected column names, data types, missing values, and duplicate records.
3. Removed exact duplicate rows.
4. Removed leading and trailing spaces from text descriptions while preserving non-text values.
5. Recovered missing product descriptions only when the corresponding StockCode had exactly one distinct available description.
6. Preserved unresolved missing descriptions instead of guessing values.
7. Reviewed missing CustomerID values.
8. Identified negative quantities, negative unit prices, and zero unit prices for further business interpretation.
9. Validated data types and checked for remaining exact duplicates.
10. Exported the cleaned dataset to a separate Excel file.

## Data Cleaning Results

| Check | Result |
|---|---:|
| Original records | 541,909 |
| Exact duplicate rows removed | 5,268 |
| Final records | 536,641 |
| Missing descriptions recovered | 1,033 |
| Missing descriptions remaining | 421 |
| Missing CustomerID values remaining | 135,037 |
| Negative Quantity records | 10,587 |
| Negative UnitPrice records | 2 |
| Zero UnitPrice records | 2,510 |
| Remaining exact duplicates | 0 |
| Description leading/trailing spaces | 0 |

## Output File

The cleaned dataset is saved as `Online_Retail_Cleaned.xlsx`.

The original dataset, `Online_Retail_Original .xlsx`, was kept unchanged.

## Important Notes

- Missing CustomerID values were retained because reliable replacement values were not available.
- Negative quantities may represent returns or cancellations.
- Negative and zero unit prices were retained for business review rather than deleted automatically.
- The 421 unresolved missing descriptions were preserved instead of being filled with unverified values.

## Conclusion

This project demonstrates practical data cleaning using Python and Pandas, including duplicate removal, missing-value analysis, safe description recovery, data type validation, and exporting the cleaned dataset for further analysis.

## Dataset Attribution

Source: [UCI Machine Learning Repository — Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)

Original dataset: Chen, D. (2015). *Online Retail*. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33

License: Creative Commons Attribution 4.0 International (CC BY 4.0).

The original dataset was cleaned and modified using Python and Pandas for this project.