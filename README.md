

````markdown
# 🚀 HealthMLOpsX

**HealthMLOpsX** is a hybrid-cloud AI + MLOps platform built for healthcare. It provides:

- ✅ Multi-cloud AI (AWS SageMaker, GCP Vertex AI, Azure ML)
- ✅ LangChain RAG chatbot (Hugging Face + Pinecone)
- ✅ TensorFlow + optional PyTorch CV models
- ✅ Databricks Spark ML pipeline
- ✅ MLOps observability (MLflow, Prometheus, Grafana, Sentry)
- ✅ FastAPI API with OAuth2, JWT, audit logging
- ✅ Infra-as-code: Terraform + Helm
- ✅ GitHub Actions CI/CD with canary deploy + rollback
- ✅ Streamlit + BI connectors (Power BI / Looker ready)

---

## 📌 Architecture

**Key components**:
- CI/CD (GitHub Actions) → Terraform + Helm → Cloud infra
- SageMaker CV + Vertex AI structured models
- Spark ML pipelines on Databricks
- FastAPI API (OAuth2 + JWT secured) → LangChain RAG + Pinecone
- MLOps monitoring (MLflow + Prometheus + Grafana + Sentry)
- Frontend (Streamlit + BI integrations)

---

## ⚡ Quick Start

### Build + push Docker image
```bash
docker build -t avvv19/healthmlopsx-api:latest -f docker/Dockerfile.api .
docker push avvv19/healthmlopsx-api:latest
````

### Deploy infra + app

```bash
terraform apply
helm upgrade --install healthmlopsx ./infra/helm
```

### Access services (adjust ports if needed)

| Service      | Example URL                                              |
| ------------ | -------------------------------------------------------- |
| FastAPI Docs | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| Prometheus   | [http://127.0.0.1:30090](http://127.0.0.1:30090)         |
| Grafana      | [http://127.0.0.1:30300](http://127.0.0.1:30300)         |

---

## 🗂 Project Structure

```
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
```

---

## ✅ Features Checklist

| Feature                                   | Status                           |
| ----------------------------------------- | -------------------------------- |
| SageMaker + Vertex AI models              | ✔ Implemented                    |
| Databricks Spark ML pipeline              | ✔ Included                       |
| LangChain RAG + Pinecone                  | ✔ Ready                          |
| OAuth2 + JWT + audit logging              | ✔ In API                         |
| MLflow tracking                           | ✔ Included                       |
| Prometheus + Grafana                      | ✔ Running                        |
| Sentry monitoring                         | ✔ Included                       |
| CI/CD (GitHub Actions + Helm + Terraform) | ✔ Configured                     |
| Streamlit + BI connectors                 | ⚠ Placeholder (extend as needed) |

---

## ⚠ Notes

* On **Windows / Minikube**: Use `minikube tunnel` or NodePorts for access.
* Update environment configs (`.env`, Helm values) before production use.
* Power BI / Looker connectors require live setup with credentials.

---

## ✉ Contact

* GitHub: [Avvv19](https://github.com/Avvv19)

---

```

---

### ✅ What’s clean about this version:
- No Mermaid diagram to cause formatting issues.
- No resume/LinkedIn text — fully focused on the project.
- All sections separate, readable, GitHub-renderable without errors.

---

1️⃣ Prometheus Targets Page (2.jpg)
🌟 What it shows:

Both prometheus and node-exporter targets are UP (healthy and scraping metrics).

Includes endpoint details, scrape duration, and no scrape errors.

The browser bar shows 127.0.0.1 indicating local Minikube deployment — this highlights your hands-on setup, not just screenshots from cloud GUIs.


2️⃣ Grafana Explore Page Query (1.jpg)
🌟 What it shows:

Successful query of node_memory_MemAvailable_bytes from Prometheus in Grafana.

Live graph of node memory available over time.

Again, local infra URL is visible (e.g., 127.0.0.1:3000 or similar).


```
