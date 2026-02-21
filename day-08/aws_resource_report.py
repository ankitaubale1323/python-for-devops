import boto3
import json
from datetime import datetime

def get_ec2_instances():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })

    return instances


def get_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    buckets = []

    for bucket in response["Buckets"]:
        buckets.append({
            "BucketName": bucket["Name"]
        })

    return buckets


def main():
    report = {
        "timestamp": str(datetime.utcnow()),
        "ec2_instances": get_ec2_instances(),
        "s3_buckets": get_s3_buckets()
    }

    # Print to terminal
    print(json.dumps(report, indent=4))

    # Save to file
    with open("aws_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nReport saved to aws_report.json")


if __name__ == "__main__":
    main()
