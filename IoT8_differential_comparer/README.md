# IoT8 Differential Comparer
Compares OpenAPI based API representations and returns differences.

## Start up

### Install dependencies
pip install -r requirements.txt

### Set environment variables
CONFLICT_SOLVER_URL = ''

### Start server
python main.py path_api_1 path_api_2

Ex.
python main.py C:\api\SHAS_REST_API.json C:\api\SHAS_REST_API_TYPE_CHANGE.json
