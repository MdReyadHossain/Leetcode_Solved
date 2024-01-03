import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    if len(student_data) == 0:
        return pd.DataFrame()

    columns_name = ['student_id', 'age']
    return pd.DataFrame(student_data, columns=columns_name)
