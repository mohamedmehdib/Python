import os

def find_largest_files(directory, num_files=10):
  largest_files = []
  for root, _, files in os.walk(directory):
    for file in files:
      file_path = os.path.join(root, file)
      file_size = os.path.getsize(file_path)
      largest_files.append((file_path, file_size))

  largest_files.sort(key=lambda x: x[1], reverse=True)

  return largest_files[:num_files]

root_directory = "C:\\"
num_largest_files = 10

largest_files = find_largest_files(root_directory, num_largest_files)

for file_path, file_size in largest_files:
  print(f"{file_path}: {file_size/8/1024} Mo")
