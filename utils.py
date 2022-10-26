import json

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def get_all():
    all_candidates = ''
    candidates = load_candidates()
    for candidate in candidates:
        all_candidates += f"{candidate['name']} -\n"\
                  f"{candidate['position']}\n"\
                  f"{candidate['skills']}\n\n"
    return all_candidates.strip()

def get_by_pk(pk):
    profile = ''
    candidates = load_candidates()
    for candidate in candidates:
        if pk == candidate['pk']:
            profile = f"<img src=({candidate['picture']})>\n"\
                      f"<pre>"\
                      f"{candidate['name']} -\n" \
                      f"{candidate['position']}\n" \
                      f"{candidate['skills']}"\
                      f"</pre>"
    return profile

def get_by_skill(skill_name):
    candidates_with_skill = ''
    candidates = load_candidates()
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            candidates_with_skill += f"{candidate['name']} -\n" \
                                     f"{candidate['position']}\n" \
                                     f"{candidate['skills']}\n\n"
    return f'<pre>{candidates_with_skill}</pre>'.strip()