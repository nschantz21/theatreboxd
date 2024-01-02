
with open("replacement_crew.txt", "r") as f:
    raw_text = f.read()

r = raw_text.split('\n')
rr_list = []
for rr in r:
    rr = rr.split(";")
    rr_list.extend(rr)

# split the position from the person/people
import re
people_list = []
for rr in rr_list:
    position_person = re.split(r"\bby\b|:", rr)
    position = position_person[0]
    person = position_person[-1]
    people = re.split(r"\band\b|,", person)
    for p in people:
        people_list.append((position, p))

with open("replacement_crew_processed.csv", "a") as f:
    for pl in people_list:
        pl_s = f"{pl[0].strip()},{pl[1].strip()}\n"
        f.write(pl_s.lower())
