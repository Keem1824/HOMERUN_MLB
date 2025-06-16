
import pandas as pd
import numpy as np
import joblib

def predict_hr(df, pitcher, weather):
    df = df.copy()
    try:
        model = joblib.load('model/xgb_model.pkl')
        scaler = joblib.load('model/xgb_scaler.pkl')
        feats = df[['HR_rate', 'ISO', 'wOBA', 'ExitVelo', 'LaunchAngle', 'barrel_rate', 'hard_hit_pct']]
        df['HR_probability'] = model.predict_proba(scaler.transform(feats))[:, 1]
    except:
        df['HR_probability'] = df['HR_rate'] * np.random.uniform(4, 6)
    return df.sort_values(by='HR_probability', ascending=False)
