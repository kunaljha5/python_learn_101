#!/bin/python3
import json,requests,os,sys,logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def get_git_branch():
    command="cd .. ; git rev-parse --abbrev-ref HEAD;"
    try:
        branch_names = os.popen(command).read().strip().split('/')
        branchType = branch_names[0]
        if branchType == "master" or branchType == "develop":
            branchIdentifier = branchType
            logger.info(branchIdentifier)
        else:
            branchIdentifier = branch_names[1]
            logger.info(branchIdentifier)
    except IndexError:
        branchIdentifier = "NOT-FOUND"
        logger.error(branchIdentifier)
    return branchIdentifier


def sonar_get_componentId(project_key):
    sonar_project_url = sonar_url + '/api/navigation/component?component=' + project_key
    sonar_response  = requests.get(sonar_project_url, auth=(sonarusername, sonarpassword))
    sonar_response.status_code == 200 or  logger.error("URL Request failed")
    jp2 = json.loads(sonar_response.text)
    logger.info(sonar_project_url)
    logger.info(jp2)
    try:
        if jp2['id']:
            returnValue = str(jp2['id'])
            return returnValue
    except KeyError:
        returnValue = "PROJECT NOT FOUND"
        logger.error(returnValue)
        return returnValue


def sonar_verify_last_analysis(componentId):
    sonar_project_analysis_url = sonar_url + '/api/ce/activity_status?componentId=' + componentId
    sonar_response = requests.get(sonar_project_analysis_url, auth=(sonarusername, sonarpassword))
    sonar_response.status_code == 200 or logger.error("URL Request failed")
    jp2 = json.loads(sonar_response.text)
    logger.info(sonar_project_analysis_url)
    logger.info(jp2)
    try:
        if jp2["pending"] > 0:
            logger.info("Analysis Pending on Sonarqube")
            return False
        elif jp2["failing"] > 0:
            logger.info("Analysis Failing on Sonarqube")
            return False
        elif jp2 ["inProgress"] > 0:
            logger.info("Analysis inProgress on Sonarqube")
            return False
        else:
            logger.info("Analysis Completed on Sonarqube")
            return True
    except:
        logger.error("Analysis Unable to fetch from Sonarqube")
        return True


def sonar_newly_add_parameter(project_key, s_branch):
    single_project_para_url = sonar_url + '/api/measures/component?branch=' + s_branch + \
                              '&component='+ project_key +'&metricKeys=coverage'
    rs = requests.get(single_project_para_url, auth=(sonarusername, sonarpassword))
    rs.status_code == 200
    jp2 = json.loads(rs.text)
    logger.info(single_project_para_url)
    logger.info("Fetching " + s_branch + " Branch Code Coverage")
    try:
        if len(jp2['component']['measures']) > 0:
            returnValue = float(jp2['component']['measures'][0]['value'])
        else:
            returnValue = 0
        return returnValue
    except KeyError:
        logger.error(jp2)
        single_project_para_url = sonar_url + '/api/measures/component?component=' + project_key + '&metricKeys=coverage'
        rs = requests.get(single_project_para_url, auth=(sonarusername, sonarpassword))
        rs.status_code == 200
        jp2 = json.loads(rs.text)
        logger.info(single_project_para_url)
        logger.info("Fetching master Branch Code Coverage")
        try:
            if len(jp2['component']['measures']) > 0:
                returnValue = float(jp2['component']['measures'][0]['value'])
            else:
                returnValue = 0
            return returnValue
        except KeyError:
            logger.error(jp2)
            return 0


def check_analysis():
    exit_statement = sonar_verify_last_analysis(componentId)
    while True:
        exit_statement = sonar_verify_last_analysis(componentId)
        if exit_statement is True:
            break
        os.system("sleep 30")


def coverage_checker():
    current_coverage = sonar_newly_add_parameter(project_key, s_branch)
    if current_coverage > 70 or current_coverage > default_coverage:
        print("+---------------------------------------------------------------------------------+\n| \
        \t \tQuality Gate \n|\t CodeCoverage : Passed [" + str(current_coverage) + \
              "]\n+---------------------------------------------------------------------------------+")
    else:
        print("+---------------------------------------------------------------------------------+\n|\
        \t \tQuality Gate \n|\t CodeCoverage : Failed [" + str(current_coverage) + \
              "]\n+---------------------------------------------------------------------------------+")


#  Setting Variables For Script Execution

sonarpassword = os.environ['myci_sonarPassword']
sonarusername = "devops"
sonar_url = 'http://localhost:9000'
project_key = sys.argv[1]
if len(sys.argv) > 2:
    default_coverage = int(sys.argv[2])
else:
    default_coverage = 70

s_branch = get_git_branch()


# Fetch the Component ID of the project provided in argument 1
componentId = sonar_get_componentId(project_key)

# Verify the last analysis status if it is in pending or in-progress
#
check_analysis()


# Verify the last analysis status is above 70%
#
coverage_checker()
