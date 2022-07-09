import yaml
import os
import pandas

df_unicode = pandas.read_csv('variables.csv')
df_dict = {}
for index, row in df_unicode.iterrows():
    df_dict[row['icon']] = row['unicode']
fk_dir = "/home/atri/git/Fork-Fork-Awesome"
fa_dir = "/home/atri/git/Font-Awesome" # v5
created_ver = 1.4

with open(f"{fk_dir}/src/icons/icons.yml", 'r') as f:
    fk_icon = yaml.safe_load(f)

fk_icon_ids = [icon['id'] for icon in fk_icon['icons']]
fk_icon_unicodes = [icon['unicode'] for icon in fk_icon['icons']]
fa_icon_ids = []
for id in df_dict.keys():
    fa_icon_ids.append(id)
fa_icon_unicodes = []
for unicode in df_dict.values():
    fa_icon_unicodes.append(unicode)

# readdress fk_icon_ids in e100 to e900
cur_unicode_hex = int('e100', 16)
for id in fk_icon_ids:
    if id in fa_icon_ids:
        fk_icon['icons'][fk_icon_ids.index(id)]['unicode'] = df_dict[id]
    else:
        fk_icon['icons'][fk_icon_ids.index(id)]['unicode'] = f"{cur_unicode_hex:x}"
        cur_unicode_hex += 1

# unknown bug
#fa_icon_dirs = ['regular', 'solid', 'brands']
fa_icon_dirs = ['regular', 'brands']
for fa_icon_dir in fa_icon_dirs:
    fa_icon_ids = []
    for root, dirs, files in os.walk(f"{fa_dir}/svgs/{fa_icon_dir}"):
        for file in files:
            if file.endswith(".svg"):
                fa_icon_ids.append(file.split(".")[0])

    for fa_icon_id in fa_icon_ids:
        if not fa_icon_id in fk_icon_ids:
            print(f"{fa_icon_id} not in fk_icon_ids")
            if fa_icon_dir == 'brands':
                fk_icon['icons'].append({'name': fa_icon_id, 'id': fa_icon_id, 'unicode': df_dict[fa_icon_id], 'created': created_ver, 'categories': ['Brand Icons']})
            else:
                fk_icon['icons'].append({'name': fa_icon_id, 'id': fa_icon_id, 'unicode': df_dict[fa_icon_id], 'created': created_ver})
            os.system(f"cp -f {fa_dir}/svgs/{fa_icon_dir}/{fa_icon_id}.svg {fk_dir}/src/icons/svg")
        elif fa_icon_dir == 'solid':
            fa_icon_alt_id = fa_icon_id + '-solid'
            fk_icon['icons'].append({'name': fa_icon_alt_id, 'id': fa_icon_alt_id, 'unicode': f"{cur_unicode_hex:x}", 'created': created_ver})
            cur_unicode_hex += 1
            os.system(f"cp -f {fa_dir}/svgs/{fa_icon_dir}/{fa_icon_id}.svg {fk_dir}/src/icons/svg/{fa_icon_alt_id}.svg")

    print(f"{fa_icon_dir} done")
    fk_icon_ids = [icon['id'] for icon in fk_icon['icons']]

# save yaml
with open(f"{fk_dir}/src/icons/icons.yml", 'w') as f:
    yaml.dump(fk_icon, f, default_flow_style=False, sort_keys=False, indent=2)
print("done")
