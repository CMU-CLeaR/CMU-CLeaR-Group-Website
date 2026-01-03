STRS = '''1. Yiwen Qiu, Yujia Zheng, Kun Zhang, "Identifying Selections for Unsupervised Subtask Discovery,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
2. Xinshuai Dong, Ignavier Ng, Biwei Huang, Yuewen Sun, Songyao Jin, Roberto Legaspi, Peter Spirtes, Kun Zhang , "On the Parameter Identifiability of Partially Observed Linear Causal Models,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
3. Longkang Li, Haoyue Dai, Hanin Al Ghothani, Biwei Huang, Jiji Zhang, Shahar Harel, Isaac Bentwich, Guangyi Chen, Kun Zhang, "On Causal Discovery in the Presence of Deterministic Relations,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
4. Lingjing Kong, Guangyi Chen, Biwei Huang, Eric Xing, Yuejie Chi, Kun Zhang , "Learning Discrete Concepts in Latent Hierarchical Models,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
5. Lingjing Kong, Guangyi Chen, Petar Stojanov, Haoxuan Li, Eric Xing, Kun Zhang, "Towards Understanding Extrapolation: a Causal Lens,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
6. Xiangchen Song, Zijian Li, Guangyi Chen, Yujia Zheng, Yewen Fan, Xinshuai Dong, Kun Zhang , "Causal Temporal Representation Learning with Nonstationary Sparse Transition,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
7. Guang-Yuan Hao, Jiji Zhang, Biwei Huang, Hao Wang, Kun Zhang , "Natural Counterfactuals With Necessary Backtracking,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
8. Yuewen Sun, Biwei Huang, Yu Yao, Donghuo Zeng, Xinshuai Dong, Songyao Jin, Boyang Sun, Roberto Legaspi, Kazushi Ikeda, Peter Spirtes, Kun Zhang , "Identifying Latent State-Transition Processes for Individualized Reinforcement Learning,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
9. Zhengming Chen, Ruichu Cai, Feng Xie, Jie Qiao, Anpeng Wu, Zijian Li, Zhifeng Hao, Kun Zhang , "Learning Discrete Latent Variable Structures with Tensor Rank Conditions,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
10. Haoxuan Li, Yue Liu, Zhi Geng, Kun Zhang, "A Local Method for Satisfying Interventional Fairness with Partially Known Causal Graphs,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
11. Chenxi Liu, Yongqiang Chen, Tongliang Liu, Mingming Gong, James Cheng, Bo Han, Kun Zhang, "Discovery of the Hidden World with Large Language Models,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
12. Zhikang Chen, Min Zhang, Sen Cui, Haoxuan Li, Gang Niu, Mingming Gong, Changshui Zhang, Kun Zhang , "Neural Collapse Inspired Feature Alignment for Out-of-Distribution Generalization,” accepted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
13. Kun Zhang, Shaoan Xie, Ignavier Ng, Yujia Zheng, "Causal Representation Learning from Multiple Distributions: A General Setting,” accepted to International Conference on Machine Learning (ICML) 2024 
14. Shunxin Fan, Mingming Gong, Kun Zhang, "On the Recoverability of Causal Relations from Temporally Aggregated I.I.D. Data,” accepted to International Conference on Machine Learning (ICML) 2024 
15. Guangyi Chen, Yifan Shen, Zhenhao Chen, Xiangchen Song, Yuewen Sun, Weiran Yao, Xiao Liu, Kun Zhang, "CaRiNG: Learning Temporal Causal Representation under Non-Invertible Generation Process,” accepted to International Conference on Machine Learning (ICML) 2024
16. Yujia Zheng, Zeyu Tang, Yiwen Qiu, Bernhard Schölkopf, Kun Zhang, "Detecting and Identifying Selection Structure in Sequential Data,” accepted to International Conference on Machine Learning (ICML) 2024
17. Ignavier Ng, Xinshuai Dong, Haoyue Dai, Biwei Huang, Peter Spirtes, Kun Zhang, "Score-Based Causal Discovery in the Presence of Causally-Related Latent Variables,” accepted to International Conference on Machine Learning (ICML) 2024
18. Tianjun Yao, Yongqiang Chen, Zhenhao Chen, Kai Hu, Zhiqiang Shen, Kun Zhang, "Empowering Graph Invariance Learning with Deep Spurious Infomax,” accepted to International Conference on Machine Learning (ICML) 2024
19. Wenjie Wang, Biwei Huang, Feng Liu, Xinge You, Tongliang Liu, Kun Zhang, Mingming Gong, "Optimal Kernel Choice for Score Function-based Causal Discovery,” accepted to International Conference on Machine Learning (ICML) 2024
20.  Fang Guo, Pei Zhang, Vivian Do, Andreas Gerhardus, Jakob Runge, Kun Zhang, Zheshen Han, Shenxi Deng, Hongli Lin, Sheikh Taslim Ali, Ruchong Chen, Yuming Guo, Linwei Tian, "Ozone as an environmental driver of influenza,” accepted to Nature Communications, 2024
21. Yuanyuan Wang, Wei Huang, Mingming Gong, Xi Geng, Tongliang Liu, Kun Zhang, Dacheng Tao, "Identifiability and Asymptotics in Learning Homogeneous Linear ODE Systems from Discrete Observations,” accepted to Journal of Machine Learning Research, 25(154):1−50, 2024.'''

for line in STRS.split('\n'):
    index, details = line.split('. ', 1)
    authors, title_conference = details.rsplit(', "', 1)
    title, conference = title_conference.split(',” accepted to ', 1)
    conference_name, year = conference.rsplit(' ', 1)
    year = year.strip()
    authors_list = authors.split(', ')
    citenamestr = [' '.join(author.split(' ')[-1:]) + ', ' + ' '.join(author.split(' ')[:-1]) for author in
                   authors_list]
    citenamestr = ' and '.join(citenamestr)
    bibname = authors_list[0].split(' ')[-1].lower() + year + title.split(" ")[0].lower()
    print(f'''
@inproceedings{{{bibname},
  title={{{title}}},
  author={{{citenamestr}}},
  booktitle={{{conference_name}}},
  year={{{year}}},
  pdf={{}}
}}''')



'''

@inproceedings{dai2024local,
  title={Local Causal Discovery with Linear non-Gaussian Cyclic Models},
  author={Dai, Haoyue and Ng, Ignavier and Zheng, Yujia and Gao, Zhengqing and Zhang, Kun},
  abbr={AISTATS},
  booktitle={International Conference on Artificial Intelligence and Statistics},
  year={2024},
  pdf={https://arxiv.org/pdf/2403.14843}
}


@inproceedings{ng2024structure,
  title={Structure Learning with Continuous Optimization: A Sober Look and Beyond},
  author={Ng, Ignavier and Huang, Biwei and Zhang, Kun},
  abbr={CLeaR},
  booktitle={Conference on Causal Learning and Reasoning (Best Paper Award)},
  year={2024},
  pdf={https://arxiv.org/abs/2304.02146}
}


@inproceedings{yao2024mugsi,
  title={MuGSI: Distilling GNNs with Multi-Granularity Structural Information for Graph Classification},
  author={Yao, Tianjun and Sun, Jiaqi and Cao, Defu and Zhang, Kun and Chen, Guangyi},
  abbr={WWW},
  booktitle={The Web Conference},
  year={2024},
  pdf={}
}

@inproceedings{zeng2024counterfactual,
  title={Counterfactual Reasoning Using Predicted Latent Personality Dimensions for Optimizing Persuasion Outcome},
  author={Zeng, Donghuo and Legaspi, Roberto and Sun, Yuewen and Dong, Xinshuai and Ikeda, Kazushi and Zhang, Kun and Spirtes, Peter},
  booktitle={Persuasive Technology (Best paper nominee)},
  abbr={PT},
  year={2024},
  pdf={https://arxiv.org/pdf/2404.13792}
}

@inproceedings{dai2024gene,
  title={Gene Regulatory Network Inference in the Presence of Dropouts: a Causal View},
  author={Dai, Haoyue and Ng, Ignavier and Luo, Gongxu and Spirtes, Peter and Stojanov, Petar and Zhang, Kun},
  booktitle={International Conference on Learning Representations (Oral)},
  abbr={ICLR},
  year={2024},
  pdf={https://arxiv.org/pdf/2403.15500}
}

@inproceedings{li2024causal,
  title={Causal Structure Recovery with Latent Variables under Milder Distributional and Graphical Assumptions},
  author={Li, Xiu-Chuan and Zhang, Kun and Liu, Tongliang},
  booktitle={International Conference on Learning Representations},
  abbr={ICLR},
  year={2024},
  pdf={https://openreview.net/pdf?id=MukGKGtgnr}
}

@inproceedings{tang2024procedural,
  title={Procedural Fairness Through Decoupling Objectionable Data Generating Components},
  author={Tang, Zeyu and Wang, Jialu and Liu, Yang and Spirtes, Peter and Zhang, Kun},
  booktitle={International Conference on Learning Representations (Spotlight)},
  abbr={ICLR},
  year={2024},
  pdf={https://arxiv.org/pdf/2311.14688}
}

@inproceedings{chen2024llcp:,
  title={LLCP: Learning Latent Causal Processes for Reasoning-based Video Question Answer},
  author={Chen, Guangyi and Li, Yuke and Liu, Xiao and Li, Zijian and Suradi, Eman Al and Wei, Donglai and Zhang, Kun},
  booktitle={International Conference on Learning Representations},
  abbr={ICLR},
  year={2024},
  pdf={https://openreview.net/pdf?id=Cu5wJa5LGO}
}

@inproceedings{jin2024structural,
  title={Structural Estimation of Partially Observed Linear Non-Gaussian Acyclic Model: A Practical Approach with Identifiability},
  author={Jin, Songyao and Xie, Feng and Chen, Guangyi and Huang, Biwei and Chen, Zhengming and Dong, Xinshuai and Zhang, Kun},
  booktitle={International Conference on Learning Representations},
  abbr={ICLR},
  year={2024},
  pdf={https://openreview.net/pdf?id=nHkMm0ywWm}
}

@inproceedings{li2024federated,
  title={Federated Causal Discovery from Heterogeneous Data},
  author={Li, Longkang and Ng, Ignavier and Luo, Gongxu and Huang, Biwei and Chen, Guangyi and Liu, Tongliang and Gu, Bin and Zhang, Kun},
  booktitle={International Conference on Learning Representations},
  abbr={ICLR},
  year={2024},
  pdf={https://arxiv.org/pdf/2402.13241}
}

@inproceedings{liu2024identifiable,
  title={Identifiable Latent Polynomial Causal Models through the Lens of Change},
  author={Liu, Yuhang and Zhang, Zhen and Gong, Dong and Gong, Mingming and Huang, Biwei and Hengel, Anton van den and Zhang, Kun and Shi, Javen Qinfeng},
  booktitle={International Conference on Learning Representations},
  abbr={ICLR},
  year={2024},
  pdf={https://arxiv.org/pdf/2310.15580}
}

@inproceedings{dong2024a,
  title={A Versatile Causal Discovery Framework to Allow Causally-Related Hidden Variables},
  author={Dong, Xinshuai and Huang, Biwei and Ng, Ignavier and Song, Xiangchen and Zheng, Yujia and Jin, Songyao and Legaspi, Roberto and Spirtes, Peter and Zhang, Kun},
  booktitle={International Conference on Learning Representations},
  abbr={ICLR},
  year={2024},
  pdf={https://arxiv.org/pdf/2312.11001}
}

@inproceedings{sun2024acamda,
  title={ACAMDA: Improving Data Efficiency in Reinforcement Learning Through Guided Counterfactual Data Augmentation},
  author={Sun, Yuewen and Wang, Erli and Huang, Biwei and Lu, Chaochao and Feng, Lu and Sun, Changyin and Zhang, Kun},
  abbr={AAAI},
  booktitle={Proceedings of the AAAI conference on Artificial Intelligence},
  year={2024},
  pdf={https://openreview.net/pdf?id=4pjgPGB1qr}
}

@inproceedings{zhang2024towards,
  title={Towards Realistic Zero-Shot Classification via Self Structural Semantic Alignment},
  author={Zhang, Sheng and Naseer, Muzammal and Chen, Guangyi and Shen, Zhiqiang and Khan, Salman and Zhang, Kun and Khan, Fahad Shahbaz},
  abbr={AAAI},
  booktitle={Proceedings of the AAAI conference on Artificial Intelligence},
  year={2024},
  pdf={https://arxiv.org/pdf/2308.12960}
}

@inproceedings{chen2024identification,
  title={Identification of Causal Structure with Latent Variables based on Higher Order Cumulants},
  author={Chen, Wei and Huang, Zhiyi and Cai, Ruichu and Hao, Zhifeng and Zhang, Kun},
  abbr={AAAI},
  booktitle={Proceedings of the AAAI conference on Artificial Intelligence},
  year={2024},
  pdf={https://arxiv.org/pdf/2312.11934}
}

'''