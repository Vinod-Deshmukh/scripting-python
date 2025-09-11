import os
import re
import csv

directory_path='D:/august-2025/scripting-python/file-and-text-scripts/emails'
email_pattern=r"[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails=set()
# step 1:Loop through all text files.
for file_name in os.listdir(directory_path):
    if file_name.endswith('.txt'):
        file_path=os.path.join(directory_path,file_name)

    with open(file_path,'r',encoding='utf-8') as f:
        content=f.read()
        found=re.findall(email_pattern,content)
        emails.update(found)

# step 2: Wrirte emails to a csv files.
output_file=os.path.join(directory_path,"email.csv")
with open(output_file,'w',newline='')as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['Email'])
    for email in sorted(emails):
        writer.writerow([email])

print(f'✅ Extracted {len(emails)} unique emails and saved to {output_file}')