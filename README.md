# API_to_S3

## Environment variables
```
TWITTER_CONSUMER_KEY  
TWITTER_SECRET_KEY
BUCKET_NAME
```
And AWS credentials

## Run
### Poetry for virtual environment management
```
poetry shell
poetry install
```
### Run API calls and data ingestion to RDS
```
python main.py
```
### Run Elasticsearch upload and queries
```
python es_upload.py
python es_query.py
```

### Run Twitter API calls to find posts and relationships
```
python create_graph_data.py
```
