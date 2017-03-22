import json

def member_func(member_name, member_id, link):
    data = {
        'member_name': member_name,
        'member_id': member_id,
        'member_link': link
    }
    member = member_search(member_name)
    if member:
        with open('profile.json', 'w') as f:
            profile = json.load(f)
            member['member_name'] = data['member_name']
            member['member_id'] = data['member_id']
            member['member_link'] = data['member_link']

    else:
      with open('profile.json') as f:
         profile = json.load(f)
         profile['Members:'].append(data)
      with open('profile.json', 'w') as f:
         json.dump(profile, f, indent=4)



def member_search(member_name):
    with open('profile.json') as f:
        profile = json.load(f)
    for member in profile['Members:']:
        if member["member_name"] == member_name:
             return member
    return None






