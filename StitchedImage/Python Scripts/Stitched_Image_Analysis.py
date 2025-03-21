import os
import csv
from ij import IJ, WindowManager
from ij.measure import ResultsTable

# -------------------------------
# CONFIGURATION
# -------------------------------
base_path = "folder_file_path/Data"  # Path containing channel folders
output_path = "folder_file_path/CSV"  # Path for CSV files
channels = ["Channel_" + str(i) for i in range(1, 9)]  # Channel folders: Channel_1 to Channel_8

# Ensure output path exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# -------------------------------
# PROCESS EACH CHANNEL
# -------------------------------
for channel in channels:
    channel_path = os.path.join(base_path, channel)
    if not os.path.isdir(channel_path):
        print("Skipping missing channel folder: " + channel)
        continue

    image_files = sorted([f for f in os.listdir(channel_path) if f.endswith(('.tif', '.png', '.jpg', '.oir'))])

    if not image_files:
        print("No image files found in " + channel)
        continue

    cell_counts = []

    for img_file in image_files:
        img_path = os.path.join(channel_path, img_file)
        print("Processing: " + img_file + " in " + channel)

        # Extract frame number from filename (assuming 'frame_###.tif' format)
        frame_num = int(''.join([c for c in img_file if c.isdigit()]))

        # Open image using ImageJ
        imp = IJ.openImage(img_path)
        if imp is None:
            print("Error: Could not open " + img_file)
            continue

        # Convert to 8-bit and threshold
        IJ.run(imp, "8-bit", "")
        IJ.run(imp, "Auto Threshold", "method=Yen white")
        IJ.run(imp, "Convert to Mask", "")

        # Analyze Particles
        IJ.run("Set Measurements...", "area redirect=None decimal=3")
        IJ.run(imp, "Analyze Particles...", "size=10-Infinity show=Nothing summarize")

        # Extract cell count from Results Table
        rt = ResultsTable.getResultsTable()
        if rt is not None:
            cell_count = rt.getCounter()
        else:
            cell_count = 0  # Default to 0 if results table is missing

        cell_counts.append((frame_num, cell_count))

        # Close image
        imp.changes = False
        imp.close()
        IJ.run("Clear Results")

    # Sort by frame number before saving
    cell_counts.sort()

    # -------------------------------
    # SAVE RESULTS TO CSV
    # -------------------------------
    csv_file = os.path.join(output_path, channel + "_cell_counts.csv")
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Frame Number", "Cell Count"])
        writer.writerows(cell_counts)

    print("Results saved for " + channel + " in " + csv_file)
