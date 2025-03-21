import pandas as pd
import os
import glob
import config

def calculate_capture_efficiency(input_dir, output_folder, total_tracks_file, trapped_tracks_count_file):
    # Read the total tracks count data and the trapped tracks count data
    total_tracks_df = pd.read_csv(total_tracks_file)
    trapped_tracks_count_df = pd.read_csv(trapped_tracks_count_file)

    # Get the name of the leftmost column (assumed to be the filename column)
    filename_column = total_tracks_df.columns[0]

    # Initialize a list to store the data for each file
    data_list = []

    # List all CSV files in the input directory
    input_files = glob.glob(os.path.join(input_dir, '*.csv'))

    # Process each file
    for input_file in input_files:
        # Find the file name
        file_name = os.path.basename(input_file)

        # Find the total track count, the trapped track count, and the initial frame count for this file
        total_track_count = total_tracks_df[total_tracks_df[filename_column] == file_name]['Total'].iloc[0]
        trapped_track_count = trapped_tracks_count_df[trapped_tracks_count_df['File Name'] == file_name]['Number of Trapped Cells'].iloc[0]
        initial_frame_count = trapped_tracks_count_df[trapped_tracks_count_df['File Name'] == file_name]['Frame 0'].iloc[0]

        # Calculate the capture efficiency, captured - initial, and the new capture efficiency
        capture_efficiency = trapped_track_count / total_track_count if total_track_count > 0 else 0
        captured_initial = trapped_track_count - initial_frame_count
        new_capture_efficiency = captured_initial / (total_track_count - initial_frame_count) if (total_track_count - initial_frame_count) > 0 else 0

        # Store the counts in a dictionary
        file_data = {
            'File Name': file_name,
            'Number of Trapped Cells': trapped_track_count,
            'Total Track Count': total_track_count,
            'Capture Efficiency': capture_efficiency,
            'Trapped Cells - Initial': captured_initial,
            'Total Tracks - Initial': total_track_count - initial_frame_count,
            'New Capture Efficiency': new_capture_efficiency
        }

        # Append the dictionary to the data list
        data_list.append(file_data)

    # Convert the data list to a DataFrame
    capture_efficiency_df = pd.DataFrame(data_list)

    # Write the DataFrame to a CSV file
    output_file_path = os.path.join(output_folder, 'capture_efficiency.csv')
    capture_efficiency_df.to_csv(output_file_path, index=False)

    print(f'Capture Efficiency written to {output_file_path}')

if __name__ == "__main__":
    # Input directory containing the CSV files
    input_dir = config.TRAPPED_TRACK_FOLDER

    # Output directory for the capture efficiency data
    output_folder = os.path.join(config.ANALYSIS_FOLDER, 'Capture Efficiency')

    # Path to the CSV file containing total track counts
    total_tracks_file = os.path.join(config.NEW_TRACKS_OUTPUT_FOLDER, 'new_tracks_perframe.csv')

    # Path to the CSV file containing trapped tracks count
    trapped_tracks_count_file = os.path.join(config.TRAPPED_TRACKS_COUNT_FOLDER, 'trapped_tracks_count.csv')

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Calculate the capture efficiency and write the results to a CSV file
    calculate_capture_efficiency(input_dir, output_folder, total_tracks_file, trapped_tracks_count_file)
