# hwf-search-etl
![Unit Test](https://github.com/hwf87/hwf-search-etl/actions/workflows/github-actions.yml/badge.svg?event=push)

This is a data scraping project that sources data from the Houzz e-commerce platform, the CNN YouTube channel, and the TedTalk official website. The implementation uses the Apache Beam framework to build an ETL pipeline and write the results into an Elasticsearch database. The final step visualizes the crawler results using Kibana.

## Medium Blogs
[[Data Engineering] Build a web crawling ETL pipeline with Apache Beam + Elasticsearch + Kibana](https://jackyfu1995.medium.com)

## Architecture Overview
![plot](./docs/app_arch.png)

## How to Start
1. git clone https://github.com/hwf87/hwf-search-etl.git

2. Create a .env file with following configs
> Note that YOUTUBE_API_KEY you can easily create one for yourself from [YouTube Data API v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com).

> ES HOST, USERNAME, PASSWORD can also be modified, but you'll need to do the corresponding work on docker-compose-elk.yaml
```
YOUTUBE_API_KEY={CREATE-ONE-FOR-YOUSELF}
ES_HOST=http://es-container:9200
ES_USERNAME=elastic
ES_PASSWORD=elastic
```

3. Create a virtual environment for testing
```
conda create -n search_engine python=3.8
conda activate search_engine
```

4. Download SentenceTransformer pretrain model from HuggingFace
> You'll be able to find sentence_embedding_model.pth file in model folder after execute following commands.

> If you are using M1 MacOS, and facing issue "Library not loaded: @rpath/libopenblas.0.dylib".

> Try ```conda install openblas``` before you run below.
```
cd ./hwf-search-etl
pip install -r requirements.txt
python ./model/download_pretrain_model.py
```

5. Build Elasticsearch & Kibana Service
> visit http://127.0.0.1:9200 for elasticsearch

> visit http://127.0.0.1:5601 for kibana

> check docker container by 'docker ps'

> check elk_elastic network exists by 'docker network ls'
```
cd ./elk
docker-compose -f docker-compose-elk.yaml up -d
docker ps
docker network ls
```

6. Build Pipeline images
```
cd ./hwf-search-etl
docker build --tag search-etl -f Pipeline.Dockerfile .
docker images
```

7. Run Pipeline
- export RUN_MODE=local | beam
- export DATA_SOURCE=houzz | news | tedtalk
> In average, it'll take around 20 mins for crawling a single source for the most recent 5000 docs.
```
docker run --rm --network elk_elastic --env-file .env search-etl $RUN_MODE $DATA_SOURCE
```

8. Check Results
- Visit http://127.0.0.1:5601 for Kibana and login (username/password)
- Open the menu on the left, click Management >> Dev Tools
- Run the following commands to check the index we just created
```
GET houzz/_count
GET cnn/_count
GET tedtalk/_count
```
![plot](./docs/check_kibana.png)

9. Create your own dashboard with Kibana
- Create Index Pattern
- Go to Analytics >> Dashboard

## Pipeline Design Pattern
![plot](./docs/pipeline_design.png)

## How to run without docker for Debuging
1. Set environment variaables
> Remember to change ES_HOST=http://localhost:9200 in .env file
```
set -a
source .env
set +a
```
2. Execute Pipeline
```
conda activate search_engine
python pipeline.py $RUN_MODE $DATA_SOURCE
```

## Unit Test
```
bash unit_test.sh
```
- Coverage report
```
(search_engine) jackyfu@Macbook-air hwf-search-etl % pytest --cov=./src/ test
============================================================================= test session starts =============================================================================
platform darwin -- Python 3.8.10, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/jackyfu/Desktop/hwf87_git/hwf-search-etl
plugins: mock-3.10.0, cov-4.0.0
collected 86 items

test/test_CrawlerBase.py .......................                                                                                                                        [ 26%]
test/test_ProcessorBase.py sss                                                                                                                                          [ 30%]
test/test_data_extractor.py s................s........s...........                                                                                                      [ 74%]
test/test_data_loader.py ......                                                                                                                                         [ 81%]
test/test_data_transformer.py ......                                                                                                                                    [ 88%]
test/test_init_objects.py ..........                                                                                                                                    [100%]

---------- coverage: platform darwin, python 3.8.10-final-0 ----------
Name                                      Stmts   Miss  Cover
-------------------------------------------------------------
src/CrawlerBase.py                          100      5    95%
src/ProcessorBase.py                         45     19    58%
src/__init__.py                               0      0   100%
src/houzz/houzz_data_extractor.py           128     33    74%
src/houzz/houzz_data_loader.py               24      0   100%
src/houzz/houzz_data_transformer.py          32      0   100%
src/news/__init__.py                          0      0   100%
src/news/news_data_extractor.py              67     11    84%
src/news/news_data_loader.py                 24      0   100%
src/news/news_data_transformer.py            32      0   100%
src/tedtalk/__init__.py                       0      0   100%
src/tedtalk/tedtalk_data_extractor.py       111     22    80%
src/tedtalk/tedtalk_data_loader.py           24      0   100%
src/tedtalk/tedtalk_data_transformer.py      32      0   100%
-------------------------------------------------------------
TOTAL                                       619     90    85%

=========================================================== 80 passed, 6 skipped, 19 warnings in 399.29s (0:06:39) ============================================================
```

## Precommit
- Black config: find ```pyproject.toml```
- Flake8 config: find ```tox.ini```
```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
        name: black
-   repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
```

## CI/CD
- Githun Actions
- Find ```github-actions.yml```
```
[JOB 1] Build
- steps
    - Set up Python
    - Install dependencies
    - Test with pytest
    - Pre-Commit Check
    - Build images
    - Push to github artifactory
[JOB 2] Deploy
- steps
    - Download images from github artifactory
    - Push to github packages
    - Service Deployment
```
