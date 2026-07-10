import requests
from bs4 import BeautifulSoup
import re
import os
from pypdf import PdfWriter
import shutil

#the things I want!
url = "https://www.rgpvonline.com/btech-e-all-question-papers.html#4s" #putting the url of pyq web
valid_years = {'2022','2023','2024','2025'} #how many years pyq I want
subject_variations = ["control-systems", "control-system"]
subject_name = "Control_Systems"
target_links = []

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

all_links = soup.find_all('a')
print(f"🔍 Scanned the page and found {len(all_links)} total links.")

print(f'----HUNTING FOR {subject_variations} WORK IN PROGRESS----')

for link in all_links:
    href = link.get('href')
    text = link.text
    found_years = set(re.findall(r'\b\d{4}\b', text)) #turning the years into set

    if href and (any(variant in text.lower() for variant in subject_variations)) and (valid_years & found_years):
        #print(f"Visible text : {text.strip()}")
        #print(f"The Link: {href}")
        pdf_link = href.replace(".html", ".pdf") #convertin .html into .pdf
        target_links.append(pdf_link) #I wanna store the links in list
    
print(f"📊 Successfully collected total {len(target_links)} papers.")

#now I make a space to hold files
os.makedirs("temp_papers",exist_ok=True)

# We create an empty list to keep track of our local file names
downloaded_files = []

for i, url in enumerate(target_links): #enumerate huh
    # Get the raw data from the internet
    response = requests.get(url)
    raw_pdf_data = response.content
    
    # Create a unique name for this file inside our folder
    file_name = f"temp_papers/paper_{i}.pdf"
    
    # Save it to your hard drive
    with open(file_name, "wb") as file:
        file.write(raw_pdf_data)
        
    # Remember this filename for the merging step later
    downloaded_files.append(file_name)

#now step to merge
merger = PdfWriter()

for file_path in downloaded_files:
    print(f"Stapling: {file_path}")
    merger.append(file_path)

with open(f"{subject_name}_Master_PYQ.pdf", "wb") as output_file:
    merger.write(output_file)

merger.close()
print("SUCCESS!! /ᐠ.｡.ᐟ\ᵐᵉᵒʷˎˊ˗")

if os.path.exists("temp_papers"):
    try:
        shutil.rmtree("temp_papers")
        print("🧹 Cleaned up! The 'temp_papers' folder has been deleted completely.")
    except PermissionError:
        print("⚠️ Windows delayed the folder delete, sweeping individual files instead...")
        for file_path in downloaded_files:
            try:
                os.remove(file_path)
            except Exception:
                pass
