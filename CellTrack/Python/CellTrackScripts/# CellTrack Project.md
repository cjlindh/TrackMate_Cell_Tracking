# CellTrack Project

## Overview
The CellTrack project is designed to analyze cell tracking data from CSV files. It includes scripts for calculating displacements, extracting tracks with the least displacement below a threshold, counting new tracks per frame, counting trapped tracks, and calculating capture efficiency.

## Configuration
The `config.py` file contains important configuration settings for the project. It defines the file paths for input CSV files, output analysis folders, and other parameters used in the analysis scripts. Here's a breakdown of the configuration settings:

- `CSV_FOLDER`: The folder containing the input CSV files with tracking data.
- `ANALYSIS_FOLDER`: The main folder where analysis results will be stored.
- `SCRIPTS_FOLDER`: The folder containing the Python scripts for analysis.
- `DISPLACEMENTS_FOLDER`: The folder within `ANALYSIS_FOLDER` where displacement analysis results will be saved.
- `TRAPPED_TRACK_FOLDER`: The folder within `ANALYSIS_FOLDER` where extracted trapped tracks will be saved.
- `NUMBER_OF_TRAPPED_CELLS_FOLDER`: The folder within `ANALYSIS_FOLDER` where the count of trapped tracks will be saved.
- `NEW_TRACKS_INPUT_FOLDER`: The folder containing input CSV files for counting new tracks per frame (usually the same as `CSV_FOLDER`).
- `NEW_TRACKS_OUTPUT_FOLDER`: The folder within `ANALYSIS_FOLDER` where the count of new tracks per frame will be saved.
- `TRAPPED_TRACKS_COUNT_FOLDER`: The folder within `ANALYSIS_FOLDER` where the count of trapped tracks for each input file will be saved.
- `CAPTURE_EFFICIENCY_FOLDER`: The folder within `ANALYSIS_FOLDER` where capture efficiency data will be saved.
- `consecutive_frames`: The number of consecutive frames to consider in the displacement analysis.
- `trapped_distance_threshold`: The maximum displacement that counts as a track being trapped.

## Running the Scripts
1. **Displacement Analysis:** Calculates the maximum and least displacements of cells within consecutive frames.
2. **Extracting Tracks:** Extracts tracks with the least displacement below a specified threshold.
3. **Counting New Tracks:** Counts the number of new tracks appearing in each frame.
4. **Trapped Tracks Count:** Counts the number of trapped tracks and their occurrences in each frame.
5. **Capture Efficiency:** Calculates the capture efficiency based on the number of trapped cells and total track count.

## Output Analysis Folder Structure
The results of the analysis are saved in the following subfolders within the Analysis folder:
- **Displacements:** Contains CSV files with the maximum and least displacements of cells within consecutive frames.
- **Trapped Track:** Contains CSV files with extracted tracks that have the least displacement below the specified threshold.
- **Trapped Cells:** Contains CSV files with the count of trapped tracks and their occurrences in each frame.
- **New Tracks Analysis:** Contains a CSV file with the count of new tracks appearing in each frame.
- **Trapped Tracks Count:** Contains a CSV file with the count of trapped tracks for each input CSV file.
- **Capture Efficiency:** Contains a CSV file with the capture efficiency data for each input CSV file.
