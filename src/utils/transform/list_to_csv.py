import pandas as pd

def turn_list_to_pd_csv(flattened_list, output_filename):
    ser = pd.Series(flattened_list)
    ser.dropna(inplace=True)
    ser = ser.str.replace(r"\(.*\)", "")
    output = ser.to_csv(output_filename, index=False, header=False)
    return output
