def clean_data(df):
    df.columns = df.columns.str.lower().str.strip()
    df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
    df.fillna(0, inplace=True)
    return df