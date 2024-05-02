# S3 Bucket Small File Counter

This Python script helps you count the number of files in an Amazon S3 bucket that are smaller than or equal to a specified size. The script uses the AWS SDK for Python, Boto3, to interact with AWS S3.

## Requirements

To run this script, you need:
- Python 3.x installed on your machine.
- Boto3 library installed. You can install it using `pip install boto3`.
- AWS CLI configured with appropriate AWS credentials and permissions to access the S3 service.

## How It Works

The script performs the following steps:

1. **Initialize a Client**: It initializes a client for the S3 service using Boto3. This client allows the script to interact with your S3 buckets.

2. **Bucket Name and Size Threshold**: The script takes two command-line arguments:
   - The name of the S3 bucket you want to analyze.
   - The maximum file size (in bytes) for counting. Files smaller than or equal to this size will be counted.

3. **Pagination Handling**: Since a bucket can contain a large number of files, the script uses pagination to manage large lists of objects efficiently. It fetches lists of objects in the bucket in manageable batches.

4. **Counting Files**: The script iterates over each batch of objects. If an object's size is less than or equal to the specified maximum size, it increments the count.

5. **Error Handling**: If there's an issue accessing the bucket or listing its contents (e.g., due to permissions issues), the script catches the error and prints an error message.

6. **Output**: Finally, the script prints the count of files that are smaller than or equal to the specified size.

## Usage

To use this script, navigate to the directory containing the script in your command line interface and run:

```bash
python s3_small_file_counter.py <bucket_name> <max_file_size_in_bytes>
