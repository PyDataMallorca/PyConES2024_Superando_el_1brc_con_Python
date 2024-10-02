# -*- coding: utf-8 -*-
"""
Genera fichero de datos en distintos formatos

Workshop PyConES 2024

Autores:
Ernesto Coloma
Jordi Contestí
Kiko Correoso
"""

from typing import Optional
from pathlib import Path
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

import duckdb
import pyarrow.feather as feather
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def _get_filename(
    filename: str, fmt: str, compression: Optional[str]
) -> str:
    filename = f"{filename}.{fmt}"
    if compression:
        filename += f".{compression}"
    return filename

def generate_sample_data(
    lines: Optional[int] = 50_000_000,
    fmt: str = "csv",
    filename: str = "sample",
    compression: Optional[str] = None,
) -> None:
    """
    Generates sample data and saves it to a file in the specified format.

    Args:
        lines (int, optional): Number of data lines to generate (by default 50_000_000).
        fmt (str, optional): Format for saving the data (default is "csv").
            Allowed formats: "csv", "feather", "parquet".
        filename (str, optional): Base filename for the saved data (default is "sample").
        compression (str, optional): Compression method for the saved file (e.g., "gzip", "bz2").
            Not applicable to all formats.

    Returns:
        None: The generated data is saved to a file.

    Raises:
        None

    Example:
        generate_sample_data(lines=1000, fmt="parquet", filename="my_data", compression="gzip")
    """
    allowed_formats = ("csv", "feather", "parquet")
    if compression == "gzip":
        fn = _get_filename(filename, fmt, "gz")
    else:
        fn = _get_filename(filename, fmt, compression)
    query = f"""
            SELECT 
                list_extract(
                    array_value('A', 'B', 'C', 'D', 'E', 'F'),
                    CAST(CEIL(random() * 6) AS INTEGER)
                ) AS product, 
                CAST(5 + random() * 110 AS INTEGER) AS price
            FROM range({lines})
            """
    set_seed = f"""
            SELECT setseed(0.42);
            """

    if not Path(fn).is_file():
        match fmt:
            case "csv":
                duckdb.sql(f"""
                    {set_seed}
                    COPY (
                        {query}
                    ) TO '{fn}' (FORMAT '{fmt}', COMPRESSION '{compression}')
                """)

            case "parquet":
                if not compression:
                    compression = 'uncompressed'
                duckdb.sql(f"""
                    {set_seed}
                    COPY (
                        {query}
                    ) TO '{fn}' (FORMAT '{fmt}', COMPRESSION '{compression}')
                """)
                
            case "feather":
                arr = duckdb.sql(f"""{set_seed}{query}""").arrow()

                with open(fn, 'wb') as f:
                    feather.write_feather(arr, f, compression="zstd")

            case _:
                print(
                    "This format is not allowed.\n"
                    "Please, use any of the following options:\n"
                    f"\t{allowed_formats}"
                )
                return None
    else:
        print(f"File {fn} already exists. Not created!!")
        return None
    
def generate_heatmap(df: pd.DataFrame, title: str) -> None:
    """
    Generates a heatmap from a given DataFrame and displays it with customized color scaling.

    Args:
        df (pd.DataFrame): The input DataFrame containing numeric data for the heatmap.
        title (str): The title of the heatmap to be displayed above the plot.

    Returns:
        None: The function creates and displays the heatmap without returning any value.

    Details:
        - The function attempts to convert all data in the DataFrame to numeric values using `pd.to_numeric` 
          (non-numeric data is coerced to NaN).
        - A custom colormap is used, transitioning from bright green (low values) to red (high values), with white 
          centered around the median value.

    Example:
        generate_heatmap(df=my_dataframe, title="My Heatmap")
    """
    df_numeric = df.apply(pd.to_numeric, errors='coerce')
    colors = [(0.0, 0.7, 0.0), (1, 1, 1), (1, 0, 0)]
    cmap_name = 'bright_green_red'
    n_bins = 20
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    fig, ax = plt.subplots(figsize=(10, 6))
    vmin = df_numeric.min().min()
    median_value = df_numeric.median().median()
    vmax = df_numeric.max().max()
    norm = TwoSlopeNorm(vmin=vmin, vcenter=median_value, vmax=vmax)

    cax = ax.imshow(df_numeric, cmap=custom_cmap, norm=norm)

    for (i, j), val in np.ndenumerate(df_numeric.values):
        if not np.isnan(val):
            ax.text(j, i, f'{val:.4f}', va='center', ha='center', color='black')

    ax.set_xticks(np.arange(df_numeric.shape[1]))
    ax.set_yticks(np.arange(df_numeric.shape[0]))
    ax.set_xticklabels(df_numeric.columns, rotation=45, ha='left')
    ax.set_yticklabels(df_numeric.index)
    ax.tick_params(axis='x', which='both', length=0)
    ax.xaxis.set_ticks_position('top')
    ax.set_title(title, fontsize=12, pad=20)
    ax.grid(False)

    plt.show()
    return None