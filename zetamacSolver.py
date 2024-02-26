from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import re
import time

driver = webdriver.Chrome()

# Open Website
driver.get("https://arithmetic.zetamac.com/")

# Start the game
startButton = driver.find_element(By.XPATH, '//input[@value="Start"]')
startButton.click()

while True:
   
    # Get the math problem 
    problemSpan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'problem')))
    problemText = problemSpan.text
    
    # Find the mathematical symbol
    mathSymbols = {'+', '–', '÷','×'}
    symbolIndices = [index for index, char in enumerate(problemText) if char in mathSymbols]

    # Check if any symbols were found
    if symbolIndices:
        sign_index = symbolIndices[0]
        sign = problemText[sign_index] 

        # Do the calculation
        if sign == '–':
            newProblemText = problemText.replace('–', '-')
            answer = eval(newProblemText) 
        elif sign == '+':
            answer = eval(problemText)
        elif sign == '×':
            newProblemText = problemText.replace('×', '*')
            answer = eval(newProblemText)
        elif sign == '÷':
            newProblemText = problemText.replace('÷', '/')
            answer = eval(newProblemText)
    
    # Enter the answer
    answerInput = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'answer')))
    answerInput.send_keys(str(answer))  
    answerInput.send_keys(Keys.RETURN)
    
    # Wait for the new problem to load
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return jQuery.active == 0'))
    time.sleep(100)    