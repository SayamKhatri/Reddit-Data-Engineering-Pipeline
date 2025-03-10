# Reddit-Data-Engineering-Pipeline
AWS End to End Data Engineering Project

An automated and scalable ETL pipeline designed for ingesting, transforming, and curating Reddit data daily, enabling comprehensive social media analysis and data-driven decision-making.

## Overview

This project deploys a robust data engineering pipeline leveraging AWS cloud infrastructure. It ingests data from Reddit's APIs, processes it using Apache Airflow and AWS Glue (PySpark), and stores the transformed data into AWS Redshift for analytics. AWS Athena provides serverless querying capabilities, making insights accessible and actionable.

## Technologies Used

- **AWS Glue** – Serverless ETL tool for data transformation.
- **AWS S3** – Data storage and staging area.
- **AWS Redshift** – Data warehousing solution.
- **AWS Athena** – Interactive query service for easy data analysis.
- **Glue Crawler** – Automated schema discovery and metadata management.
- **Apache Airflow** – Workflow orchestration and scheduling.
- **AWS EC2 & Docker** – Containerized environment for ETL tasks.
- **Python & PySpark** – Data processing and scripting.

## Key Features

- **Daily Automated Pipeline**: Seamlessly executes ETL tasks daily, ensuring up-to-date analytics.
- **Scalable Infrastructure**: Containerized deployment with Docker on EC2 for optimal performance and resource utilization.
- **Integrated Workflow**: Orchestrates complex workflows seamlessly using Apache Airflow.
- **Optimized Data Storage**: Utilizes AWS Redshift for high-performance analytical queries and reporting.
- **Cost-effective Querying**: Employs AWS Athena for ad-hoc analysis without maintaining additional infrastructure.

## Architecture

![RedditDataEngineering](https://github.com/user-attachments/assets/76256385-3d10-42a6-be4c-4a4fc4e9cdcc)

## ⚙️ Setup & Deployment

1. **Clone this repository**
   ```bash
   git clone https://github.com/SayamKhatri/Reddit-Data-Engineering-Pipeline.git
   ```
2. **Configure AWS Credentials**
   - Set up AWS CLI and configure access keys.
3. **Deploy Infrastructure**
   - Use provided CloudFormation templates or Terraform scripts.
4. **Build & Run Docker Containers**
   ```bash
   docker build -t reddit-etl .
   docker run reddit-etl
   ```

## 📄 License

This project is open-source under the MIT License. See the [LICENSE](LICENSE) file for details.



