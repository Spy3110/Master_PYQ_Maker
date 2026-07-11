import requests
from bs4 import BeautifulSoup
import re
import os
from pypdf import PdfWriter
import shutil

#some custom functions
def display_banner():
    print("====================================================")
    print("      RGPV AUTOMATED PAPER HARVESTER v1.0          ")
    print("====================================================")
#-----------------------------------------------------------------------------------------------
def get_user_choice():
    display_banner()

    print("[*] Available Branches:")
    print(" 1. Computer Science (CSE)")
    print(" 2. Electronics & Communication (ECE)")
    print(" 3. Electrical & Electronics (EX)")
    print(" 4. Mechanical Engineering (ME)")
    print(" 5. Civil Engineering (CE)")
    print(" 6. All branch First year")

    branch_choice = input("\n[?] What's your branch?[1-6]: ").strip()

    if branch_choice == "1":
        branch_code = "btech-cse"
    elif branch_choice == "2":
        branch_code = "btech-e"
    elif branch_choice == "3":
        branch_code = "btech-e"
    elif branch_choice == "4":
        branch_code = "btech-me"
    elif branch_choice == "5":
        branch_code = "btech-civil"
    else:
        branch_code = "rgpv-first-year"

    display_banner()
    semester = input("[?] Enter your Semester number (e.g., 3, 4, 5): ").strip()

    display_banner()
    subject_query = input("[?] Enter the subject keyword (e.g., control-systems): ").strip().lower()

    if branch_code == "rgpv-first-year":
        target_url = "https://www.rgpvonline.com/rgpv-first-year.html#list"
    else:
        target_url = f"https://rgpvonline.com/{branch_code}-all-question-papers.html#{semester}s"

    return target_url, subject_query
#-----------------------------------------------------------------------------------------------------------

def download_manager(target_url, subject_query):
    valid_years = {'2022', '2023', '2024', '2025'} 
    target_links = []
    
    # Simple check to handle missing headers if the university site acts up
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(target_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_links = soup.find_all('a')
    
    print(f"Scanned the page and found {len(all_links)} total links.")
    print(f'----HUNTING FOR {subject_query} WORK IN PROGRESS----')

    for link in all_links:
        href = link.get('href')
        text = link.text
        found_years = set(re.findall(r'\b\d{4}\b', text))

        # FIX 1 & 2: Moved inside the loop and simplified the string check
        if href and (subject_query in text.lower()) and (valid_years & found_years):
            pdf_link = href.replace(".html", ".pdf")
            
            # Make sure it's an absolute URL before adding to the list
            if not pdf_link.startswith('http'):
                pdf_link = f"https://www.rgpvonline.com/{pdf_link.lstrip('/')}"
                
            target_links.append(pdf_link)

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

    with open(f"{subject_query}_Master_PYQ.pdf", "wb") as output_file:
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
#--------------------------------------------------------------------------------------------------------

def main():

    target_url, subject_query = get_user_choice()

    print("\n[+] Target URL Constructed successfully!")
    print(f"[*] Targeting: {target_url}")
    print(f"[*] Searching for papers matching: '{subject_query}'")

    download_manager(target_url, subject_query)
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------------------  
