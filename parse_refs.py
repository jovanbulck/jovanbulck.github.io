#!/usr/bin/python3

with open('_data/references.bib', 'r') as refi:
    with open('_includes/references_parsed.bib', 'w') as refo:
            refo.write('{% raw %}')
            for l in refi:
                if l != '\n':
                   refo.write(l)
            refo.write('@____dummy{% endraw %}')
