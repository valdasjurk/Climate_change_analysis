# Source: https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

import kaggle
import pandas as pd

DIRECTORY = "data/raw/GlobalLandTemperaturesByCity.csv"


def download_dataset():
    kaggle.api.dataset_download_files(
        dataset="berkeleyearth/climate-change-earth-surface-temperature-data",
        path="input_data_climate",
        unzip=True,
        quiet=False,
        force=False,
    )


def read_dataset():
    df = pd.read_csv(DIRECTORY)
    df = df.drop_duplicates()
    return df


""" indexing and filtering exercises"""


def pick_specific_column(df):
    print(df["Country"])
    print(df[["Country"]])
    print(df.loc[:, ["Country"]])
    print(df.iloc[:, 4])
    print(df.Country)  # not recomended


def pick_specific_2_columns(df):
    print(df[["City", "Country"]])
    print(df.loc[:, ["City", "Country"]])
    print(df.iloc[:, [3, 4]])
    print(df[df.columns[3:5]])


def pick_specific_row(df):
    row_based_on_country_and_date = df.loc[
        (df["Country"] == "Denmark")
        & (df["dt"] == "1743-11-01")
        & (df["City"] == "Aalborg")
    ]
    print(row_based_on_country_and_date)
    print(df.iloc[2])
    print(df.iloc[500:502])
    print(df.loc[1])
    print(df.query("City == 'Aalborg'"))


# When df is indexed with integers, you can use the .loc and .iloc methods interchangeably, how they are different?
# - The loc() function is label based data selecting method, while iloc is index based method.


# Create a dataframe and display the difference:
def loc_iloc_difference(df):
    loc_method = df.loc[:, "Country"]
    print(loc_method)
    iloc_method = df.iloc[:, 4]
    print(iloc_method)


def reasonable_masks(df):
    below_zero = df[df["AverageTemperature"] < 0]
    print(below_zero)
    df["dt"] = pd.to_datetime(df["dt"])
    year_filtering = df[df["dt"].dt.year > 2000]
    print(year_filtering)
    XIX_century_data = df[(df["dt"].dt.year >= 1800) & (df["dt"].dt.year < 1900)]
    print(XIX_century_data)
    is_containing_nan = df["AverageTemperature"].isna()
    print(is_containing_nan)
    summer_time_data = df[(df["dt"].dt.month >= 6) & (df["dt"].dt.month <= 8)]
    print(summer_time_data)


def create_new_column(df, column, column_name):
    df[column_name] = column
    return df


def remove_str_part(df, col, what_to_remove):
    replacement = df[col].str.replace(what_to_remove, "")
    df = create_new_column(df, replacement, "Latitude_raw")
    return df


if __name__ == "__main__":
    # download_dataset()
    df = read_dataset()
    print(df.head())
    df = remove_str_part(df, "Latitude", "N")
    print(df)
    # pick_specific_column(df)
    # pick_specific_2_columns(df)
    # pick_specific_row(df)
    # loc_iloc_difference(df)
    # reasonable_masks(df)
