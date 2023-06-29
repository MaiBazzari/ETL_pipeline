﻿# ETL Pipeline 

This is my first Repository done during WAIA(Data analysis/Data Engineering) bootcamp.
My first ETL Pipeline will be etl1
## Requirements 
- psycopg2-binary
- pandas
- boto3
## Instructions
To run it locally first build the image.
```bash
  docker image build -t etl1 .
```
Then run the etl job using docker:
```bash
  docker run --env-file .env etl1 
```



