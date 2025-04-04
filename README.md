# itsm-data-pipeline

Overview

This project builds an IT Service Management (ITSM) Data Pipeline using Apache Airflow, DBT, PostgreSQL, and Apache Superset. The pipeline processes ServiceNow ticket data, transforms it, and visualizes key operational metrics.

Project Components

Apache Airflow: Orchestrates data pipeline workflows.

DBT (Data Build Tool): Transforms raw ITSM data into meaningful insights.

PostgreSQL: Stores processed ITSM data for querying.

Apache Superset: Creates interactive dashboards for data visualization.

Features

Automated Data Ingestion: Extract ServiceNow data.

Data Transformation: Clean, format, and structure data using DBT.

KPI & Metrics Calculation: Ticket volume trends, resolution time, closure rate, and backlog analysis.

Interactive Visualization: Dashboards built in Apache Superset.

Installation & Setup

Prerequisites

Docker & Docker Compose

Python (>= 3.8)

PostgreSQL

Apache Airflow

DBT

Apache Superset
