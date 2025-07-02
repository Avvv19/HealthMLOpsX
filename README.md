# 🚀 HealthMLOpsX

**HealthMLOpsX** is a hybrid-cloud, production-grade AI + MLOps platform:
- SageMaker CV models (TensorFlow / PyTorch)
- Vertex AI / BigQuery ML structured models
- LangChain RAG chatbot (Hugging Face + Pinecone)
- Databricks Spark ML pipeline
- FastAPI secured with OAuth2, JWT, audit logging
- MLOps (MLflow, Prometheus, Grafana, Sentry)
- Terraform + Helm infra-as-code
- CI/CD: GitHub Actions with canary deploy & rollback
- Streamlit / Power BI / Looker ready frontend

---
## Architecture

```mermaid
flowchart TD
  A[GitHub Actions CI/CD] --> B[Terraform + Helm]
  B --> C[AWS / GCP / Azure Infra]
  C --> D[SageMaker CV Model]
  C --> E[Vertex AI / BigQuery ML]
  C --> F[Databricks Spark ML]
  D & E & F --> G[FastAPI API]
  G --> H[LangChain RAG + Pinecone]
  G --> I[MLflow Tracking]
  G --> J[Prometheus / Grafana / Sentry]
  G --> K[Streamlit / Power BI Frontend]


Quick Start
Build + Push API

docker build -t avvv19/healthmlopsx-api:latest -f docker/Dockerfile.api .

docker push avvv19/healthmlopsx-api:latest

Deploy Infra + App
terraform apply
helm upgrade --install healthmlopsx ./infra/helm

Local Access URLs
Service	URL

FastAPI	http://127.0.0.1:8000/docs
Prometheus	http://127.0.0.1:30090
Grafana	http://127.0.0.1:30300


📦 Project Structure

HealthMLOpsX/
├── app/
│   ├── api.py
│   ├── security.py
│   ├── rag_pipeline.py
│   ├── cv_model.py
│   ├── structured_model.py
│   └── mlflow_tracker.py
├── docker/
│   └── Dockerfile.api
├── frontend/
│   └── streamlit_app.py
├── infra/
│   ├── helm/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   │       ├── deployment.yaml
│   │       ├── service.yaml
│   │       ├── prometheus.yaml
│   │       ├── grafana.yaml
│   │       └── sentry.yaml
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── tests/
│   └── test_api.py
└── README.md
