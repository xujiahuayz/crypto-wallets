# SoK: Design, Vulnerabilities, and Security Measures of Cryptocurrency Wallets

## Repository Structure
```bash
├── data/
│   ├── incidents.csv            # 2012-2025 real-world loss events (84 rows)
│   └── vuln_threats.csv         # 33 wallet-specific design vulnerabilities
├── notebooks/
│   ├── incidents_timeline.ipynb   # Exploratory analysis & design notes
│   └── README.md                 # In-depth methodology walk-through
├── assets/
│   └──  # a list of figures generated in the paper
└── README.md                     # ← You are here
```

## Datasets

1. **incidents.csv** (84 events, 2012-2025)  
   Quantifies \$6.98 B of confirmed wallet/exchange losses.

2. **vuln_threats.csv** (33 vulnerabilities, 2009-2024)  
   Maps wallet design to vulnerabilities and threats.

## Citation
```bibtex
@article{erinle2023sok,
  title   = {SoK: Design, Vulnerabilities, and Security Measures of Cryptocurrency Wallets},
  author  = {Erinle, Yimika and Kethepalli, Yathin and Feng, Yebo and Xu, Jiahua},
  journal = {arXiv preprint arXiv:2307.12874},
  year    = {2023}
}
