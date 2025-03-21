import os
import subprocess
import config

def run_python_scripts_in_order(folder_path, order_file_path):
    with open(order_file_path, 'r') as file:
        script_order = [line.strip() for line in file if line.strip()]

    for script in script_order:
        script_path = os.path.join(folder_path, script)
        if os.path.exists(script_path):
            print(f"Running script: {script}")
            subprocess.run(['python3', script_path], check=True)
            print(f"Finished running script: {script}")
        else:
            print(f"Script not found: {script}")

if __name__ == "__main__":
    folder_path = config.SCRIPTS_FOLDER
    order_file_path = os.path.join(folder_path, 'scripts_order.txt')
    run_python_scripts_in_order(folder_path, order_file_path)
