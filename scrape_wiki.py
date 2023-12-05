import pandas as pd
a_l = r"https://en.wikipedia.org/wiki/List_of_musicals:_A_to_L"
m_z = r"https://en.wikipedia.org/wiki/List_of_musicals:_M_to_Z"
a_l_tables = pd.read_html(a_l)
m_z_tables = pd.read_html(m_z)

a_l_tables.extend(m_z_tables)
all_tables = pd.concat(a_l_tables)

all_tables.to_csv("all_shows.csv")

# split the fields
def split_field(names: pd.Series) -> list[str]:
    names = names.str.split(",").explode()
    names = names.str.split(" and ").explode()
    group = names.groupby(names.index)
    names_list = [group.to_list() for name, group in group]
    return pd.Series(names_list, name=names.name)

# these are all the agent names you will need to add to the db
all_tables["Music"] = split_field(all_tables["Music"])
all_tables["Book"] = split_field(all_tables["Book"])
all_tables["Lyrics"] = split_field(all_tables["Lyrics"])


from itertools import chain

list_of_lists = [x for x in all_tables["Music"]]
flat_list = list(chain(*list_of_lists))
set(flat_list)
# store the names as lower case but display as TitleCase


