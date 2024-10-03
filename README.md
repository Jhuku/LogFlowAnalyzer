# LOGFLOW Analyzer

### Steps for running the script

1. Clone the repository in your desired local location. The scipt for analyzing the logflow is named `logflow_analyzer.py`
2. There are two modes for running the script.
    1. **Auto mode**: Run the script `logflow_analyzer.py` readily by running the command
                   `python3 logflow_analyzer.py`. This mode uses the sample logflow file (`logs.txt`) and the lookup table (`lookup.csv`) provided as part of this repository
    
    2. **Custom mode**: This enables the script to run against your own logflow file and the lookup files. The script can be run by executing the command `python3 logflow_analyzer.py <absoulte/path/to/logflow/file.txt> <absolute/path/to/lookupfile.csv>`

3. The output files for showing the count of tags is generated as `tagcount.csv` and the port-protocol count is generated in the file named `portprotocount.csv` in the same location as the script in the format specified in the requirement.