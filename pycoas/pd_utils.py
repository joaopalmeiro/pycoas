from typing import Tuple

import pandas as pd
from pandas.io.formats.style import Styler


def show_unique_values(df: pd.DataFrame, verbose: bool = True) -> Tuple[Styler, Styler]:
    object_cols = list(df.select_dtypes(include=["object"]).columns)

    unique_counts = pd.DataFrame.from_records(
        [(col, df[col].nunique()) for col in df.columns],
        columns=["Column_Name", "#_Unique"],
    ).sort_values(by=["#_Unique"])
    unique_object_counts = pd.DataFrame.from_records(
        [(col, df[col].nunique()) for col in object_cols],
        columns=["Column_Name", "#_Unique"],
    ).sort_values(by=["#_Unique"])

    if verbose:
        print(
            "Number of columns: {}\nNumber of object columns: {}".format(
                unique_counts.shape[0], unique_object_counts.shape[0]
            )
        )

    # `vmin`: When `None`, the minimum value of the data will be used.
    unique_counts = (
        unique_counts.style.hide_index()
        .bar("#_Unique", color="lightblue", align="left", vmin=0)
        .set_caption("All columns")
    )
    unique_object_counts = (
        unique_object_counts.style.hide_index()
        .bar("#_Unique", color="lightblue", align="left", vmin=0)  # or `align="zero"`
        .set_caption("Object columns")
    )

    return unique_counts, unique_object_counts
