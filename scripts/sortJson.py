import sys
import json
import os

def sort_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except ValueError:
        print("Error: The file content is not valid JSON.")
        return

    sorted_data = sort_dict(data)
    print("Sorting done.")
    sorted_file_path = os.path.join(os.path.dirname(file_path), 'sorted-' + os.path.basename(file_path))
    
    with open(sorted_file_path, 'w') as sorted_file:
        json.dump(sorted_data, sorted_file, indent=4)
    
    print(f"Sorted JSON has been saved to: {sorted_file_path}")

def sort_dict(d):
    if isinstance(d, dict):
        return {k: sort_dict(v) for k, v in sorted(d.items())}
    if isinstance(d, list):
        sorted_list = [sort_dict(i) for i in d]
        # return sorted_list

        ## uncomment the above return and coment out the below if you do not need the list to be sorted by the sort_key
        sort_key = "blockId"
        return sorted(sorted_list, key=lambda x: x[sort_key] if isinstance(x, dict) and sort_key in x else float('inf'))
    else:
        return d

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort_json.py <file_path>")
    else:
        sort_json(sys.argv[1])
