import pandas as pd

def compare_xml_files(file1, file2):
    # Read the first XML file into a Pandas dataframe
    df1 = pd.read_xml(file1)

    # Read the second XML file into a Pandas dataframe
    df2 = pd.read_xml(file2)

    # Find the common columns between the two dataframes
    common_columns = list(set(df1.columns) & set(df2.columns))

    # Filter the first dataframe to only include the common columns
    df1 = df1[common_columns]

    # Filter the second dataframe to only include the common columns
    df2 = df2[common_columns]

    # Merge the two dataframes on the common columns
    merged_df = pd.merge(df1, df2, on=common_columns, how='inner')

    # Write the merged dataframe to a new XML file
    merged_df.to_xml('merged_data.xml', index=False)

# Drop .xml file names here:
compare_xml_files('file1.xml', 'file2.xml')
