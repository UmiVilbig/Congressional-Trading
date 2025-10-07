Fundementals of a Data Pipeline
1. Collect data from various sources (APIs, files, streams etc)
2. Transform and validate the data into its usuable from
3. Version and store the data
4. Downstream the data to consumers (analytics, ML models etc)

Development Cycle for a Data Pipeline
[Design] → [Prototype] → [Stabilize] → [Automate] → [Scale]

Stage       Goal                                Example
Design      Define what I need and why          "Collect weather data to analyze temperature trends"
Prototype   Write minimal collectors            Script that saves JSON snapshots
Stabilize   Schema validation, error handling   logging and tests
Automate    Add orchestration + versioning      Perfect/Airflow for recurring jobs
Scale       Add kafka, monitoring

Philosophy
collect → normalize → clean → enrich → aggregate → export

How to develop a Pipeline

collectors/api/example.py
pipelines/batch/normalize.py
pipelines/batch/aggregate.py

- Write a new versioned file

You want 
1. Fast feedback
2. No database resets
3. No dependency on external orchestration

Checklist
1. the data collector should only grab the raw data and save it to a versioned file or directory. It should have minimal if any transformation logic
2. data deletion should be kept to a minimum and only done when absolutely necessary