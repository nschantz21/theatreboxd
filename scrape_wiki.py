import pandas as pd
a_l = r"https://en.wikipedia.org/wiki/List_of_musicals:_A_to_L"
m_z = r"https://en.wikipedia.org/wiki/List_of_musicals:_M_to_Z"
a_l_tables = pd.read_html(a_l)
m_z_tables = pd.read_html(m_z)

a_l_tables.extend(m_z_tables)
all_tables = pd.concat(a_l_tables)

all_tables.to_csv("all_shows.csv")
