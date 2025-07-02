import mlflow

def start_run_tracking(run_name: str):
    mlflow.set_tracking_uri("http://localhost:5000")  # or your mlflow server
    mlflow.set_experiment("HealthMLOpsX")
    with mlflow.start_run(run_name=run_name):
        mlflow.log_param("example_param", 123)
        mlflow.log_metric("example_metric", 0.95)
        mlflow.log_artifact("README.md")  # if any artifact
