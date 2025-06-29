provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "healthmlopsx_bucket" {
  bucket = "healthmlopsx-${random_id.bucket_suffix.hex}"
  acl    = "private"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}
