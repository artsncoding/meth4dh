import re

yearRe = re.compile('[0-9][0-9][0-9][0-9]')
def extractYears(date):
    years = yearRe.search(date)

    if years:
        year = years.group(0)
    else:
        year = 0
    return year
