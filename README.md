# Population Flow Analysis — USA Census 2016

Laboratory exercise for the course *Programmazione di Applicazioni Data Intensive*  
Laurea in Ingegneria e Scienze Informatiche — DISI, Università di Bologna, Cesena  
Proff. Gianluca Moro, Roberto Pasolini

---

## Description

Analysis of inter-state population migration in the United States based on 2016 U.S. Census Bureau data. The dataset includes information on residents who remained in the same household, moved within the same state, relocated from another state, or immigrated from abroad.

Data is provided as a NumPy archive (`usa_census.npz`) containing the following arrays: `states`, `population`, `area`, `same_house`, `same_state`, `other_state`, `state_to_state`, `from_abroad`.

---

## Structure

The laboratory is divided into six exercises of increasing complexity:

1. **NumPy Recap** — indexing, slicing, boolean masking, and aggregations on raw arrays
2. **Series Operations** — unit conversion and derived series (e.g., population density)
3. **Series Reductions** — analytical queries using `sum`, `min`, `max`, `idxmax`, etc.
4. **DataFrame Operations** — querying `census` and `state_to_state` frames
5. **DataFrame Selection** — advanced filtering with `.loc` and `.iloc`
6. **Visualization** — bar charts and box plots using matplotlib

---

## Requirements

```
numpy
pandas
matplotlib
jupyter
```

Install with:

```bash
pip install numpy pandas matplotlib jupyter
```

---

## Usage

```bash
jupyter notebook
```

The dataset is downloaded automatically on first run. Source: [U.S. Census Bureau](https://www.census.gov/data/tables/time-series/demo/geographic-mobility/state-to-state-migration.html)
