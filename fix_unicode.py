import yaml
import os
import pandas

df_unicode = pandas.read_csv('var.csv')
df_dict = {}
for index, row in df_unicode.iterrows():
    df_dict[row['icon']] = row['unicode']

fk_dir = "/home/atri/git/Fork-Fork-Awesome"

with open(f"{fk_dir}/src/icons/icons.yml", 'r') as f:
    fk_icon = yaml.safe_load(f)

for icon in fk_icon['icons']:
    #print(icon)
    if icon['id'] in list(df_dict.keys()):
        icon['unicode'] = df_dict[icon['id']]
    else:
        print(f"{icon['id']} not found in var.csv")

with open(f"{fk_dir}/src/icons/icons.yml", 'w') as f:
    yaml.dump(fk_icon, f, default_flow_style=False, sort_keys=False, indent=2)
