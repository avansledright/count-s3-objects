import boto3
import sys
from botocore.exceptions import ClientError
# Initialize a session using your credentials
s3 = boto3.client('s3')

# Define the bucket name
bucket_name = sys.argv[1]

def count_small_files(bucket, object_size):
    count = 0
    paginator = s3.get_paginator('list_objects_v2')
    
    # Create a PageIterator from the paginator
    page_iterator = paginator.paginate(Bucket=bucket)
    try:
        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    if obj['Size'] <= int(object_size):
                        count += 1
        return count
    except ClientError as e:
        print(e)
        print("Failed to get object count")
        return False

if __name__ == "__main__":
    object_size_max = sys.argv[2]
    # Print the count of objects that are 1 MB or less
    print(count_small_files(bucket_name, object_size_max))
