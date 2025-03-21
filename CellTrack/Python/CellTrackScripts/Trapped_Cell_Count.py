import pandas as pd
import os
import glob
import config

def count_trapped_tracks(input_dir, output_folder):
    # Initialize a list to store the data for each file
    data_list = []

    # List all CSV files in the input directory
    input_files = glob.glob(os.path.join(input_dir, '*.csv'))

    # Process each file
    for input_file in input_files:
        # Read the CSV file
        data = pd.read_csv(input_file)

        # Count the number of tracks in the file
        count = data.shape[0]

        # Count the number of tracks starting in each frame
        frame_counts = {f'Frame {frame}': data[data['First Frame'] == frame].shape[0] for frame in range(164)}

        # Store the counts in a dictionary
        file_data = {'File Name': os.path.basename(input_file), 'Number of Trapped Cells': count}
        file_data.update(frame_counts)

        # Append the dictionary to the data list
        data_list.append(file_data)

    # Convert the data list to a DataFrame
    trapped_counts_df = pd.DataFrame(data_list)

    # Write the DataFrame to a CSV file
    output_file_path = os.path.join(output_folder, 'trapped_tracks_count.csv')
    trapped_counts_df.to_csv(output_file_path, index=False)

    print(f'Trapped Tracks Count written to {output_file_path}')

if __name__ == "__main__":
    # Input directory containing the CSV files
    input_dir = config.TRAPPED_TRACK_FOLDER

    # Output directory for the counts
    output_folder = os.path.join(config.ANALYSIS_FOLDER, 'Trapped Tracks Count')

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Count the trapped tracks and write the results to a CSV file
    count_trapped_tracks(input_dir, output_folder)
