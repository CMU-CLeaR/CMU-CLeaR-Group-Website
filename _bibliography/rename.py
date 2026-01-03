#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Haoyue
@file: rename.py
@time: 9/17/22 18:25
@desc: 
"""
## STRS copied from Kun's personal website
import time

STRS = '''Yang Liu, Hao Cheng, Kun Zhang, “Identifiability of Label Noise Transition Matrix,” accepted to International Conference on Machine Learning (ICML) 2023 

Ruichu Cai, Zhiyi Huang, Wei Chen, Zhifeng Hao, Kun Zhang, “Causal Discovery with Latent Confounders Based on Higher-Order Cumulants,” accepted to International Conference on Machine Learning (ICML) 2023 

Shiming Chen, Wenjin Hou, Ziming Hong, Xiaohan Ding, Yibing Song, Xinge You, Tongliang Liu, Kun Zhang, “Evolving Semantic Prototype Improves Generative Zero-Shot Learning,” accepted to International Conference on Machine Learning (ICML) 2023 

Yu Yao, Mingming Gong, Yuxuan Du, Jun Yu, Bo Han, Kun Zhang, Tongliang Liu, “Which is Better for Learning with Noisy Labels: The Semi-supervised Method or Modeling Label Noise?” accepted to International Conference on Machine Learning (ICML) 2023 

Jiaqi Sun, Lin Zhang, Guangyi Chen, Peng XU, Kun Zhang, Yujiu Yang, “Feature Expansion for Graph Neural Networks,” accepted to International Conference on Machine Learning (ICML) 2023 

Yatong Chen, Zeyu Tang, Kun Zhang, Yang Liu, “Model Transferability with Responsive Decision Subjects,”  accepted to International Conference on Machine Learning (ICML) 2023'''

time.sleep(5)

for line in STRS.split('\n\n'):
    line = line.strip()
    authors_list = line.split(', “')[0].split(', ')
    citenamestr = []
    for aname in authors_list:
        last_name = aname.split(' ')[-1]
        first_name = ' '.join(aname.split(' ')[:-1])
        citename = f'{last_name}, {first_name}'
        citenamestr.append(citename)
    first_author_last_name = citenamestr[0].split(',')[0].lower()
    citenamestr = ' and '.join(citenamestr)
    # print(citenamestr)
    title = line.split(', “')[1].split(',”')[0]
    bibname = f'{first_author_last_name}2023{title.split(" ")[0].split(":")[0].lower()}'
    fullname = f'''
@inproceedings{{{bibname},
  abbr={{ICML}},
  title={{{title}}},
  author={{{citenamestr}}},
  booktitle={{International Conference on Machine Learning}},
  year={2023},
  pdf={{}}
}}'''
    print(fullname)



# STRS = '''Generalizing Nonlinear ICA Beyond Structural Sparsity, by Yujia Zheng, Kun Zhang
# Learning World Models with Identifiable Factorization, by Yu-Ren Liu, Biwei Huang, Zhengmao Zhu, Honglong Tian, Mingming Gong, Yang Yu, Kun Zhang
# Temporally Disentangled Representation Learning under Unknown Nonstationarity, by Xiangchen Song, Weiran Yao, Yewen Fan, Xinshuai Dong, Guangyi Chen, Juan Carlos Niebles, Eric Xing, Kun Zhang
# Counterfactual Generation with Identifiability Guarantee, by Hanqi Yan, Lingjing Kong, Lin Gui, Yuejie Chi, Eric Xing, Yulan He, Kun Zhang
# Identification of Nonlinear Latent Hierarchical Models, by Lingjing Kong, Biwei Huang, Feng Xie, Eric Xing, Yuejie Chi, Kun Zhang
# On the Identifiability of Sparse ICA without Assuming Non-Gaussianity, by Ignavier Ng, Yujia Zheng, Xinshuai Dong, Kun Zhang
# Subspace Identification for Multi-Source Domain Adaptation, by Zijian Li, Ruichu Cai, Guangyi Chen, Boyang Sun, Zhifeng Hao, Kun Zhang'''
#
# for line in STRS.split('\n'):
#     line = line.strip()
#     title = line.split(', by ')[0]
#     authors_list = line.split(', by ')[1].split(', ')
#     citenamestr = []
#     for aname in authors_list:
#         last_name = aname.split(' ')[-1]
#         first_name = ' '.join(aname.split(' ')[:-1])
#         citename = f'{last_name}, {first_name}'
#         citenamestr.append(citename)
#     first_author_last_name = citenamestr[0].split(',')[0].lower()
#     citenamestr = ' and '.join(citenamestr)
#     bibname = f'{first_author_last_name}2023{title.split(" ")[0].split(":")[0].lower()}'
#     fullname = f'''
# @inproceedings{{{bibname},
#   abbr={{NeurIPS}},
#   title={{{title}}},
#   author={{{citenamestr}}},
#   booktitle={{Conference on Neural Information Processing Systems}},
#   year={2023}
# }}'''
#     print(fullname)
