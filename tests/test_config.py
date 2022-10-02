import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range": 
    {"age": 7897897, 
    "sex": 4, 
    "cp": 99, 
    "trtbps": 2, 
    "chol": 12, 
    "fbs": 789, 
    "restecg": 75, 
    "thalachh": 2, 
    "exng": 33, 
    "oldpeak": 9, 
    "slp": 9,
    "caa": 44, 
    "thall": 33,
    },

    "correct_range":
    {"age": 55, 
    "sex": 1, 
    "cp": 2, 
    "trtbps": 155, 
    "chol": 232, 
    "fbs": 1, 
    "restecg": 2, 
    "thalachh": 132, 
    "exng": 0, 
    "oldpeak": 4, 
    "slp": 1,
    "caa": 2, 
    "thall": 2,
    },

    "incorrect_col":
    {"age": 55, 
    "sex": 1, 
    "cp": 2, 
    "trt bps": 155, 
    "chol ": 232, 
    "fbs": 1, 
    "restecg": 2, 
    "thalachh": 132, 
    "exng": 0, 
    "oldpeak": 4, 
    "s lp": 1,
    "caa": 2, 
    "tha ll": 2,
    }
}

TARGET_range = {
    "min": 0,
    "max": 1
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message