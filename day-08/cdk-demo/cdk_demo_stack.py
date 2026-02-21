from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct


class CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self,
            "MyFirstBucket",
            versioned=True
        )