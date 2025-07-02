# 🚀 HealthMLOpsX

**HealthMLOpsX** is a hybrid-cloud, production-ready AI + MLOps platform that integrates:
- SageMaker CV models (TensorFlow / optional PyTorch)
- Vertex AI structured models / BigQuery ML
- LangChain RAG chatbot (Hugging Face + Pinecone)
- Databricks Spark ML pipelines
- FastAPI secured with OAuth2 / JWT / audit logging
- Full MLOps stack (MLflow, Prometheus, Grafana, Sentry)
- Infrastructure-as-Code (Terraform + Helm)
- CI/CD (GitHub Actions with canary deployment + rollback)
- Streamlit / BI hooks (Power BI / Looker ready)

---

## 🏗 Architecture

```mermaid
flowchart TD
  A[GitHub Actions CI/CD] --> B[Terraform + Helm]
  B --> C[AWS / GCP / Azure infra]
  C --> D[SageMaker CV Model]
  C --> E[Vertex AI / BigQuery ML]
  C --> F[Databricks Spark ETL / MLlib]
  D & E & F --> G[FastAPI API]
  G --> H[LangChain RAG + Pinecone]
  G --> I[MLflow tracking]
  G --> J[Prometheus + Grafana + Sentry monitoring]
  G --> K[Streamlit / Power BI frontend]
⚡ Quick Start
🐳 Build + Push API
bash
Copy
Edit
docker build -t avvv19/healthmlopsx-api:latest -f docker/Dockerfile.api .
docker push avvv19/healthmlopsx-api:latest
🏗 Infra + App Deploy
bash
Copy
Edit
terraform apply
helm upgrade --install healthmlopsx ./infra/helm
🎯 Local Access URLs
Service	URL
FastAPI	http://127.0.0.1:8000/docs
Prometheus	http://127.0.0.1:30090
Grafana	http://127.0.0.1:30300

Use minikube service prometheus or grafana if NodePort is configured.

📦 Project Structure
pgsql
Copy
Edit
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
