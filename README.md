# CellTrack Scripts
# Made by Camilla J. Lindh and Ivan Wang, 2024

## Overview
This collection of Python scripts is designed to analyze cell tracking data. The scripts perform various tasks such as calculating displacements, filtering based on least displacement thresholds, and counting the number of trapped cells.

## Scripts

### 1. Celltrack_Displacements.py
Calculates the maximum and least displacement of cells within a specified number of consecutive frames. The results are saved to a CSV file.

### 2. Celltrack_Count_Trapped_Cells.py
Filters tracks with a least displacement less than a specified threshold (trapped distance) and saves the filtered tracks to a new CSV file.

### 3. Trapped_Cell_Count.py
Counts the number of tracks in the filtered files (representing trapped cells) and saves the counts to a CSV file.

### 4. CellTrack.py
Runs all the scripts in a specified order, as defined in the `scripts_order.txt` file.

## Configuration
The `config.py` file contains the paths to various directories used by the scripts. Update this file to reflect the correct paths for your data and output files.

## Usage
1. Update the `config.py` file with the correct paths.
2. Ensure that the `scripts_order.txt` file lists the scripts in the desired order of execution.
3. Run the `CellTrack.py` script to execute all the scripts in the specified order.

## Requirements
- Python 3.x
- Pandas library

## License
[MIT](https://choosealicense.com/licenses/mit/)
