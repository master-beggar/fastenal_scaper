import os

os.chdir(r'C:\Users\wnaimi\Desktop')
fastener = 'Fasteners.txt'
imperial = 'Imperial.txt'
metric = 'Metric.txt'

metric_pn = set()
imperial_pn = set()

with open(imperial) as file:
    for line in file:
        line = line.split('|')
        pn = line[0].strip()
        imperial_pn.add(pn)

with open(metric) as file:
    for line in file:
        line = line.split('|')
        pn = line[0].strip()
        metric_pn.add(pn)

all_pn = metric_pn|imperial_pn

fastener_pn = set()

with open(fastener) as file:
    for line in file:
        line = line.strip()
        line_list = line.split('\t')
        if len(line_list) > 1:
            pn = line_list[0].strip()
            fastener_pn.add(pn)

diff_pn = all_pn^fastener_pn
with open('Diff.txt', 'w') as file:
    for part in diff_pn:
        file.write(part+'\n')
