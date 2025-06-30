import logging
from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

from app import config
from app.rag_pipeline import generate_answer

# ————————————————
# Logging
# ————————————————
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("healthmlopsx")

# ————————————————
# Prometheus metrics
# ————————————————
REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"]
)
REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "Latency of HTTP requests in seconds",
    ["method", "endpoint"]
)

# ————————————————
# FastAPI setup
# ————————————————
app = FastAPI(title="HealthMLOpsX RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

# ————————————————
# Middleware for metrics
# ————————————————
@app.middleware("http")
async def metrics_middleware(request, call_next):
    method   = request.method
    endpoint = request.url.path
    with REQUEST_LATENCY.labels(method, endpoint).time():
        response = await call_next(request)
    REQUEST_COUNT.labels(method, endpoint, response.status_code).inc()
    return response

# ————————————————
# Health endpoint
# ————————————————
@app.get("/health", summary="Service health check")
async def health():
    try:
        _ = generate_answer("ping")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

# ————————————————
# Metrics endpoint
# ————————————————
@app.get("/metrics")
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

# ————————————————
# Root & Ask endpoints
# ————————————————
@app.get("/", summary="API is alive")
async def root():
    return {"message": "🚀 RAG API up and running!"}

@app.get("/ask", summary="Run a RAG query")
async def ask(query: str):
    if not query.strip():
        raise HTTPException(status_code=422, detail="Query cannot be empty")
    logger.info(f"Received query: {query}")
    resp = generate_answer(query)
    logger.info(f"Responded in {resp['duration_ms']} ms")
    return resp
