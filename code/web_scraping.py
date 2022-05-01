from selenium import webdriver


def get_states():
    """Start web driver"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    # URL TO SCRAPE
    driver.get("https://covidnow.moh.gov.my/")
    states_list_raw = driver.find_elements_by_xpath(
        "//div[contains(@class, 'mb-0.5')]")
    states_list_raw = [','.join(state.text for state in states_list_raw)]
    states_list_conv = str.split(*states_list_raw, sep=',')

    state_deaths = []
    state_name = []

    for index, state in enumerate(states_list_conv):
        # to format the redundant occurrence of_deaths
        split_lines = state.split(sep='\n')
        state_name.append(split_lines[0])
        state_deaths.append(float(split_lines[1]))

    # Create dict with state_name as key and deaths as value
    states_dict = dict(zip(state_name, state_deaths))

    # Sort in ascending order
    states_dict = dict(
        sorted(states_dict.items(), key=lambda x: x[1], reverse=True))

    # display top three states with highest deaths per million
    i = 0
    processed_states = ''
    end = ', '
    for name, deaths in states_dict.items():
        if i == 2:
            end = '.'
        if i < 3:
            processed_states += name + ' ' + str(deaths) + end

        i += 1

    driver.quit()
    return processed_states
