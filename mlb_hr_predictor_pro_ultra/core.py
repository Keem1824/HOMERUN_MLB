
# core.py — basic home run predictor logic
import pandas as pd
import numpy as np
import joblib

# Fallback: use random model if no model loaded
def predict_hr(df, pitcher, weather):
    try:
        model = joblib.load('model/xgb_model.pkl')
        scaler = joblib.load('model/xgb_scaler.pkl')
    except:
        model = None
        scaler = None

    features = df[['HR_rate', 'ISO', 'wOBA', 'ExitVelo', 'LaunchAngle', 'barrel_rate', 'hard_hit_pct']]
    if scaler:
        features = scaler.transform(features)
        df['HR_probability'] = model.predict_proba(features)[:, 1]
    else:
        df['HR_probability'] = df['HR_rate'] * np.random.uniform(4, 8)

    return df.sort_values(by='HR_probability', ascending=False)
