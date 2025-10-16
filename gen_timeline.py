#!/usr/bin/python3
import yaml
import json
import bibtexparser
import dateutil.parser as dateparser

YAML_IN  = '_data/papers.yml'
BIB_IN   = '_data/references.bib'
JSON_OUT = 'timeline_items.json'

groups = {
    'interface-shielding': 'Enclave shielding',
    'mcu'                : 'Microcontroller security',
    'side-channel'       : 'Side channels',
    'transient-execution': 'Transient execution',
    'meta-science'       : 'Meta-science'
}

with open(YAML_IN, 'r') as f:
    papers = yaml.safe_load(f)
  
with open(BIB_IN) as f:
    bibtex = bibtexparser.load(f)

def fmt_group(paper):
    return next((g for g in groups.keys() if g in paper['topic'].split(' ')))

def fmt_start(paper):
    bib = next((entry for entry in bibtex.entries if entry['ID'] == paper['bibtex']))   
    month = bib.get('month', 'Jan')
    return f"{paper['year']}-{dateparser.parse(month).month:02d}-01"

data = {}
data['items'] = [
    {
      **{
        'id': p['id'],
        'content': p['short'],
        'title': p['title'],
        'authors': p['author'],
        'venue': p.get('acro', p['venue']),
        'year': p['year'],
        'start': fmt_start(p),
        'group': fmt_group(p)
      },
      **({'logo': f'files/{p['id']}-logo.svg'} if p.get('logo') == True else {})
    }
    for p in papers['pubs']
]

data['groups'] = [
    {
        'id': gid,
        'content': f'<b>{gname}</b>'
    }
    for gid, gname in groups.items()
]

data['arrows'] = [
    {
        'id': i,
        'id_item_1': prev,
        'id_item_2': p['id'],
        'direction': 1,
        'type': 2,
    }
    for i, (p, prev) in enumerate(
        (p, prev) for p in papers['pubs'] for prev in p.get('prev', '').split()
    )
]

with open(JSON_OUT, "w") as json_file:
    json.dump(data, json_file, indent=4)