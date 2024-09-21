import pandas as pd
import numpy as np
from typing import Sequence

def null_values(df: pd.DataFrame) -> None:
    print(df.isnull().sum().sort_values(ascending=False))

def empty_imputer(df: pd.DataFrame, missing_column: str) -> pd.DataFrame:
    df.loc[df[missing_column].isnull(), [missing_column]] = "Yok"
    return df

# Boy ve kilo için doldurma yapma
def imputer_missing_values(df: pd.DataFrame, missing_column: str, target_column: str, th: int) -> pd.DataFrame:
    for index, row in df[df[missing_column].isnull()].iterrows():
        sample = df.loc[(df[target_column] >= row[target_column] - th) & (df[target_column] <= row[target_column] + th), :]
        if row["gender"] is not np.NaN:
            sample = sample.loc[sample["gender"] == row["gender"],:] # same gender
        df.loc[index, [missing_column]] = sample[missing_column].dropna().values.mean()
    return df

def fill_missing_values(df: pd.DataFrame, missing_diseases: Sequence):
    print(f"Before filling missing data:\n {null_values(df)}")
    # gender
    df = empty_imputer(df, "gender")
    # city
    df = empty_imputer(df, "city")
    # blood type
    df = empty_imputer(df, "blood_type")
    # allergies
    df = empty_imputer(df, "allergies")
    # chronic diseases
    for dis in missing_diseases:
        df = empty_imputer(df, dis)
    # height
    df = imputer_missing_values(df, "height", "weight", 5)
    # weight
    df = imputer_missing_values(df, "weight", "height", 10)
    df["bmi"] = (df["weight"] / df["height"]**2) * 10e3

    print(f"After filling:\n{null_values(df)}")
    return df

def preprocess_pipe(df: pd.DataFrame, missing_diseases: Sequence) -> pd.DataFrame:
    df = fill_missing_values(df, missing_diseases)
    for disease in missing_diseases:
        df = split_disease_column(df, disease)
    df.drop(['birthdate', 'origin', 'drug_start_date', 'drug_end_date','side_effect_notif_date'], axis=1, inplace=True)
    return df

def split_disease_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = df[column_name].apply(lambda row: row.split(','))
    df[[column_name+"_1", column_name+"_2"]] = pd.DataFrame(df[column_name].tolist(), index=df.index)
    df = empty_imputer(df, column_name+"_2")
    return df.drop([column_name], axis=1)


def fill_chronic_diseases(df: pd.DataFrame, col_name: str, diseases: Sequence):
    df_chronic_mod = df.loc[(df['bmi'] > 35) & (df['age'] > 50), diseases]
    # Mod of bmi high patients
    bmi_high = list(df_chronic_mod[col_name].value_counts().index.values[:-2])
    print(f"BMI High: {bmi_high}")
    if "Yok" in bmi_high:
        bmi_high.remove("Yok")
    for index, row in df.iterrows():
        if row[col_name] == "Yok" and row['bmi'] > 40 and row['age'] > 50:
            family_dis = row[diseases].values
            for item in bmi_high:
                if item in family_dis:
                    df.loc[index, [col_name]] = item
                    break
    return df