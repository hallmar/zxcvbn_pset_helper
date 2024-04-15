import os
import re
#shamelessly mostly(if not all) written by openai
def process_files(folder_path, dest_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pset"):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(dest_path, filename)
            process_file(input_file, output_file)

def process_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()

    updated_content = re.sub(rb'"(.*track_type.*)": (\d+)', lambda m: b'"' + m.group(1) + b'": ' + bytes(str(int(m.group(2)) + 2), 'utf-8') if int(m.group(2)) > 3 else m.group(0), content)

    with open(output_file, 'wb') as f:
        f.write(updated_content)

# Replace 'folder_path' with the path to your folder containing the .pset files
pset_path = os.path.dirname(os.path.abspath(__file__))+'/original'
mod_pset_path = os.path.dirname(os.path.abspath(__file__))+'/modified'
process_files(pset_path, mod_pset_path)
