import yaml

fk_dir = "/home/atri/git/Fork-Fork-Awesome"
with open(f"{fk_dir}/src/icons/icons.yml", 'r') as f:
    fk_icon = yaml.safe_load(f)

fk_icon_ids = [icon['id'] for icon in fk_icon['icons']]
fk_icon_aliases = []
for icon in fk_icon['icons']:
    if 'aliases' in icon:
        fk_icon_aliases.extend(icon['aliases'])
fk_icon_all = fk_icon_ids + fk_icon_aliases
fk_icon_unicodes = [icon['unicode'] for icon in fk_icon['icons']]
# check if duplicates
fk_icon_ids_duplicates = [id for id in fk_icon_ids if fk_icon_ids.count(id) > 1]
fk_icon_aliases_duplicates = [alias for alias in fk_icon_aliases if fk_icon_aliases.count(alias) > 1]
fk_icon_all_duplicates = [id for id in fk_icon_all if fk_icon_all.count(id) > 1]
fk_icon_unicodes_duplicates = [unicode for unicode in fk_icon_unicodes if fk_icon_unicodes.count(unicode) > 1]
print(f"fk_icon_ids_duplicates: {fk_icon_ids_duplicates}")
print(f"fk_icon_aliases_duplicates: {fk_icon_aliases_duplicates}")
print(f"fk_icon_all_duplicates: {fk_icon_all_duplicates}")
print(f"fk_icon_unicodes_duplicates: {fk_icon_unicodes_duplicates}")

# remove duplicates aliases in yaml
for icon in fk_icon['icons']:
    if 'aliases' in icon:
        for alias in icon['aliases']:
            if alias in fk_icon_all_duplicates:
                icon['aliases'].remove(alias)
                if len(icon['aliases']) == 0:
                    del icon['aliases']
with open(f"{fk_dir}/src/icons/icons.yml", 'w') as f:
    yaml.dump(fk_icon, f, default_flow_style=False, sort_keys=False, indent=2)
