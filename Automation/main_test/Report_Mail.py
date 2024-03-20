from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from pretty_html_table import build_table
import pandas as pd
from smtplib import SMTP
import logging
import os
import xml.etree.ElementTree as ET

SuccessCount = 0
FailureCount = 0
SkippedCount = 0
Success_List = []
Failure_Cause = []
Execution_time = []
# vdcs bvgv awvb aurx

SENDER_MAIL = 'vikaspatel1203@gmail.com'
SENDER_PWD = 'vdcsbvgvawvbaurx'
Tester = "ketanmangukiya001@gmail.com"
cc = "ketanmangukiya001@gmail.com"
Recipents = cc.split(",") + [Tester]


def fetch():
    path = os.getcwd() + "\\junit.xml"
    tree = ET.parse(path)
    root = tree.getroot()
    test_results = []
    for testcase in root.findall('.//testcase'):
        test_name = testcase.get('name')
        time_taken = testcase.get('time')
        error_message = None
        failure = testcase.find('failure')
        if failure is not None:
            error_message = failure.get('message')
        if error_message:
            test_results.append([test_name, time_taken, error_message])
        else:
            test_results.append([test_name, time_taken, "pass"])
    # return test_results
    print(test_results)


def Success_List_Append(testID, results):
    global SuccessCount, FailureCount
    Success_List.append([testID, results])
    if results == "Pass":
        SuccessCount += 1
        # print(testID)
        logging.info("Success Count = " + str(SuccessCount))

def read_file():
    with open("junit.xml", 'r') as f:
        data = f.read()
    logging.info(data)

def Failure_Cause_Append(testID, failureCause):
    global SuccessCount, FailureCount
    Failure_Cause.append([testID, failureCause])
    FailureCount += 1
    logging.info("Failure Count = " + str(FailureCount))

#
def TestReport_Generation():
    global Test_Report_Table
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://selenium__standalone-chrome:4444/wd/hub',options=options)

    print("Entered into TestReport_Generation()")
    Test_Report = [
        ["Project Name", "PAC"],
        ["Test Type", "Automation"],
        ["Browser Used", "Chrome"],
        ["Browser Version", driver.capabilities["browserVersion"]],
        ["Test Pass", SuccessCount],
        ["Test Fail", FailureCount],
        ["Total Test Cases", int(SuccessCount + FailureCount)],
    ]
    Test_Report_DF = pd.DataFrame(Test_Report, columns=("Summary", "Details"))
    Test_Report_Table = build_table(Test_Report_DF, "blue_dark", text_align="justify")
    driver.quit()
    print("Exiting from TestReport_Generation()")


def Summary_Table_Formation():
    global Summary_Table
    global Failure_Cause_Table
    Summary_table_DF = pd.DataFrame(
        Success_List, columns=["TestCase No.", "TestCases Summary", "Results"]
    )
    Summary_Table = build_table(Summary_table_DF, "green_dark", text_align="justify")
    if FailureCount != 0:
        Failure_Cause_Table_DF = pd.DataFrame(
            Failure_Cause,
            columns=["TestCase No.", "TestCases Summary", "Failure Cause"],
        )
        Failure_Cause_Table = build_table(
            Failure_Cause_Table_DF, "red_dark", text_align="justify"
        )


def Send_Mail():
    print("Sending Mail...........")
    message = MIMEMultipart()
    message["Subject"] = "Demo Results"
    message["From"] = SENDER_MAIL
    message["To"] = Tester
    message["Cc"] = cc
    # style='height: 500px; overflow: auto; width: fit-content'
    if FailureCount != 0:
        empanelled = "<p>Failure Cause Table</p><div>" + Failure_Cause_Table + "</div>"
    else:
        empanelled = "<p>No Failure Observed.</p>"
    html = (
        """\
    	<html>
    	  <head></head>
    	  <body>
    	    <p>Hi,<br>
    	        Please find below Test Report for Automation Testing
    	    </p>
    	    <p>Test Report/Details
    	    </p>
    	    <div>"""
        + Test_Report_Table
        + """
    	    </div>
    	    <p>Summary Table
    	    </p>
    	    <div >"""
        + Summary_Table
        + """
    	    </div>
    	    <p>"""
        + empanelled
        + """</p>
    	    <p>THIS IS SYSTEM GENERATED MAIL.</p>
    	    <p></p>
    	  </body>
    	</html>
    	"""
    )

    part2 = MIMEText(html, "html")
    message.attach(part2)
    filename = os.path.join(os.getcwd(), "pytest.log")
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= Logs")
    message.attach(part)
    msg_body = message.as_string()
    try:
        server = SMTP("smtp.gmail.com", 587)
        # outlook = client.Dispatch("Outlook.Application")
        server.starttls()
        server.login(message["From"], SENDER_PWD)
        server.sendmail(message["From"], Recipents, msg_body)
        server.quit()
        print("Mail Sent successfully")
    except Exception as e_mail:
        print("Mail sending Failed")
        print(e_mail)
