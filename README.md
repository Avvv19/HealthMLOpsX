# HealthMLOpsX

HealthMLOpsX is a personal learning and reference prototype for exploring API serving, retrieval, metrics, containers, and infrastructure configuration. It is not a deployed healthcare platform, a clinically validated system, or a compliance-certified product.

## What is implemented

- FastAPI service modules and API routes
- Retrieval-oriented modules using sentence-transformer/FAISS dependencies
- Prometheus metrics integration
- Docker and Docker Compose configuration
- Example Helm and Terraform files
- Small Spark/PySpark-oriented module
- Test files for selected API and security behavior

## Claim-to-evidence table

| Capability | Repository evidence | Public status |
|---|---|---|
| FastAPI service | `app/api.py` and related modules | Implemented prototype code |
| Retrieval pipeline | `app/rag_pipeline.py` and retrieval dependencies | Implemented prototype path; quality results are not published |
| Prometheus metrics | `app/` metrics code and monitoring configuration | Implemented/configured for local exploration |
| Containers | Dockerfiles and `docker-compose.yml` | Local container configuration |
| Kubernetes/Helm | `infra/helm/` manifests | Reference configuration; no operated cluster evidence |
| Terraform | `infra/terraform/` example | Limited reference example; not a complete environment |
| MLflow | Example/placeholder integration | Exposure only; no saved tracked run proves lifecycle operation |
| Spark/PySpark | `app/spark_pipeline.py` | Small learning implementation |
| AWS SageMaker deployment | No implementation found | Not implemented; future work only |
| GCP Vertex AI integration | No implementation found | Not implemented; future work only |
| Azure ML integration | No implementation found | Not implemented; future work only |
| Drift monitoring and retraining | No reproducible implementation found | Not implemented; future work only |
| A/B model deployment | No implementation found | Not implemented; future work only |
| Formal healthcare compliance | No external assessment or operating controls evidence | Not claimed |

## Local setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.api:app --reload
```

Run the available tests with:

```bash
pytest -q
```

Some dependencies are large and environment-sensitive. A test result should be treated as current only when the exact command and environment are recorded.

## Limitations

- No production deployment or external users are evidenced.
- No clinical validation, PHI processing authorization, or compliance certification is provided.
- Infrastructure files are examples and do not establish an operated environment.
- MLflow values and cloud integration points require real configuration and saved evidence.

## Future work

- Replace placeholder MLflow behavior with a reproducible local run and saved artifact
- Add explicit configuration validation and secret handling
- Expand tests around retrieval, metrics, and failure paths
- Remove tracked runtime/cache artifacts
- Implement a complete cloud path only when it can be tested end to end
