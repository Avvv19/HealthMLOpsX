provider "aws" {
  region = "us-east-1"
}
resource "aws_s3_bucket" "mlops_bucket" {
  bucket = "healthmlopsx-storage"
}
