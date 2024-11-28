
# Local S3 Environment for Object Storage with Minio and Python
A Python script that sets up a local S3-like environment for object storage using Minio, allowing you to develop and test S3-compatible applications locally. Connect to the environment using the AWS SDK or CLI, just like you would with real S3.

## S3 Bucket Management with Versioning
This script provides a set of utilities for managing Amazon S3 buckets, including creating a bucket with versioning enabled, uploading files from a folder, and listing the bucket's contents along with object version details.

---
## Features
- **Bucket Creation with Versioning**: Automatically creates a bucket and enables versioning to maintain a history of object changes.
- **Upload Files from a Local Folder**: Recursively uploads all files in a specified local folder to the S3 bucket.
- **List Bucket Contents with Versions**: Displays all objects in the bucket along with their version IDs, size, and latest status.

---
## Prerequisites
1. **Python**: Ensure Python 3.6 or later is installed.
2. **Boto3**: Install the AWS SDK for Python.
   ```bash
    pip install boto3
    ```
3. **AWS Credentials(If need to conect AWS)**: 
    - Set up your AWS access key and secret key. Use an IAM user with appropriate permissions for S3 operations.
    - else use MinIO credential for this
3. **Optional**:  A custom endpoint URL can be configured for services like MinIO.


### How to Use
#### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

#### Step 2: Configure the Script
1. Replace the placeholders in the script with your actual AWS credentials and configurations:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- ENDPOINT_URL (optional, for non-AWS S3-compatible services)
- BUCKET_NAME (name of the S3 bucket)
- FOLDER_PATH (path to the folder to upload)
#### Step 3: Run the Script
```bash
    python access_by_boto3.py
```

## License
This script is open source and available under the GNU Affero GPL License. Contributions are welcome!