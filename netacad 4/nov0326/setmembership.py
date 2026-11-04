registered_ids = {104, 108, 115, 121}

print(115 in registered_ids)
print(999 in registered_ids)

registered_ids.add(999)
registered_ids.discard(108)