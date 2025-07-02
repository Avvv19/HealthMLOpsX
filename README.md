# 🚀 HealthMLOpsX

**HealthMLOpsX** is a hybrid-cloud AI + MLOps platform for healthcare, delivering:
- ✅ **Multi-cloud AI (AWS SageMaker, GCP Vertex AI, Azure ML)**
- ✅ **LangChain RAG chatbot (Hugging Face + Pinecone)**
- ✅ **TensorFlow + PyTorch CV models**
- ✅ **Databricks Spark ML pipeline**
- ✅ **MLOps (MLflow, Prometheus, Grafana, Sentry)**
- ✅ **FastAPI API secured with OAuth2, JWT, audit logging**
- ✅ **Infra-as-code (Terraform + Helm)**
- ✅ **CI/CD via GitHub Actions with canary deploy + rollback**
- ✅ **Streamlit / Power BI / Looker integration-ready**

---

## 📌 Architecture

flowchart TD
  CI[GitHub Actions CI/CD] --> TF[Tf / Helm]
  TF --> CLOUD[AWS / GCP / Azure]
  CLOUD --> SM[SageMaker CV Model]
  CLOUD --> VA[Vertex AI / BigQuery ML]
  CLOUD --> DB[Databricks Spark]
  SM & VA & DB --> API[FastAPI + OAuth2 + JWT]
  API --> RAG[LangChain RAG + Pinecone]
  API --> ML[MLflow Tracking]
  API --> MON[Prometheus / Grafana / Sentry]
  API --> FE[Streamlit / Power BI Frontend]

⚡ Quick Start
1️⃣ Build + Push API Docker image
docker build -t avvv19/healthmlopsx-api:latest -f docker/Dockerfile.api .
docker push avvv19/healthmlopsx-api:latest

2️⃣ Deploy Infra + App
terraform apply
helm upgrade --install healthmlopsx ./infra/helm

3️⃣ Local URLs (minikube tunnel may be needed)
FastAPI Docs	http://127.0.0.1:8000/docs
Prometheus	http://127.0.0.1:30090
Grafana	http://127.0.0.1:30300

🗂 Project Structure
pgsql
Copy
Edit
HealthMLOpsX/
├── app/
│   ├── api.py
│   ├── security.py
│   ├── rag_pipeline.py
│   ├── mlflow_tracker.py
├── docker/
│   └── Dockerfile.api
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
│       ├── outputs.tf
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── frontend/
│   └── streamlit_app.py
├── tests/
├── README.md
