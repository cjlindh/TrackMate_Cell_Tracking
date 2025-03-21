import pandas as pd
import os
import glob
import config

def extract_tracks_with_least_displacement_below_threshold(input_file_path, output_file_path, threshold):
    # Read the output CSV file
    data = pd.read_csv(input_file_path)

    # Filter the tracks with least displacement less than the threshold
    filtered_data = data[data['Least Displacement'] < threshold]

    # Write the filtered data to a new CSV file
    filtered_data.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # Use the paths from the config file
    input_dir = config.DISPLACEMENTS_FOLDER
    output_dir = config.TRAPPED_TRACK_FOLDER

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Threshold for least displacement (trapped distance)
    trapped_distance_threshold = config.trapped_distance_threshold

    # List all CSV files in the input directory
    input_files = glob.glob(os.path.join(input_dir, '*.csv'))

    # Process each file
    for input_file in input_files:
        output_file = os.path.join(output_dir, os.path.basename(input_file))
        extract_tracks_with_least_displacement_below_threshold(input_file, output_file, trapped_distance_threshold)
        print(f'Processed file: {input_file}')
