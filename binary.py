def convert_binary_to_int(binary_string):
  """Converts a binary string to an integer."""
  return int(binary_string, 2)

def sort_binary_numbers(file_path, output_file_path):
  """
  Sorts binary numbers from a file in ascending order and writes them to another file.

  Args:
      file_path: Path to the file containing binary numbers.
      output_file_path: Path to the output file where sorted numbers will be written.
  """

  # Read binary numbers from the file
  with open(file_path, "rb") as f:
    lines = f.readlines()

  # Convert binary strings to integers for efficient sorting
  numbers = [convert_binary_to_int(line.strip()) for line in lines]
  numbers.sort()

  # Convert sorted integers back to binary strings
  sorted_binary_numbers = [bin(num)[2:] for num in numbers]

  # Write sorted binary numbers to the output file
  with open(output_file_path, "wb") as f:
    for binary_number in sorted_binary_numbers:
      f.write(f"{binary_number}\n".encode())

# Example usage
file_path = "binary_numbers.txt"
output_file_path = "sorted_binary_numbers.txt"
sort_binary_numbers(file_path, output_file_path)

print(f"Binary numbers sorted and written to '{output_file_path}'.")
