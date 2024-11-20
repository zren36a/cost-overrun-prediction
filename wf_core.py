import subprocess

# Orchestrate the workflow
def run_workflow():
    subprocess.run(['python', 'wf_datagen.py'])
    subprocess.run(['python', 'wf_dataprocessing.py'])
    subprocess.run(['python', 'wf_visualization.py'])

if __name__ == "__main__":
    print("Calculate the MD5 Hash below, then do other required works.")
    run_workflow()
