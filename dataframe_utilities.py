def drop_rows_by_value(df, column_name, value_to_drop):
    """
    Drops rows from a DataFrame where the specified column has a given value.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to check for the value.
    value_to_drop: The value in the column that, if matched, will result in the row being dropped.

    Returns:
    pd.DataFrame: A new DataFrame with the specified rows dropped.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    filtered_df = df[df[column_name] != value_to_drop]
    return filtered_df

def drop_rows_by_value_or_na(df, column_name=None, value_to_drop=None):
    """
    Drops rows from a DataFrame based on the following:
    1. If `value_to_drop` is specified, rows where the specified column has the given value will be dropped.
    2. Rows with missing values (NaN) will also be dropped.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str, optional): The name of the column to check for the value. Default is None.
    value_to_drop (optional): The value in the column that, if matched, will result in the row being dropped. Default is None.

    Returns:
    pd.DataFrame: A new DataFrame with the specified rows dropped.
    """
    # Drop rows with missing values
    # print(column_name)
    if value_to_drop == None:
        df = df.dropna(subset=[column_name])

     # If both column_name and value_to_drop are provided, drop rows based on the value
    if column_name and value_to_drop is not None:
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
        df = df[df[column_name] != value_to_drop]

    return df


def subtract_one_from_column(df, column_name):
    """
    Subtracts one from each value in the specified column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to modify.

    Returns:
    pd.DataFrame: A DataFrame with the specified column values decreased by one.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    df[column_name] = df[column_name] - 1
    return df