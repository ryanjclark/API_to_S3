import pandas as pd

def turn_json_to_pd_csv(flattened_json, output_filename):
    df = pd.Series(flattened_json).to_frame()
    df.rename(columns={"0": "value"}, inplace=True)
    output = df.to_csv(output_filename)
    return output
