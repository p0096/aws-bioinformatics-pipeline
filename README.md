# AWS Bioinformatics Pipeline

This project implements a simple bioinformatics pipeline to analyze DNA sequences.
It is designed to be executed in a Linux environment and reflects how basic
bioinformatics workflows are run on remote servers or cloud infrastructure.

## Project goals

- Practice bioinformatics scripting using Python
- Learn how to automate analyses with Bash
- Use Git and GitHub for version control
- Simulate real-world execution on cloud platforms such as AWS

## Pipeline description

The pipeline performs the following steps:

1. Reads DNA sequences from a FASTA file
2. Computes basic statistics:
   - Number of sequences
   - Average sequence length
   - Average GC content
3. Writes a summary report to a results file
4. Automates execution using a Bash script

## Project structure

aws-bioinformatics-pipeline/
├── data/ # Input FASTA files
├── scripts/ # Python and Bash scripts
├── results/ # Output files
└── README.md

## Technologies used

- Python 3
- Bash
- Linux (Ubuntu / WSL)
- Git & GitHub
- AWS (EC2 and S3 – conceptual use)

## How to run the pipeline

From the root directory of the project:

```bash
chmod +x scripts/run_pipeline.sh
./scripts/run_pipeline.sh


After execution, the results will be available in: results/summary.txt

## Future improvements

- Add support for larger datasets

- Include sequence filtering steps

- Run the pipeline on an AWS EC2 instance

- Upload results automatically to Amazon S3

## Author

Paula
