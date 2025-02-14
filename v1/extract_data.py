import os
import lzma
from tqdm import tqdm
from multiprocessing import cpu_count
import concurrent.futures

def process_file(args):
    directory, filename, output_file = args
    file_path = os.path.join(directory, filename)
    try:
        with lzma.open(file_path, "rt", encoding="utf-8") as infile:
            text = infile.read()
        with open(output_file, "a", encoding="utf-8") as outfile:
            outfile.write(text)
        characters = set(text)
        return characters
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return set()

def xz_files_in_dir_recursive(directory):
    # Recursively collect all .xz files from subdirectories
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".xz"):
                files.append((root, filename))  # Store directory and filename as a tuple
    return files

def process_files_in_parallel(files, output_file):
    vocab = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        args = [(directory, filename, output_file) for directory, filename in files]
        for characters in tqdm(executor.map(process_file, args), total=len(files)):
            vocab.update(characters)
    return vocab

def main():
    folder_path = "openwebtext"
    output_file_train = "output_train.txt"
    output_file_val = "output_val.txt"
    vocab_file = "vocab.txt"

    # Get all .xz files in folder_path and its subdirectories
    files = xz_files_in_dir_recursive(folder_path)
    total_files = len(files)

    # Split files into training (90%) and validation (10%) sets
    split_index = int(total_files * 0.9)
    files_train = files[:split_index]
    files_val = files[split_index:]

    # Ensure output files are empty before appending
    open(output_file_train, 'w').close()
    open(output_file_val, 'w').close()

    # Process training files
    print("Processing training files...")
    vocab_train = process_files_in_parallel(files_train, output_file_train)

    # Process validation files
    print("Processing validation files...")
    vocab_val = process_files_in_parallel(files_val, output_file_val)

    # Combine vocabularies and write to vocab.txt
    vocab = vocab_train.union(vocab_val)
    with open(vocab_file, "w", encoding="utf-8") as vfile:
        for char in sorted(vocab):
            vfile.write(char + '\n')

if __name__ == "__main__":
    main()
