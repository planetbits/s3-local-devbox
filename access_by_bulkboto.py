import logging 
from bulkboto3 import BulkBoto3
 
logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(levelname)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
 
TARGET_BUCKET = "test-bucket"
NUM_TRANSFER_THREADS = 50
TRANSFER_VERBOSITY = True
 
# instantiate a BulkBoto3 object
bulkboto_agent = BulkBoto3(
    resource_type="s3",
    endpoint_url="http://127.0.0.1:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="admin123",
    max_pool_connections=300,
    verbose=TRANSFER_VERBOSITY,
)
 
bulkboto_agent.create_new_bucket(bucket_name=TARGET_BUCKET)
 
bulkboto_agent.upload_dir_to_storage(
    bucket_name=TARGET_BUCKET,
    local_dir="test_dir",
    storage_dir="my_storage_dir",
    n_threads=NUM_TRANSFER_THREADS,
)