# Coding Methodology & Reproducibility

This folder documents the **data processing and analysis steps** used to generate all results for  
**SoK: Design, Vulnerabilities, and Security Measures of Cryptocurrency Wallets**.

---

## 1. Overview

All datasets, code, and figures needed for reproducibility are included.  
Analysis is performed in Python (≥3.9) using Jupyter notebooks.

- Datasets: `/data/`
- Main notebook: `incidents_timeline.ipynb`
- Output figures: `/assets/`

---

## 2. Data Import & Cleaning

- Data is loaded with pandas from `incidents.csv` and `vuln_threats.csv`.
- ‘Funds Lost’ fields are normalised to USD, and ‘Date’ fields are parsed.
- Events are grouped into four-month periods (Jan, May, Sep) for visual clarity in the timeline plot.
- The `Custody` column is set to "Non-Custodial" by default if missing.

---

## 3. Analysis & Visualisation

- Timeline bubbles encode total funds lost (size) and custody type (colour).
- Both period anchors and intermediate events are plotted for completeness.
- All code is in the notebook, which builds `assets/Timeline_of_Wallet_Hacks.pdf` via Plotly.

---

## 4. Reproducibility

- **Reproduce all results** by running the notebook `incidents_timeline.ipynb` end-to-end.
- No manual editing required; outputs are generated automatically from raw data.

---

## 5. Data Inclusion Criteria

- **incidents.csv:** Real-world wallet/exchange losses, 2012–2025, from public disclosures.
- **vuln_threats.csv:** Concrete vulnerabilities mapped to the paper’s taxonomy.
- Both datasets are cleaned, unified, and categorised for transparency.

---
