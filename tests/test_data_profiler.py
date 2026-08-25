import pandas as pd

from bizx.data import DataProfiler


def test_data_profiler():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [25, 30],
        }
    )

    profiler = DataProfiler(df)
    result = profiler.generate()

    assert result["rows"] == 2
    assert result["columns"] == 2