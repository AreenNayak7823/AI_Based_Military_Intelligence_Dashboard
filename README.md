# 🛡️ AI-Based Military Intelligence Dashboard

An interactive, multi-page web application designed for tactical intelligence synthesis, geospatial risk visualization, and predictive threat modeling. This terminal relies on the **Global Terrorism Database (GTD)** to analyze over 180,000+ historical incident logs, project threat trajectories, and classify tactical risk vectors using machine learning.

---

## 🎯 Core Analytics Modules

The framework is segmented into dedicated tactical intelligence suites:

1. **🏠 Home Node:** Handles core data load validation, integrity telemetry checks, and active memory allocation monitoring.
2. **🌏 Global Threat Map:** Renders low-latency geospatial scatter plot overlays representing the volume density and target classifications of incidents globally.
3. **🗺️ Country Analysis:** Drills down into localized metrics, aggregating annual target profiles, fatal vs. wounded tracking ratios, and casualty distributions.
4. **🧠 Attack Prediction:** Uses a trained **Random Forest Machine Learning Classifier** to predict incoming adversary tactical methodologies given specific regional intelligence parameters.
5. **🚨 Threat Level Prediction:** Algorithmically weights historical target profiles, frequency thresholds, and localized activity rates to grade current threat posture matrices.
6. **📈 Forward Forecasting:** Generates 5-year mathematical risk vector trendlines utilizing fast linear regression analytics based on historical data.
7. **📋 AI Intelligence Report:** Dynamically compiles a customized, formal text summary briefing on a selected theater of operations with local download capabilities (`.txt`).

---

## 🛠️ Technology Stack

* **Interface & Framework:** Python 3.x, Streamlit (Multi-page configuration)
* **Machine Learning Pipeline:** Scikit-Learn (Random Forest, Linear Regression Vectors)
* **Data Synthesis Engines:** Pandas, NumPy
* **Geospatial & Graphical Rendering:** Plotly Graph Objects, Plotly Express

---

## ⚙️ Repository Layout

```text
├── APP.py                       # Strategic Command Center launcher
├── train_attack_model.py        # ML Random Forest modeling training pipeline
├── attack_model.pkl             # Serialized trained prediction matrix weights
├── .gitignore                   # Excludes heavy database directories from tracking
├── Utils/
│   └── data_loader.py          # Centralized multi-threaded data memory caching pipeline
└── Pages/
    ├── 1_Home.py                # Telemetry & system configurations check
    ├── 2_Global_Threat_Map.py   # Geospatial intelligence scatter mapping
    ├── 3_Country_Analysis.py    # Historical country volume deep dives
    ├── 4_Attack_Prediction.py   # Machine learning deployment gateway
    ├── 5_Threat_Level_Prediction.py # Algorithm risk assessment matrix
    ├── 6_Forecasting.py         # 5-Year projective timeline trends
    └── 7_AI_Intelligence_Report.py # Executive text report builder
