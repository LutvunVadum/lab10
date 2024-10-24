import os

directory_path = "ТЕХТ"

full_directory_path = os.path.abspath(directory_path)
print("Повний шлях до каталогу:", full_directory_path)

doc_files = []
docx_files = []
txt_files = []

for file in os.listdir(directory_path):
    if file.endswith(".doc"):
        doc_files.append(file)
    elif file.endswith(".docx"):
        docx_files.append(file)
    elif file.endswith(".txt"):
        txt_files.append(file)

print("Файли з розширенням .doc:", doc_files)
print("Файли з розширенням .docx:", docx_files)
print("Файли з розширенням .txt:", txt_files)

with open(os.path.join(directory_path, "my_files.txt"), "w") as f:
    f.write("Файли з розширенням .doc:\n")
    f.write("\n".join(doc_files) + "\n\n")
    
    f.write("Файли з розширенням .docx:\n")
    f.write("\n".join(docx_files) + "\n\n")
    
    f.write("Файли з розширенням .txt:\n")
    f.write("\n".join(txt_files) + "\n")

print("Дані записані у файл my_files.txt")

