# LOGFLOW Analyzer

### Steps for running the script

1. Clone the repository in your desired local location. The scipt for analyzing the logflow is named `logflow_analyzer.py`
2. There are two modes for running the script.
    1. **Auto mode**: Run the script `logflow_analyzer.py` readily by running the command
                   `python3 logflow_analyzer.py`. This mode uses the sample logflow file (`logs.txt`) and the lookup table (`lookup.csv`) provided as part of this repository
    
    2. **Custom mode**: This enables the script to run against your own logflow file and the lookup files. The script can be run by executing the command `python3 logflow_analyzer.py <absoulte/path/to/logflow/file.txt> <absolute/path/to/lookupfile.csv>`

3. The output files for showing the count of tags is generated as `tagcount.csv` and the port-protocol count is generated in the file named `portprotocount.csv` in the same location as the script in the format specified in the requirement.

### Assumptions

1. The script runs only for the flow log file version 2
2. I am assuming the formatting of the flow log file and the lookup tables are proper as specified in the problem statement.
3. The script is tested in windows and mac.
4. The script uses a map for mapping protocol numbers with the protocol names that is based on https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml.
There could chances of mismatches with the lookup file provided that may have entries that say for eg. `xns-idp` or `leaf-1` and the corresponding lookup files may have these as `xns_idp` or `leaf_1`. These may cause the log entries to be Untagged

### Tests performed

1. Added empty lines, extra spaces in the log files and lookup files to handle extra lines.
2. Scaled the size of the log file to about 12MBs and tested the script.
3. Tried to run the script in both windows and mac environments.