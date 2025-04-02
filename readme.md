* /scrape - files to scrape santa clara county's council website for it's meeting videos with selenium
* /transcribe - transcribing the sccc council videos downloaded with openai-whisper

I hope to create DAGs out of the scraper and transcriber (maybe with dagster, or in the cloud). Next I also want to use LLMs to summarize the meeting data, and split it into 'topics' based on the meeting agenda.

# How to Run

## Scraper
Right now the code pulls one video from one specific meeting (https://sccgov.iqm2.com/Citizens/Detail_Meeting.aspx?ID=16839). Hope to build a DAG that checks the RSS feed for more meetings, and then backfill the video data with that
```
cd scraper
docker-compose build
docker-compose up -d
```

At the moment, the scraping doesn't happen when the docker container launches. You'll have to find the docker container called `python-scraper` and copy the container_id with `docker container ls`.

Then you can get into the container, and run the python script from the CLI
```
docker exec -it CONTAINER_ID_HERE bash
python scripts/test_scrape_videos.py
```

## Transcriber
Uses openai's whisper to transcribe. 

Place the video file you want to transcribe in ~/transcribe. make sure you replace the `Dockerfile` and `
```
cd transcribe
docker-compose build
docker-compose up -d
```

# How does it work?
todo..