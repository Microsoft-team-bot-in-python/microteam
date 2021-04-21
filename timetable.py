import selenium
from selenium import webdriver
import time

driver=webdriver.chrome(executable_path="PATH OF CHROME WEBDRIVER")

def DSAPMP():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def DSAPMP2():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def SNTKBK():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def SNTKBK2():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def DSAART():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def DSAART2():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)



def DBMSRKK():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def DBMSRKK2():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def COMPDS():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def SNTMHC():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def DBMSRKKLAB():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def DBMSNHB():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def WENSPLAB():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def DSAPMPLAB():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def COMRJNLAB():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def SGPBHP():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)

def HS():
    driver.get("CHANNEL LINK")
    time.sleep(5)
    driver.find_element_by_id("openTeamsClientInBrowser").click()
    time.sleep(10)

    print("PRASOON BOT: Looking for the join button")
    c = 0
    while c <= 1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn = driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn == None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break

    time.sleep(5)

    print("Turning off the webcamera....")
    driver.find_element_by_class_name("ts-toggle-button-container").click()
    time.sleep(2)

    print("Turning off mic ....")
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    time.sleep(2)

    print("Clicling the official joining meeting button.......")
    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
    joinnowbtn.click()
    time.sleep(2)

    print("we join the meeting sccuesfully........")
    time.sleep(5)

    m = 0
    while m <= 1:
        if time.strftime('%H:%M') == 'LECTURE ENDING TIME':
            driver.find_element_by_id("hangup-button").click()
            print("PRASOON BOT left the class")
            break
        else:
            continue

    time.sleep(5)


def Monday():
    while(True):
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            DSAPMP()
            continue
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            SNTKBK()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DSAART()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DBMSRKK()
            break
        else:
            continue
    print("END OF THE DAY........................")

def Tuesday():
    while(True):
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            COMPDS()
            continue
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            SNTMHC()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DBMSRKKLAB()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DBMSNHB()
            break
        else:
            continue
    print("END OF THE DAY........................")


def Weadnesday():
    while(True):
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            COMPDS()
            continue
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            SNTMHC()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            WENSPLAB()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DSAPMPLAB()
            break
        else:
            continue
    print("END OF THE DAY........................")

def Thursday():
    while(True):
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            COMPDS()
            continue
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            SNTKBK2()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            COMRJNLAB()
            continue
        if (time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DSAART2()
            break
        else:
            continue
    print("END OF THE DAY........................")


def Friday():
    while(True):
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            COMPDS()
            continue
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            DBMSRKK2()
            continue
        if(time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            SGPBHP()
            continue
        if(time.strftime("%H:%M") == "LECTURE STARTING TIME"):
            DBMSNHB()
            continue
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            DSAPMP2()
            break
        else:
            continue
    print("END OF THE DAY........................")

def Saturday():
    while(True):
        if(time.strftime("%H:%M")=="LECTURE STARTING TIME"):
            HS()
            break
        else:
            continue

    print("END OF THE DAY........................")

