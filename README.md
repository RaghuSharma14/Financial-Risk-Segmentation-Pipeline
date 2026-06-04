# 💳 SQL-Driven Risk Segmentation & Portfolio Analytics Engine

## 📌 Project Overview
This repository contains an end-to-end data pipeline designed to automate **Customer Risk Segmentation** and **Risk Eligibility** workflows. The project mirrors the responsibilities of a Risk Management Analyst by applying automated credit score thresholds and delinquency filters to isolate high-value, low-risk account segments for safe business execution.

By integrating **SQL**, **Python**, and **Power BI**, the tool transforms raw relational data into validated "Golden Lists" while maintaining 100% adherence to risk suppression policies.

---

🛠️ Technical Stack
* **Database:** MySQL (Relational data storage and querying).
* **Data Processing:** Python (Pandas) for automated risk logic application.
* **Business Intelligence:** Power BI for executive-level visualization.
* **Deliverables:** Automated Excel generation (`Validated_Risk_Segment_List.xlsx`) for downstream risk reporting.

---

## 🚀 Risk Suppression Logic
To ensure "Flawless Delivery," the engine applies a multi-layered filter:
1. **Credit Risk Filter:** Only includes accounts with a **Credit Score > 700**.
2. **Delinquency Suppression:** Automatically excludes accounts with an active **Delinquency Flag**.
3. **Value Targeting:** Prioritizes high-tier customers based on income and spend patterns.

---

## 📊 Data Visualization & Insights
Once the Python engine generates the validated target list, the data is visualized in **Power BI** to provide actionable business insights:

* **Regional Distribution (Pie Chart):** Analyzed the geographic spread of eligible customers to identify market concentration. (As noted in the analysis, the **West region** showed the highest concentration).
* **Risk vs. Reward (Scatter Chart):** Mapped **Credit Score** against **Annual Income** to identify high-net-worth outliers for premium tiering while ensuring all candidates meet the minimum credit threshold.
* **Target Quantification (Card):** Used dynamic cards to track the real-time count of eligible targets for the segment.



---

## 💡 How to Run & Replicate
Follow these steps to execute the full pipeline:

### 1. Database Setup (SQL)
* Open MySQL Workbench and run the script in `/sql_scripts/database_setup.sql`. 
* This initializes the `Customer_Profiles` table with raw historical data.

### 2. Run the Risk Engine (Python)
* Navigate to the `/python_engine` folder and run `risk_segmentation_engine.py`.
* The script connects to the database, applies the risk filters, and generates `Validated_Risk_Segment_List.xlsx`.

### 3. Generate the Dashboard (Power BI)
* Open **Power BI Desktop/Service**.
* Select **Get Data > Excel** and upload the generated file.
* Map the fields to create the **Card**, **Pie Chart**, and **Scatter Chart** as described in the Visualization section.

---

## 📂 Repository Structure
* **`/sql_scripts`**: SQL code to recreate the environment.
* **`/python_engine`**: The automation script and sample data file.
* **`/Dashboard`**: Screenshots of the final Power BI report for quick reference.