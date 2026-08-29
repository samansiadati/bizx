import io
import os
from typing import Optional

import pandas as pd
from pandas.io.common import file_path_to_url


def get_file(file_name: str, file_path: Optional[str] = None) -> str:
    """
    Build a local file path from a file name and optional directory.
    """
    return os.path.join(file_path or "", file_name)


def get_url(file_name: str, file_url: Optional[str] = None) -> str:
    """
    Build a file URL from a file name and optional base URL/path.
    """
    return file_path_to_url(os.path.join(file_url or "", file_name))


def open_csv(
    file_name: str,
    file_path: Optional[str] = None,
    **kwargs,
) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame.
    """
    return pd.read_csv(get_file(file_name, file_path), **kwargs)


def open_excel(
    file_name: str,
    file_path: Optional[str] = None,
    **kwargs,
) -> pd.DataFrame:
    """
    Read an Excel file into a Pandas DataFrame.
    """
    return pd.read_excel(get_file(file_name, file_path), **kwargs)


def open_json(
    file_name: str,
    file_path: Optional[str] = None,
    **kwargs,
) -> pd.DataFrame:
    """
    Read a JSON file into a Pandas DataFrame.
    """
    return pd.read_json(get_file(file_name, file_path), **kwargs)


def pandas_schema(df: pd.DataFrame) -> pd.Series:
    """
    Return the data type of each DataFrame column.
    """
    return df.dtypes


def pandas_schema_report(df: pd.DataFrame) -> str:
    """
    Return a human-readable DataFrame schema report.
    """
    buffer = io.StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()


def pandas_cardinality(df: pd.DataFrame) -> pd.Series:
    """
    Return the number of unique values for each column.
    """
    return df.nunique()


def pandas_value_counts(df: pd.DataFrame) -> dict:
    """
    Return value-frequency distributions for each column.
    """
    return {
        column: df[column].value_counts()
        for column in df.columns
    }


def pandas_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics for the DataFrame.
    """
    return df.describe(include="all")


def pandas_save_csv(
    df: pd.DataFrame,
    path: str,
    index: bool = False,
    encoding: str = "utf-8",
    **kwargs,
) -> None:
    """
    Save a DataFrame to a CSV file.
    """
    df.to_csv(
        path,
        index=index,
        encoding=encoding,
        **kwargs,
    )



def remove_quotes(
    file_path: str,
    output_path: str,
) -> pd.DataFrame:
    """
    Remove single and double quotes from CSV column names
    and string values.

    Returns:
        The cleaned Pandas DataFrame.
    """
    df = pd.read_csv(file_path, dtype=str)

    df.columns = [
        column.replace('"', "").replace("'", "")
        for column in df.columns
    ]

    for column in df.select_dtypes(include="object").columns:
        df[column] = (
            df[column]
            .str.replace('"', '', regex=False)
            .str.replace("'", '', regex=False)
        )

    df.to_csv(output_path, index=False)

    return df