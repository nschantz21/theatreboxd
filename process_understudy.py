import re
import pandas as pd

input_file = "cast_understudy.txt"
with open(input_file, 'r') as f:
    input_text = f.read()

# Define a regular expression pattern to extract agent
# and character
pattern = re.compile(r'([^\(]+)\(([^)]+)\)')
# Find all matches in the input text
matches = pattern.findall(input_text)
# Create a list of dictionaries with 'agent' and
# 'character' keys
data = [
    {
        'agent': re.sub(r',', '', match[0].strip()),
        'character': match[1].strip()
    } for match in matches
]


# remove 'and's
and_pattern = re.compile(r'^and\s+|\s+and$|\s+and\s+')
data = [{and_pattern.sub('', k): and_pattern.sub('', v) for k,v in dd.items()} for dd in data]

# split the characters into a list
data_list = [{k: v.split(',') for k, v in dd.items()} for dd in data]

df = pd.DataFrame.from_records(data_list)
df = df.explode("character")
df['agent'] = df['agent'].apply(lambda x: x[0]).str.strip()
df.to_csv("cast_understudy_processed.csv", index=False)