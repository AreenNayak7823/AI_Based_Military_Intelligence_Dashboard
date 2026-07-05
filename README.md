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


## 🧠 Predictive Machine Learning Engine Deep-Dive

The core predictive capability of this dashboard is powered by a **Random Forest Classifier** implemented via `scikit-learn`. The system dynamically anticipates adversary attack methodologies based on regional, historical, and tactical input attributes.

### 1. Feature Engineering & Preprocessing
To optimize classification accuracy, the pipeline extracts and processes key features from the raw dataset:
* **Categorical Encoding:** High-cardinality categorical fields (such as target types, weapon domains, and operational regions) are mapped into optimized numerical vectors using label and frequency encoding.
* **Missing Value Imputation:** Missing data dimensions are handled via high-speed statistical mode imputation to preserve dataset structural integrity without introducing sample bias.
* **Dimensionality Selection:** Features are restricted to high-signal operational indicators (e.g., region, country, target type) to prevent model overfitting and maintain sub-millisecond local inference times.

### 2. The Model Architecture
We utilize an optimized **Random Forest Classifier**, an ensemble learning method that builds a collection of uncorrelated structural decision trees. 
* **The Voting Ensemble:** Each tree in the forest casts a tactical classification vote for the target profile. The model aggregates these individual trees and outputs the class with the highest majority vote.
* **Why Random Forest?** It inherently handles complex non-linear relationships, resists overfitting due to feature bagging, and scales incredibly well with high-volume datasets like the Global Terrorism Database (GTD).

### 3. Training & Performance Verification
* **Train-Test Split:** The historical matrix is randomly partitioned using an 80/20 split configuration (80% training data to build the decision trees, 20% independent testing data to evaluate accuracy).
* **Evaluation Metrics:** The system evaluates model performance utilizing a multi-class Confusion Matrix, tracking **Precision** (avoiding false alarms) and **Recall** (ensuring critical threat vectors aren't missed).
* **Model Serialization:** Once trained via `train_attack_model.py`, the optimal weights and decision paths are serialized into `attack_model.pkl`. The multi-page Streamlit application loads this lightweight file into memory using caching, allowing instant predictions in the UI without re-training.
*
