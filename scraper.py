from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, ElementClickInterceptedException, ElementNotInteractableException
)
from bs4 import BeautifulSoup
import pandas as pd
import time


n = int(input("no_of_projects_we_want_extract_from_that_page : "))

driver = webdriver.Chrome()
driver.get("https://rera.odisha.gov.in/projects/project-list")
wait = WebDriverWait(driver, 20)

results = []

for i in range(n):
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.project-card.mb-3")))
    projects = driver.find_elements(By.CSS_SELECTOR, ".card.project-card.mb-3")
    project = projects[i]
    print(f"Processing project {i+1}")

    view_btn = project.find_element(By.CSS_SELECTOR, "a.btn.btn-primary")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_btn)
    time.sleep(0.8)
    try:
        view_btn.click()
    except (ElementClickInterceptedException, ElementNotInteractableException):
        driver.execute_script("arguments[0].click();", view_btn)
        time.sleep(0.5)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-tabs")))

    # --- ENSURE PROJECT OVERVIEW TAB IS ACTIVE ---
    overview_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'Project Overview')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", overview_tab)
    time.sleep(0.5)
    try:
        overview_tab.click()
    except (ElementClickInterceptedException, ElementNotInteractableException):
        driver.execute_script("arguments[0].click();", overview_tab)
        time.sleep(0.5)

    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    try:
        overview = soup.find('app-project-overview')
        rera_no = overview.find('label', string='RERA Regd. No.').find_next('strong').text.strip()
        project_name_detail = overview.find('label', string='Project Name').find_next('strong').text.strip()
    except Exception:
        rera_no = project_name_detail = "N/A"

    # --- PROMOTER DETAILS TAB ---
    promoter_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'Promoter Details')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", promoter_tab)
    time.sleep(0.5)
    try:
        promoter_tab.click()
    except (ElementClickInterceptedException, ElementNotInteractableException):
        driver.execute_script("arguments[0].click();", promoter_tab)
        time.sleep(0.5)

    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    try:
        promoter = soup.find('app-promoter-details')
        promoter_name_detail = promoter.find('label', string='Company Name').find_next('strong').text.strip()
        promoter_address = promoter.find('label', string='Registered Office Address').find_next('strong').text.strip()
        gst_no = promoter.find('label', string='GST No.').find_next('strong').text.strip()
    except Exception:
        promoter_name_detail = promoter_address = gst_no = "N/A"

    results.append({
        "Rera Regd. No": rera_no,
        "Project Name": project_name_detail,
        "Promoter Name": promoter_name_detail,
        "Promoter Address": promoter_address,
        "GST No.": gst_no
    })

    driver.back()
    time.sleep(2)

driver.quit()

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv("odisha_rera_projects.csv", index=False)
print("Scraping complete! Data saved to odisha_rera_projects.csv")
