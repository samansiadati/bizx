from __future__ import annotations

import pandas as pd


class DataProfiler:
    """Basic profiling utilities for pandas DataFrames."""

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def generate(self) -> dict:
        """Generate a basic data profile."""
        df = self.dataframe

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": df.isna().sum().to_dict(),
            "dtypes": df.dtypes.astype(str).to_dict(),
        }