import pandas as pd
import os
import glob
import config

def count_new_tracks_per_frame(input_dir, output_file_path):
    # Initialize an empty DataFrame to store the combined results
    combined_df = pd.DataFrame()

    # List all CSV files in the input directory
    input_files = glob.glob(os.path.join(input_dir, '*.csv'))

    # Process each file
    for file_path in input_files:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Ensure FRAME and TRACK_ID are numeric, coerce non-numeric values to NaN
        data['FRAME'] = pd.to_numeric(data['FRAME'], errors='coerce')
        data['TRACK_ID'] = pd.to_numeric(data['TRACK_ID'], errors='coerce')

        # Drop rows with NaN values in FRAME and TRACK_ID
        data = data.dropna(subset=['FRAME', 'TRACK_ID'])

        # Find the minimum frame for each track
        min_frames = data.groupby('TRACK_ID')['FRAME'].min()

        # Count the number of new tracks appearing in each frame
        new_tracks_count = min_frames.value_counts().sort_index()

        # Sort the frame numbers numerically and create a DataFrame with new tracks count
        sorted_frame_cols = sorted(new_tracks_count.index, key=lambda x: int(x))
        output_df = pd.DataFrame([new_tracks_count.reindex(sorted_frame_cols, fill_value=0).astype(int)])
        output_df.index = [os.path.basename(file_path)]

        # Append the results to the combined DataFrame
        combined_df = pd.concat([combined_df, output_df])

    # Sort columns numerically except for the last two which will be 'Total' and 'Average'
    sorted_cols = sorted([col for col in combined_df.columns if col not in ['Total', 'Average']], key=lambda x: int(x))
    combined_df = combined_df[sorted_cols]

    # Calculate the total and average new tracks and add them to the DataFrame
    combined_df['Total'] = combined_df.sum(axis=1)

    # Calculate the average excluding the '0' frame
    if '0' in combined_df.columns:
        average_cols = [col for col in combined_df.columns if col != '0']
        combined_df['Average'] = combined_df[average_cols].mean(axis=1)
    else:
        combined_df['Average'] = combined_df.mean(axis=1)

    # Write the combined DataFrame to a CSV file
    combined_df.to_csv(output_file_path)

if __name__ == "__main__":
    # Use the paths from the config file
    input_dir = config.NEW_TRACKS_INPUT_FOLDER
    output_dir = config.NEW_TRACKS_OUTPUT_FOLDER

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to the output CSV file
    output_file_path = os.path.join(output_dir, 'new_tracks_perframe.csv')

    # Count new tracks per frame for all files and output to a single CSV file
    count_new_tracks_per_frame(input_dir, output_file_path)

    print(f'Results written to {output_file_path}')
