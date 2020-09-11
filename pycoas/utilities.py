import numpy as np
import pandas as pd


def reduce_memory_usage(df, verbose=True):
    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024 ** 2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    end_mem = df.memory_usage().sum() / 1024 ** 2

    if verbose:
        print(
            "Memory usage decreased to {:5.2f} MB ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )

    return df


def show_unique_values(df):
    object_cols = list(df.select_dtypes(include=["object"]).columns)
    unique_counts = pd.DataFrame.from_records(
        [(col, df[col].nunique()) for col in df.columns],
        columns=["Column_Name", "#_Unique"],
    ).sort_values(by=["#_Unique"])
    unique_object_counts = pd.DataFrame.from_records(
        [(col, df[col].nunique()) for col in object_cols],
        columns=["Column_Name", "#_Unique"],
    ).sort_values(by=["#_Unique"])

    print(
        "Number of columns: {}\nNumber of object columns: {}".format(
            unique_counts.shape[0], unique_object_counts.shape[0]
        )
    )

    unique_counts = (
        unique_counts.style.hide_index()
        .bar("#_Unique", color="lightblue", align="left")
        .set_caption("All columns")
    )
    unique_object_counts = (
        unique_object_counts.style.hide_index()
        .bar("#_Unique", color="lightblue", align="zero")
        .set_caption("Object oolumns")
    )

    return display(unique_counts, unique_object_counts)
