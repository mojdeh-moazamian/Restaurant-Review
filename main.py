from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from models import RestaurantReview
from utils import read_reviews_from_excel
import pandas as pd
import numpy as np

app = FastAPI()


reviews = []
excel_file_path = 'example.xlsx'

@app.post("/reviews/", response_model=RestaurantReview)
def create_review(review: RestaurantReview):
    reviews.append(review)
    return review

@app.get("/reviews/", response_model=List[RestaurantReview])
def get_reviews():
    return reviews

    
    
@app.get("/fetch-excel-reviews/", response_model=List[str])
def fetch_excel_reviews(reviewer: Optional[str] = Query(None)):
    try:
        excel_reviews = read_reviews_from_excel(excel_file_path)
        
        reviewers_in_excel = set(review['reviewer'].lower() for review in excel_reviews)
        if reviewer and reviewer.lower() not in reviewers_in_excel:
            raise HTTPException(status_code=404, detail="The reviewer does not exist")
        if reviewer:
            reviewer_reviews = [review['testo'] for review in excel_reviews if reviewer.lower() in review['reviewer'].lower()]
            if all(pd.isna(x) for x in reviewer_reviews):
                raise HTTPException(status_code=404, detail="The reviewer didn't leave any comments")
            return reviewer_reviews
        all_reviews = [review['testo'] for review in excel_reviews]
        return all_reviews
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
