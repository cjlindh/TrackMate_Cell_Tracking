import os

CSV_FOLDER = 'folder_file_path/CSV' # Output from TrackMate
ANALYSIS_FOLDER = 'folder_file_path/Analysis' # All data will output here
SCRIPTS_FOLDER = 'folder_file_path/CellTrackScripts'

DISPLACEMENTS_FOLDER = os.path.join(ANALYSIS_FOLDER, 'Displacements')
TRAPPED_TRACK_FOLDER = os.path.join(ANALYSIS_FOLDER, 'Trapped Track')
NUMBER_OF_TRAPPED_CELLS_FOLDER = os.path.join(ANALYSIS_FOLDER, 'Trapped Cells')
NEW_TRACKS_INPUT_FOLDER = CSV_FOLDER
NEW_TRACKS_OUTPUT_FOLDER = os.path.join(ANALYSIS_FOLDER, 'New Tracks Analysis')
TRAPPED_TRACKS_COUNT_FOLDER = os.path.join(ANALYSIS_FOLDER, 'Trapped Tracks Count')  # New folder for Trapped Tracks Count
CAPTURE_EFFICIENCY_FOLDER = os.path.join(ANALYSIS_FOLDER, 'Capture Efficiency')  # New folder for Capture Efficiency
consecutive_frames = 4  # Number of consecutive frames
trapped_distance_threshold = 0.1  # The maximum displacement that counts as trapped
