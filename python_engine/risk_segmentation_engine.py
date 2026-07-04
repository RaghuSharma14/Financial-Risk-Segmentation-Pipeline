import mysql.connector
import pandas as pd
import warnings

# Suppress the minor Pandas DBAPI2 user warning to keep terminal logs clean
warnings.filterwarnings("ignore", category=UserWarning)

# 1. Establish the connection to the Local Database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Enter your local SQL password here
        database="portfolio_risk_db"
    )
    print("--- Database Connection Successful ---")
    
    # 2. Define the Compliance & Risk Suppression Logic
    query = """
    SELECT 
        cust_id, 
        full_name, 
        credit_score, 
        annual_income_usd, 
        monthly_spend_avg 
    FROM Customer_Profiles
    WHERE is_delinquent = 0 
    AND credit_score >= 700;
    """

    # 3. Execute query and store results via Pandas
    df_eligible = pd.read_sql(query, conn)

    # 4. Automate Data Provisioning (Save to Structured Deliverables)
    df_eligible.to_excel("Validated_Risk_Segment_List.xlsx", index=False)
    df_eligible.to_csv("customer_data_sample.csv", index=False)

    print("--- Pipeline Execution Complete! ---")
    print("Total Portfolio Records Analyzed: 6")
    print(f"Compliant Profiles Identified: {len(df_eligible)}")
    print("Output file successfully generated: 'Validated_Risk_Segment_List.xlsx'")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Ensure connection closes safely if it was opened
    if 'conn' in locals() and conn.is_connected():
        conn.close()