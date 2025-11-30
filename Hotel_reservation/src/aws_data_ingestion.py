import boto3
from botocore.exceptions import ClientError
from pathlib import Path

class DataIngestion:
    def __init__(self, config: dict, logger, path:Path):
        self.logger = logger
        self.local_path = path
        self.bucket = config["s3_bucket"]
        self.s3_prefix = config["s3_prefix"]
        self.region = config.get("region", "ap-south-1")
        self.aws_profile = config.get("aws_profile", "default")

        self._validate_inputs()
        self.s3_client = self._init_s3_client()

    def _validate_inputs(self):
        if not self.local_path.exists():
            raise FileNotFoundError(f"Local file does not exist: {self.local_path}")

    def _init_s3_client(self):
        session = boto3.Session(profile_name=self.aws_profile, region_name=self.region)
        return session.client("s3")

    def upload(self):
        s3_key = f"{self.s3_prefix}{self.local_path.name}"

        try:
            self.logger.info(f"Uploading {self.local_path} → s3://{self.bucket}/{s3_key}")
            self.s3_client.upload_file(str(self.local_path), self.bucket, s3_key)
            self.logger.info("Upload successful.")
            return {"bucket": self.bucket, "key": s3_key}
        except ClientError as e:
            self.logger.error(f"S3 upload failed: {e}")
            raise

    def delete(self):
        s3_key = f"{self.s3_prefix}{self.local_path.name}"

        try:
            self.logger.info(f"Deleting s3://{self.bucket}/{s3_key}")
            self.s3_client.delete_object(Bucket=self.bucket, Key=s3_key)
            self.logger.info("Deletion successful.")
        except ClientError as e:
            self.logger.error(f"S3 deletion failed: {e}")
            raise
