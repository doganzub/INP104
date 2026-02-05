import os
import json

def clean_notebook(file_path):
    try:
        print(f"Cleaning {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)

        # Process all cells
        if 'cells' in nb:
            for cell in nb['cells']:
                if cell.get('cell_type') == 'code':
                    cell['outputs'] = []
                    cell['execution_count'] = None
        
        # Save the notebook
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Successfully cleaned {file_path}")
        return True
    except Exception as e:
        print(f"Error cleaning {file_path}: {e}")
        return False

def main():
    root_dir = "."
    notebooks_cleaned = 0
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modify dirnames in-place to skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            
        for filename in filenames:
            if filename.endswith(".ipynb"):
                file_path = os.path.join(dirpath, filename)
                if clean_notebook(file_path):
                    notebooks_cleaned += 1

    print(f"\nTotal notebooks cleaned: {notebooks_cleaned}")

if __name__ == "__main__":
    main()
