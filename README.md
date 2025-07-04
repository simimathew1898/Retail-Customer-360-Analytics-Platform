# Retail Customer 360 Analytics Platform

An AWS-native cloud data architecture project that builds a 360° view of retail customers by integrating data from orders, marketing campaigns, and customer support. This end-to-end project is built using real-world data and AWS Free Tier services — showcasing data lake design, pipeline orchestration, and analytics.

---

## Project Goals

- Simulate a real enterprise retail analytics use case  
- Build a modular, secure AWS-native data architecture  
- Learn data lake zoning, ETL pipelines, IAM security, CI/CD, and more  
- Demonstrate cloud architect skills using AWS best practices  

---

## Use Case

> Build a 360° view of customer interactions across **sales**, **marketing**, and **support** channels using raw CSV files.

---

## Tech Stack

| Category        | Tools/Services Used                                                                 |
|----------------|--------------------------------------------------------------------------------------|
| Data Lake    | Amazon S3 (raw / trusted / final zones)                                             |
| ETL/ELT      | AWS Glue, Pandas, dbt (for modeling)                                                 |
| Warehouse    | Amazon RDS for PostgreSQL (AWS Free Tier)                                           |
| Modeling     | Star Schema, Campaign Click Logs, Order Summaries                                   |
| Security     | IAM, S3 Bucket Policies, Encryption (KMS), VPC                                       |
| Orchestration| AWS Step Functions, EventBridge                                                      |
| Visualization| Streamlit dashboard (local) or Amazon QuickSight                                     |
| Monitoring   | Amazon CloudWatch, CloudTrail, SNS alerts                                            |
| CI/CD        | GitHub Actions, IaC with AWS CloudFormation                                          |
| Docs         | Markdown, Diagrams (draw.io), Data Dictionary                                        |

---

## Project Structure

```bash
Retail-Customer-360-Analytics-Platform/
├── data/
│   ├── orders/
│   │   ├── orders.csv
│   │   └── orders_cleaned.csv
│   ├── marketing/
│   │   ├── marketing.csv
│   │   └── marketing_cleaned.csv
│   └── support/
│       ├── support.csv
│       └── support_tickets_sample.json
│
├── notebooks/
│   ├── clean_orders.ipynb
│   ├── clean_marketing.ipynb
│   └── generate_support_sample.ipynb
│
├── glue_jobs/
│   └── (ETL scripts if any)
├── .github/
│   └── workflows/  # GitHub Actions for CI/CD
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Datasets Used

| Dataset              | Source (Kaggle)                                                                 | Description                                 |
|----------------------|----------------------------------------------------------------------------------|---------------------------------------------|
| Orders               | [Online Retail Dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data) | E-commerce transaction logs                 |
| Marketing Campaigns  | [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) | Marketing + CRM data                        |
| Support Tickets      | [Customer Support on Twitter](https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter) | Tweet-based customer support logs           |

---

## Sample Datasets in Repo

| File Name                              | Purpose                  |
|----------------------------------------|--------------------------|
| `orders_cleaned.csv`                   | Filtered and formatted order data   |
| `marketing_cleaned.csv`                | Flattened customer-campaign matrix |
| `support_tickets_sample.json`          | Sample of 300 support interactions (original JSON > 400MB) |

> **Note:** Full-size datasets are too large for GitHub and are stored in S3 or locally.

---

## Next Steps

| Sprint       | Tasks                                                             |
|--------------|-------------------------------------------------------------------|
| Sprint 1     | Create secure S3 Data Lake with raw/trusted/final zones           |
| Sprint 2     | Upload cleaned data to appropriate zones using AWS CLI/Lambda     |
| Sprint 3     | Build ETL pipeline using AWS Glue (or pandas script for local dev)|
| Sprint 4     | Model data in PostgreSQL (RDS) using Star Schema                  |
| Sprint 5     | Visualize key metrics via Streamlit dashboard or QuickSight       |
| Sprint 6     | Add CI/CD, monitoring, alerts, and security best practices        |

---

## Skills Demonstrated

- Designing secure, cost-effective AWS data lakes  
- Writing modular ETL pipelines with real-world logic  
- Simulating campaign, sales, and support engagement tracking  
- Handling large files, GitHub LFS, and open-source tooling  
- Documentation, version control, and project-based storytelling  

---

## To Run Locally

```bash
# Clone repo
git clone https://github.com/simimathew1898/Retail-Customer-360-Analytics-Platform.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Author

**Simi Mathew**  
👨‍💻 Data & Cloud Engineering Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/simimathew1898/) | [GitHub](https://github.com/simimathew1898)
