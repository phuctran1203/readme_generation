import subprocess

# repository_path is the path to your local repository after cloning into your machine
# readme_saved_path is the path where you want to save the generated README.md file
# repository_path and readme_saved_path should be set to your actual paths
# Exaple: 
# repository_path: "C:\Users\your\real\path\to\your\repository"
# readme_saved_path: "C:\Users\your\real\path\to\save\README.md"

repository_path = r"replace your path here"
readme_saved_path = r"replace your path here"

if(not repository_path or not readme_saved_path):
    input("Enter the path to your local repository: ", repository_path)
    input("Enter the path to save the generated README.md: ", readme_saved_path)

command = f'readmeai -r "{repository_path}" -o "{readme_saved_path}"'

try:
    subprocess.run(command, check=True, shell=True)
    print("README.md generated successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error generating README: {e.output}")