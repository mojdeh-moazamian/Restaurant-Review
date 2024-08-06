import pandas as pd

def read_reviews_from_excel(file_path: str):
    df = pd.read_excel(file_path)
    df['data'] = pd.to_datetime(df['data'], errors='coerce')  # Convert 'data' to datetime
    reviews = df.to_dict(orient='records')
    return reviews
