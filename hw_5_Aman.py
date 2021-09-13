import re
room=open("data_corey.txt")
number=room.read()
Allcontacts=(len(re.findall("\d+-\d+-\d+",number)))
(print(f"Total amount of phone numbers: {Allcontacts}"))
Contacts_with_seven=(len(re.findall("\d+-\d+-\d+\d+\d7",number)))
(print(f"Total amount of phone numbers with ending 7: {Contacts_with_seven}"))