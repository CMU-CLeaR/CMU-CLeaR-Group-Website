#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Haoyue
@file: rename.py
@time: 9/17/22 18:25
@desc: 
"""
'''
at first it looks like:

@inproceedings{zhang2020causal,https://proceedings.neurips.cc/paper/2020/file/02ed812220b0705fabb868ddbf17ea20-Paper.pdf
  abbr={NeurIPS},
  title={A causal view on robustness of neural networks},
  author={Zhang, Cheng and Zhang, Kun and Li, Yingzhen},
  booktitle={Conference on Neural Information Processing Systems},
  year={2020}
}

'''
with open('papers.bib', 'r') as fin: lines = fin.readlines()

newlines = []
buffer_lines = []
pdf_link = None

for line in lines:
    line = line.replace('\n', '')
    if '@' in line and '{' in line and ',' in line:
        newlines.extend(buffer_lines)
        buffer_lines = []; pdf_link = None
        original_beginner, read_link = line.split(',')
        buffer_lines.append(original_beginner + ',')
        pdf_link = read_link if len(read_link) > 0 else None
    elif line.strip() == '}':
        if pdf_link is not None:
            buffer_lines[-1] += ','
            buffer_lines.append(f'  pdf={{{pdf_link}}}')
            buffer_lines.append(line)
    else:
        buffer_lines.append(line)

print('\n'.join(newlines))