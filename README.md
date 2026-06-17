# Real-Time Data Platform

A production-style streaming data platform built using:

- Apache Kafka
- Apache Spark Structured Streaming
- Delta Lake
- Apache Airflow
- Docker
- Terraform
- AWS S3

## Problem Statement

Modern e-commerce platforms generate millions of user events every day.

This project demonstrates a scalable streaming architecture that:

- Ingests clickstream and order events
- Processes events in real time
- Performs data quality checks
- Stores curated data in Delta Lake
- Orchestrates quality validation using Airflow
- Deploys infrastructure using Terraform

## Architecture

┌──────────────┐
│ Event Source │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Kafka     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Spark Stream │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Delta Lake   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Airflow DAG  │
└──────────────┘

## Features

- Real-time event ingestion
- Event schema validation
- Deduplication
- Delta Lake storage
- Data quality checks
- Workflow orchestration
- Infrastructure as Code

## Tech Stack

Python
Kafka
Spark
Delta Lake
Airflow
Terraform
Docker
AWS

## Future Enhancements

- Great Expectations
- Prometheus Monitoring
- Grafana Dashboards
- Kubernetes Deployment
- CI/CD with GitHub Actions
