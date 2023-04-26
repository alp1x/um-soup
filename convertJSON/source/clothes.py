import os
import json
import sys

class TerminalColors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

um_soup_ascii = r'''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢀⣴⠂⣠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⢀⡾⠃⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⠘⣧⡀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠈⢷⡄⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠼⠃⠰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀
    ⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀
    ⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣉⣉⣉⣉⣉⣉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀
[um-soup] - FiveM Clothes File Finder
[uyuyorum-team] - uyuyorum ~ sequester
[discord] - discord.gg/uyuyorum
'''

print(f"{TerminalColors.WARNING}{um_soup_ascii}{TerminalColors.ENDC}")

prompt_text = f"{TerminalColors.WARNING}Please enter the clothes folder [stream] path:{TerminalColors.ENDC} "
folder_path = input(prompt_text)

directory = r'{}'.format(folder_path)

if not directory.endswith(r'\stream'):
    print(f"{TerminalColors.FAIL}Please specify only the [stream] folder of your clothes folder{TerminalColors.ENDC}")
    sys.exit()

def extract_root_name(filename):
    # Kök adını dosya adından çıkarır
    return filename.split('^')[0]

def extract_category(filename):
    # Kategori adını dosya adından çıkarır ve gerektiğinde 'p_' önekini kaldırır

    parts = filename.split('^')[1].split('_')
    category = parts[0]
    if category.startswith('p'):
        category = parts[1]
    return category.upper()

def extract_item_number(filename):
    # Öğe numarasını dosya adından çıkarır ve başındaki sıfırları kaldırır
    parts = filename.split('^')[1].split('_')
    
    # Eğer parts listesi yeterli uzunlukta değilse, hata olmaması için bir default değer - um
    if len(parts) < 4:
        return "0"

    number = parts[3] if parts[2].startswith('diff') else parts[2]
    if number.startswith('0') and not number.startswith('000'):
        return number.lstrip('0')
    elif number.startswith('000'):
        return '0'
    else:
        return number

def extract_texture_letter(filename):
    # Texture harfini dosya adından çıkarır
    
    parts = filename.split('^')[1].split('_')
    diff_str = None
    for part in parts:
        if part.startswith('diff'):
            diff_str = part
            break
    if diff_str is not None:
        return parts[parts.index(diff_str) + 2]
    else:
        return None


clothes_dict = {}

for filename in os.listdir(directory):
    # '.ydd' veya '.ytd' içeren ve '^' ile ayrılmış dosya adlarını işler

    if ('.ydd' in filename or '.ytd' in filename) and '^' in filename:
        root_name = extract_root_name(filename)
        category = extract_category(filename)

        # Gerekirse kök adı ve kategori için boş sözlükler oluşturur

        if root_name not in clothes_dict:
            clothes_dict[root_name] = {}
        if category not in clothes_dict[root_name]:
            clothes_dict[root_name][category] = {}

        item_number = extract_item_number(filename)

        # .ydd dosyaları için öğe numarasını ve textures listesini oluşturur

        if filename.endswith('.ydd'):
            if item_number not in clothes_dict[root_name][category] and not item_number.endswith('.ydd'):
                clothes_dict[root_name][category][item_number] = {"textures": []}

        # .ytd dosyaları için, textures listesine texture harflerini ekler

        if filename.endswith('.ytd'):
            texture_letter = extract_texture_letter(filename)
            if texture_letter is not None and texture_letter.endswith('.ytd'):
                texture_letter = texture_letter[:-4]
            if texture_letter is not None:
                #print("item_number: ", item_number)
                if item_number not in clothes_dict[root_name][category]:
                    clothes_dict[root_name][category][item_number] = {"textures": []}
                if texture_letter not in clothes_dict[root_name][category][item_number]["textures"]:
                    clothes_dict[root_name][category][item_number]["textures"].append(texture_letter)
                    clothes_dict[root_name][category][item_number]["textures"].sort()

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(os.path.dirname(current_directory))
target_directory = os.path.join(parent_directory, "web", "build")
output_file_path = os.path.join(target_directory, "clothes.json")

with open(output_file_path, 'w') as output_file:
    json.dump(clothes_dict, output_file) # no indent

file_size_bytes = os.path.getsize(output_file_path)
file_size_kb = file_size_bytes / 1024
print(f"{TerminalColors.OKGREEN}Done! | File Size: {file_size_kb:.2f}KB{TerminalColors.ENDC}")
