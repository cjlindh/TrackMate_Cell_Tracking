import os
import csv
import matplotlib.pyplot as plt

# -------------------------------
# CONFIGURATION
# -------------------------------
base_path = "folder_file_path/CSV"  # Path to the folder containing CSV files
output_path = "folder_file_path/Plots"  # Path for saving the plots
channels = ["Channel_" + str(i) for i in range(1, 9)]  # Channel folders: Channel_1 to Channel_8

# Ensure output path exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# -------------------------------
# PLOT EACH CHANNEL
# -------------------------------
for channel in channels:
    # Define the path for the CSV file
    csv_file = os.path.join(base_path, channel + "_cell_counts.csv")
    
    if not os.path.exists(csv_file):
        print(f"Skipping missing CSV file for {channel}: {csv_file}")
        continue
    
    # Read the CSV file
    frame_numbers = []
    cell_counts = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            frame_numbers.append(int(row[0]))  # Frame number
            cell_counts.append(int(row[1]))  # Cell count
    
    # Create a line plot
    plt.figure(figsize=(8, 6))
    plt.plot(frame_numbers, cell_counts, marker='o', linestyle='-', color='b')
    plt.title(f"Channel {channel.split('_')[1]}: Number of Counted Cells vs Frame Number")
    plt.xlabel("Frame Number")
    plt.ylabel("Number of Counted Cells")
    plt.grid(True)
    
    # Save the plot as an image
    plot_file = os.path.join(output_path, f"{channel}_cell_counts_plot.png")
    plt.savefig(plot_file)
    plt.close()  # Close the figure to avoid memory issues

    print(f"Plot saved for {channel} at {plot_file}")

