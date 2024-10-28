import pandas as pd

def remove_duplicates(input_file, output_file, duplicates_file):
    df = pd.read_csv(input_file)

    duplicates = df[df.duplicated(keep=False)]                             # Identify duplicate rows
  
    df_cleaned = df.drop_duplicates()                                         # Remove duplicate rows

    df_cleaned = df_cleaned.dropna(how='any')                                     # Remove empty rows
    
    # Remove junk values; define junk values to remove
    junk_values = ["N/A", "null", ""]  

    # Remove rows with junk values in any column
    for junk in junk_values:
        df_cleaned = df_cleaned.replace(junk, pd.NA)  
    df_cleaned = df_cleaned.dropna(how='any')  

    df_cleaned = df_cleaned.loc[:, ~df_cleaned.columns.duplicated()]                # Remove duplicate columns


    df_cleaned.to_csv(output_file, index=False)
    duplicates.to_csv(duplicates_file, index=False)
    
    print(f"Duplicates, junk values, and empty rows removed. Cleaned file saved as {output_file}")
    print(f"Duplicate rows saved as {duplicates_file}")


input_file = r"C:\Users\USER\Desktop\DALBHARAT.csv"  
output_file = r"C:\Users\USER\Desktop\output_cleaned.csv"
duplicates_file = r"C:\Users\USER\Desktop\duplicates.csv"  

remove_duplicates(input_file, output_file, duplicates_file)

