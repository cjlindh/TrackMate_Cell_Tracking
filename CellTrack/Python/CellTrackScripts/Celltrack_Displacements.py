import config

# Use the path from the config file
input_folder = config.CSV_FOLDER
output_folder = config.DISPLACEMENTS_FOLDER

import pandas as pd
import os
import glob


def displacement_within_consecutive_frames(track_data, consecutive_frames):
    # Ensure position columns are numeric, coerce non-numeric values to NaN
    track_data['POSITION_X'] = pd.to_numeric(track_data['POSITION_X'], errors='coerce')
    track_data['POSITION_Y'] = pd.to_numeric(track_data['POSITION_Y'], errors='coerce')

    # Convert the 'FRAME' column to numeric, coerce non-numeric values to NaN
    track_data['FRAME'] = pd.to_numeric(track_data['FRAME'], errors='coerce')

    # Drop rows with NaN values in position columns and 'FRAME' column
    track_data = track_data.dropna(subset=['POSITION_X', 'POSITION_Y', 'FRAME'])

    # Sort the track data by frame
    track_data_sorted = track_data.sort_values(by='FRAME')

    # Check if the track has less than the specified number of consecutive frames
    if len(track_data_sorted) < consecutive_frames:
        return {'Max Displacement': float('nan'), 'Least Displacement': float('nan')}

    # Initialize the maximum and least displacements
    max_displacement = 0
    least_displacement = float('inf')

    # Calculate the first and last frames for the track
    first_frame = track_data_sorted['FRAME'].iloc[0]
    last_frame = track_data_sorted['FRAME'].iloc[-1]

    # Iterate over the track data to find the maximum and least displacements within the specified number of consecutive frames
    for i in range(len(track_data_sorted) - consecutive_frames + 1):
        # Extract the position data for the current window
        window = track_data_sorted.iloc[i:i + consecutive_frames]

        # Calculate the displacement between the first and last position in the window
        displacement = ((window.iloc[-1]['POSITION_X'] - window.iloc[0]['POSITION_X'])**2 + (window.iloc[-1]['POSITION_Y'] - window.iloc[0]['POSITION_Y'])**2)**0.5

        # Update the maximum and least displacements
        max_displacement = max(max_displacement, displacement)
        least_displacement = min(least_displacement, displacement)

    return {'Max Displacement': max_displacement, 'Least Displacement': least_displacement if least_displacement != float('inf') else float('nan'), 'First Frame': first_frame, 'Last Frame': last_frame}

def analyze_file(file_path, output_folder, consecutive_frames):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Ensure TRACK_ID is numeric
    df['TRACK_ID'] = pd.to_numeric(df['TRACK_ID'], errors='coerce')

    # Drop rows with NaN values in TRACK_ID
    df = df.dropna(subset=['TRACK_ID'])

    # Calculate the maximum and least displacements within the specified number of consecutive frames for all Track IDs
    displacements = df.groupby('TRACK_ID').apply(lambda x: displacement_within_consecutive_frames(x, consecutive_frames))

    # Convert the displacements Series to a DataFrame
    displacements_df = displacements.apply(pd.Series)

    # Sort the displacements DataFrame by Track ID
    displacements_df_sorted = displacements_df.sort_index()

    # Determine the output file path based on the input file path and output folder
    output_file_path = os.path.join(output_folder, os.path.basename(os.path.splitext(file_path)[0]) + '.csv')

    # Write the sorted results to a CSV file
    displacements_df_sorted.to_csv(output_file_path, index_label='Track ID', float_format='%.6f')

    print(f'Results written to {output_file_path}')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Specify the number of consecutive frames
consecutive_frames = config.consecutive_frames

# List all CSV files in the input folder
file_paths = glob.glob(os.path.join(input_folder, '*.csv'))

# Analyze each file
for file_path in file_paths:
    analyze_file(file_path, output_folder, consecutive_frames)
