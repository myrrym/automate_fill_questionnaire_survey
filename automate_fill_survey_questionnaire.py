def run_survey():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import random
    import time

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # Use WebDriverWait for explicit waits

    try:
        # Open the target webpage
        driver.get('https://surveypluto.com/q/ynVfJptum')  # Replace with the URL of the webpage containing the radio buttons

        # Wait for the page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div1')))  # Ensure the first question is visible

        # Define the page 1 questions and their radio button selectors
        page_1_questions = {
            'q1': 'div#div1 div.ui-controlgroup.column1 div.ui-radio',
            'q2': 'div#div2 div.ui-controlgroup.column1 div.ui-radio',
            'q3': 'div#div3 div.ui-controlgroup.column1 div.ui-radio',
            'q4': 'div#div4 div.ui-controlgroup.column1 div.ui-radio',
            'q5': 'div#div5 div.ui-controlgroup.column1 div.ui-radio',
            'q6': 'div#div6 div.ui-controlgroup.column1 div.ui-radio',
            'q7': 'div#div7 div.ui-controlgroup.column1 div.ui-radio',
            'q8': 'div#div8 div.ui-controlgroup.column1 div.ui-radio',
        }

        # Iterate through each question
        for q, selector in page_1_questions.items():
            try:
                # Find all radio buttons for the current question
                radio_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if radio_buttons:
                    # Exclude specific options for q6 and q7 if needed
                    if q in ['q6', 'q7']:
                        radio_buttons = [rb for rb in radio_buttons if 'Other (please specify)' not in rb.text]

                    # Randomly select one of the radio buttons
                    random_radio_button = random.choice(radio_buttons)

                    # Click on the <a> element to select the radio button
                    radio_button_link = random_radio_button.find_element(By.CSS_SELECTOR, 'a.jqradio')
                    wait.until(EC.element_to_be_clickable(radio_button_link)).click()
            except Exception as e:
                print(f"Error processing question {q}: {e}")

        # Click the "Next Page" button
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div12')))

        # Define the page 2's questions and their option selectors
        page_2_questions = {
            'q12': 'div#div12 div.scale-div ul li.td a.rate-off',
            'q13': 'div#div13 div.scale-div ul li.td a.rate-off',
            'q14': 'div#div14 div.scale-div ul li.td a.rate-off',
            'q15': 'div#div15 div.scale-div ul li.td a.rate-off',
            'q16': 'div#div16 div.scale-div ul li.td a.rate-off',
            'q17': 'div#div17 div.scale-div ul li.td a.rate-off',
            'q18': 'div#div18 div.scale-div ul li.td a.rate-off',
            'q19': 'div#div19 div.scale-div ul li.td a.rate-off',
            'q20': 'div#div20 div.scale-div ul li.td a.rate-off',
            'q21': 'div#div21 div.scale-div ul li.td a.rate-off',
            'q22': 'div#div22 div.scale-div ul li.td a.rate-off',
            'q23': 'div#div23 div.scale-div ul li.td a.rate-off',
            'q24': 'div#div24 div.scale-div ul li.td a.rate-off',
            'q25': 'div#div25 div.scale-div ul li.td a.rate-off',
            'q26': 'div#div26 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each new question
        for q, selector in page_2_questions.items():
            try:
                # Find all options for the current question on the new page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing new page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div28')))

        # Define the page 3's questions and their option selectors
        page_3_questions = {
            'q28': 'div#div28 div.scale-div ul li.td a.rate-off',
            'q29': 'div#div29 div.scale-div ul li.td a.rate-off',
            'q30': 'div#div30 div.scale-div ul li.td a.rate-off',
            'q31': 'div#div31 div.scale-div ul li.td a.rate-off',
            'q32': 'div#div32 div.scale-div ul li.td a.rate-off',
            'q33': 'div#div33 div.scale-div ul li.td a.rate-off',
            'q34': 'div#div34 div.scale-div ul li.td a.rate-off',
            'q35': 'div#div35 div.scale-div ul li.td a.rate-off',
            'q36': 'div#div36 div.scale-div ul li.td a.rate-off',
            'q37': 'div#div37 div.scale-div ul li.td a.rate-off',
            'q38': 'div#div38 div.scale-div ul li.td a.rate-off',
            'q39': 'div#div39 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_3_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div41')))

        # Define the final page's questions and their option selectors
        page_4_questions = {
            'q41': 'div#div41 div.scale-div ul li.td a.rate-off',
            'q42': 'div#div42 div.scale-div ul li.td a.rate-off',
            'q43': 'div#div43 div.scale-div ul li.td a.rate-off',
            'q44': 'div#div44 div.scale-div ul li.td a.rate-off',
            'q45': 'div#div45 div.scale-div ul li.td a.rate-off',
            'q46': 'div#div46 div.scale-div ul li.td a.rate-off',
            'q47': 'div#div47 div.scale-div ul li.td a.rate-off',
            'q48': 'div#div48 div.scale-div ul li.td a.rate-off',
            'q49': 'div#div49 div.scale-div ul li.td a.rate-off',
            'q50': 'div#div50 div.scale-div ul li.td a.rate-off',
            'q51': 'div#div51 div.scale-div ul li.td a.rate-off',
            'q52': 'div#div52 div.scale-div ul li.td a.rate-off',
            'q53': 'div#div53 div.scale-div ul li.td a.rate-off',
            'q54': 'div#div54 div.scale-div ul li.td a.rate-off',
            'q55': 'div#div55 div.scale-div ul li.td a.rate-off',
            'q56': 'div#div56 div.scale-div ul li.td a.rate-off',
            'q57': 'div#div57 div.scale-div ul li.td a.rate-off',
            'q58': 'div#div58 div.scale-div ul li.td a.rate-off',
            'q59': 'div#div59 div.scale-div ul li.td a.rate-off',
            'q60': 'div#div60 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_4_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div62')))

        # Define the final page's questions and their option selectors
        page_5_questions = {
            'q62': 'div#div62 div.scale-div ul li.td a.rate-off',
            'q63': 'div#div63 div.scale-div ul li.td a.rate-off',
            'q64': 'div#div64 div.scale-div ul li.td a.rate-off',
            'q65': 'div#div65 div.scale-div ul li.td a.rate-off',
            'q66': 'div#div66 div.scale-div ul li.td a.rate-off',
            'q67': 'div#div67 div.scale-div ul li.td a.rate-off',
            'q68': 'div#div68 div.scale-div ul li.td a.rate-off',
            'q69': 'div#div69 div.scale-div ul li.td a.rate-off',
            'q70': 'div#div70 div.scale-div ul li.td a.rate-off',
            'q71': 'div#div71 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_5_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div73')))

        # Define the final page's questions and their option selectors
        page_6_questions = {
            'q73': 'div#div73 div.scale-div ul li.td a.rate-off',
            'q74': 'div#div74 div.scale-div ul li.td a.rate-off',
            'q75': 'div#div75 div.scale-div ul li.td a.rate-off',
            'q76': 'div#div76 div.scale-div ul li.td a.rate-off',
            'q77': 'div#div77 div.scale-div ul li.td a.rate-off',
            'q78': 'div#div78 div.scale-div ul li.td a.rate-off',
            'q79': 'div#div79 div.scale-div ul li.td a.rate-off',
            'q80': 'div#div80 div.scale-div ul li.td a.rate-off',
            'q81': 'div#div81 div.scale-div ul li.td a.rate-off',
            'q82': 'div#div82 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_6_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div88')))

        # Define the final page's questions and their option selectors
        page_7_questions = {
            'q88': 'div#div88 div.scale-div ul li.td a.rate-off',
            'q89': 'div#div89 div.scale-div ul li.td a.rate-off',
            'q90': 'div#div90 div.scale-div ul li.td a.rate-off',
            'q91': 'div#div91 div.scale-div ul li.td a.rate-off',
            'q92': 'div#div92 div.scale-div ul li.td a.rate-off',
            'q93': 'div#div93 div.scale-div ul li.td a.rate-off',
            'q94': 'div#div94 div.scale-div ul li.td a.rate-off',
            'q95': 'div#div95 div.scale-div ul li.td a.rate-off',
            'q96': 'div#div96 div.scale-div ul li.td a.rate-off',
            'q97': 'div#div97 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_7_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div99')))

        # Define the final page's questions and their option selectors
        page_8_questions = {
            'q99': 'div#div99 div.scale-div ul li.td a.rate-off',
            'q100': 'div#div100 div.scale-div ul li.td a.rate-off',
            'q101': 'div#div101 div.scale-div ul li.td a.rate-off',
            'q102': 'div#div102 div.scale-div ul li.td a.rate-off',
            'q103': 'div#div103 div.scale-div ul li.td a.rate-off',
            'q104': 'div#div104 div.scale-div ul li.td a.rate-off',
            'q105': 'div#div105 div.scale-div ul li.td a.rate-off',
            'q106': 'div#div106 div.scale-div ul li.td a.rate-off',
            'q107': 'div#div107 div.scale-div ul li.td a.rate-off',
            'q108': 'div#div108 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_8_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Next Page" button again to move to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#divNext a.button')))
        next_button.click()

        # Wait for the next page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#div112')))

        # Define the final page's questions and their option selectors
        page_9_questions = {
            'q112': 'div#div112 div.scale-div ul li.td a.rate-off',
            'q113': 'div#div113 div.scale-div ul li.td a.rate-off',
            'q114': 'div#div114 div.scale-div ul li.td a.rate-off',
            'q115': 'div#div115 div.scale-div ul li.td a.rate-off',
            'q116': 'div#div116 div.scale-div ul li.td a.rate-off',
            'q117': 'div#div117 div.scale-div ul li.td a.rate-off',
            'q118': 'div#div118 div.scale-div ul li.td a.rate-off',
            'q119': 'div#div119 div.scale-div ul li.td a.rate-off',
            'q120': 'div#div120 div.scale-div ul li.td a.rate-off',
            'q121': 'div#div121 div.scale-div ul li.td a.rate-off',
            'q122': 'div#div122 div.scale-div ul li.td a.rate-off',
            'q123': 'div#div123 div.scale-div ul li.td a.rate-off',
            'q124': 'div#div124 div.scale-div ul li.td a.rate-off',
            'q125': 'div#div125 div.scale-div ul li.td a.rate-off',
            'q126': 'div#div126 div.scale-div ul li.td a.rate-off',
        }

        # Iterate through each final page question
        for q, selector in page_9_questions.items():
            try:
                # Find all options for the current question on the final page
                options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                
                if options:
                    # Randomly select one of the options
                    random_option = random.choice(options)
                    
                    # Click on the selected option
                    wait.until(EC.element_to_be_clickable(random_option)).click()
            except Exception as e:
                print(f"Error processing final page question {q}: {e}")

        # Click the "Submit" button
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'ctlNext')))
        submit_button.click()

        # Optional: wait to see the result
        time.sleep(10)

    finally:
        # Close the WebDriver
        driver.quit()