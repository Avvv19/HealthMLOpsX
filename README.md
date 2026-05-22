<div align="center">

<img src="https://komarev.com/ghpvc/?username=Avvv19&label=Views&color=0e75b6&style=flat" alt="views"/>

# HealthMLOpsX

### Hybrid-Cloud AI + MLOps Platform for Healthcare

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://terraform.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## Overview

**HealthMLOpsX** is a production-grade, hybrid-cloud AI + MLOps platform purpose-built for healthcare. It combines multi-cloud model serving, LangChain RAG pipelines, full MLOps observability, and enterprise-grade security into a single deployable platform that helps healthcare organizations build, monitor, and scale AI at clinical speed.

---

## Key Features

| Feature | Description |
|---------|-------------|
| Multi-Cloud AI | AWS SageMaker, GCP Vertex AI, Azure ML integration |
| LangChain RAG | Intelligent chatbot with Hugging Face + Pinecone vector store |
| Deep Learning | TensorFlow CV models + optional PyTorch support |
| Spark ML Pipelines | Databricks-powered large-scale data pipelines |
| MLOps Observability | MLflow + Prometheus + Grafana + Sentry monitoring |
| Secure API | FastAPI with OAuth2, JWT auth, and full audit logging |
| Infrastructure as Code | Terraform + Helm for reproducible deployments |
| CI/CD | GitHub Actions with canary deploy and automatic rollback |
| Frontend | Streamlit dashboard + Power BI / Looker BI connectors |

---

## Tech Stack

**AI & Machine Learning**

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logoColor=white)
![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

**Cloud & Infrastructure**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

**Monitoring & Security**

![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)

---

## Architecture

```
CI/CD (GitHub Actions)
    |
    v
Terraform + Helm --> Cloud Infrastructure (AWS/GCP/Azure)
    |
    |-- SageMaker CV Models + Vertex AI Structured Models
    |-- Databricks Spark ML Pipelines
    |-- FastAPI (OAuth2 + JWT) --> LangChain RAG + Pinecone
    |-- MLflow Tracking + Prometheus + Grafana + Sentry
    |-- Streamlit Frontend + BI Integrations
```

---

## Quick Start

```bash
# Build and push Docker image
docker build -t avvv19/healthmlopsx-api:latest -f docker/Dockerfile.api .
docker push avvv19/healthmlopsx-api:latest

# Deploy infrastructure
terraform apply

# Deploy application
helm upgrade --install healthmlopsx ./infra/helm
```

**Access Services:**

| Service | URL |
|---------|-----|
| FastAPI Docs | http://localhost:8000/docs |
| Prometheus | http://localhost:30090 |
| Grafana | http://localhost:30300 |

---

## Project Structure

```
HealthMLOpsX/
|-- app/
|   |-- api.py               # FastAPI application
|   |-- security.py          # OAuth2 + JWT
|   |-- rag_pipeline.py      # LangChain RAG
|   |-- mlflow_tracker.py    # MLflow tracking
|-- docker/
|   |-- Dockerfile.api
|-- infra/
|   |-- helm/                # Kubernetes Helm charts
|   |-- terraform/           # Infrastructure as code
|-- .github/
|   |-- workflows/
|   |   |-- ci-cd.yml        # GitHub Actions pipeline
|-- frontend/
|   |-- streamlit_app.py
|-- tests/
|-- README.md
```

---

## Features Checklist

- [x] SageMaker + Vertex AI models
- [x] Databricks Spark ML pipeline
- [x] LangChain RAG + Pinecone vector store
- [x] OAuth2 + JWT + audit logging
- [x] MLflow tracking
- [x] Prometheus + Grafana monitoring
- [x] Sentry error monitoring
- [x] GitHub Actions CI/CD with canary deploy
- [x] Terraform infrastructure as code
- [x] Helm chart deployment
- [ ] Power BI / Looker live connectors (extend as needed)

---

## Author

**Venkata Vivek Varma Alluru** | AI in Healthcare | 3+ Years Experience

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/venkatavivekvarmaalluru/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Avvv19)
