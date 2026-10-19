import pandas as pd
from pathlib import Path

folder = Path(__file__).parent
file_path = folder / "Online_Retail_Original .xlsx"
df = pd.read_excel(file_path)
print("Dataset loaded successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))


print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nMissing Values in each columns:")
print(df.isnull().sum())


print("\nColumn data types:")
print(df.dtypes)


print("\nDuplicate record:")
print(df.duplicated().sum())

print("\nSample duplicate records")
print(df[df.duplicated(keep=False)].head(10))


print("\nExact duplicate row details:")
print(df[df.duplicated(keep=False)].loc[[548, 555]].to_string())


df_no_duplicates = df.drop_duplicates()

print("\nOriginal row count:", len(df))
print("Rows after removing exact duplicates:", len(df_no_duplicates))
print("Duplicate rows identified:", len(df) - len(df_no_duplicates))


missing_description = df[df["Description"].isnull()]

print("\nRows with missing Description:")
print("Total rows:", len(missing_description))
print(
    missing_description[["InvoiceNo", "StockCode", "Quantity", "UnitPrice", "Country"]]
    .head(10)
    .to_string(index=False)
)


description_lookup = (
    df.dropna(subset=["Description"])
    .drop_duplicates(subset=["StockCode"])
    .set_index("StockCode")["Description"]
)

recoverable = missing_description["StockCode"].map(description_lookup)

print("\nDescription recovery check:")
print("Missing descriptions:", len(missing_description))
print("Potentially recoverable rows:", recoverable.notna().sum())
print("Still unmatched rows:", recoverable.isna().sum())


print(missing_description["StockCode"].head(5))


print(df.loc[df["StockCode"] == "22139", "Description"])


print(
    df.loc[
        df["StockCode"].astype(str).str.strip() == "22139", ["StockCode", "Description"]
    ].head()
)


print(
    df.loc[
        df["StockCode"].astype(str).str.strip() == "22139", "Description"
    ].value_counts(dropna=False)
)


print(
    df.loc[
        (df["StockCode"].astype(str).str.strip() == "22139")
        & (df["Description"].isna()),
        ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"],
    ]
)


print(missing_description["StockCode"].nunique())

print(
    missing_description["StockCode"]
    .isin(df.loc[df["Description"].notna(), "StockCode"])
    .sum()
)

print(len(missing_description))


print(df.groupby("StockCode")["Description"].nunique().max())


print((df.groupby("StockCode")["Description"].nunique() > 1).sum())


print(
    df.loc[
        df["Description"].str.lower().eq("amazon"), ["StockCode", "Description"]
    ].head(10)
)


print(df["Description"].str.strip().str.lower().value_counts().head(10))


print(df["Description"].str.strip().str.lower().eq("amazon").sum())


df_clean = df.drop_duplicates().copy()


print(len(df_clean))

df_clean["Description"] = df_clean["Description"].map(
    lambda x: x.strip() if isinstance(x, str) else x
)

print(df_clean["Description"].str.startswith(" ").sum())

print(df_clean["Description"].str.endswith(" ").sum())


print(df_clean["Description"].isna().sum())

print(
    "Original:",
    df["Description"].isna().sum(),
    "| Cleaned:",
    df_clean["Description"].isna().sum(),
)

print(df_clean[df_clean["Description"].isna()].tail(3).index.tolist())

print(df.loc[[535332, 536981, 538554], ["InvoiceNo", "StockCode", "Description"]])

print(df_clean.loc[535332, "Description"])

print(df_clean.index.equals(df.index))


print("Missing before strip:", df_clean["Description"].isna().sum())
print("Empty strings:", df_clean["Description"].eq("").sum())
print(
    df.loc[
        df["Description"].notna()
        & ~df["Description"].map(lambda x: isinstance(x, str)),
        ["InvoiceNo", "StockCode", "Description"],
    ].to_string(index=False)
)

print("Missing:", df_clean["Description"].isna().sum())
print(
    "Leading/trailing spaces:",
    df_clean["Description"].map(lambda x: isinstance(x, str) and x != x.strip()).sum(),
)
print("Missing Description:", df_clean["Description"].isna().sum())

print(
    "Recoverable StockCodes:",
    df_clean.loc[df_clean["Description"].isna(), "StockCode"]
    .isin(df_clean.loc[df_clean["Description"].notna(), "StockCode"])
    .sum(),
)
print(
    "StockCodes with multiple descriptions:",
    (df_clean.groupby("StockCode")["Description"].nunique() > 1).sum(),
)

print(
    df_clean.groupby("StockCode")["Description"].nunique().value_counts().sort_index()
)
print(
    "Missing rows with one unique description:",
    df_clean.loc[df_clean["Description"].isna(), "StockCode"]
    .map(
        df_clean.dropna(subset=["Description"])
        .groupby("StockCode")["Description"]
        .nunique()
    )
    .eq(1)
    .sum(),
)

description_lookup = (
    df_clean.dropna(subset=["Description"])
    .groupby("StockCode")["Description"]
    .agg("first")
)

mask = df_clean["Description"].isna() & df_clean["StockCode"].map(
    df_clean.dropna(subset=["Description"])
    .groupby("StockCode")["Description"]
    .nunique()
).eq(1)

df_clean.loc[mask, "Description"] = df_clean.loc[mask, "StockCode"].map(
    description_lookup
)

print("Missing descriptions after recovery:", df_clean["Description"].isna().sum())

print("Descriptions recovered:", 1454 - df_clean["Description"].isna().sum())
print("Missing CustomerID:", df_clean["CustomerID"].isna().sum())

print("Negative Quantity records:", (df_clean["Quantity"] < 0).sum())

print("Negative UnitPrice records:", (df_clean["UnitPrice"] < 0).sum())
print("Zero UnitPrice records:", (df_clean["UnitPrice"] == 0).sum())
print(df_clean.dtypes)
print("Remaining exact duplicates:", df_clean.duplicated().sum())
output_path = folder / "Online_Retail_Cleaned.xlsx"
df_clean.to_excel(output_path, index=False)

print("Final dataset shape:", df_clean.shape)
print("Remaining missing values:\n", df_clean.isna().sum())
print("Saved file:", output_path)
