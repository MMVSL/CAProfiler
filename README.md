# CA Profiler


CA Profiler is a ML tool that allows the prediction of the potential activity of small molecules against four isoforms of human carbonic anhydrases: I, II, IX and XII. This repository provides a Python script for activity prediction using a predefined environment and dependencies. 

## Installation

To set up the required environment, use the provided YAML file:

```sh
conda env create -f env.yml
```

Then, activate the environment:

```sh
conda activate env
```

## Usage

Run the prediction script with Python, specifying the desired isoform:

```sh
python ca_profiler.py -ci 1 -in input.csv -out output.csv
```

### Input
- The input file must be a CSV containing a column named `SMILES`, which represents the molecular structures.
- A sample CSV file (dataset_example.csv) is included in the repository for testing purposes.

### Output
- The script will generate a CSV file with the prediction results indicating whether each molecule is predicted to have activity against the selected target.

## Dependencies

All necessary dependencies are included in `env.yml`.
