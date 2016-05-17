#! python3
import smtplib,pywapi,datetime,calendar

"""
Format for text to different carriers:
Verizon - @vtext.com
ATT     - @txt.att.net
Sprint  - @messaging.sprintpcs.com
TMobile - @tmomail.net
"""

######## Getting weather info ########

zipCode = '77354'


today = datetime.date.today()
weekday = calendar.day_name[today.weekday()]+''

weather_com_result = pywapi.get_weather_from_weather_com(zipCode, units='imperial')
percentOfPrecip = (weather_com_result['forecasts'][0]['day']['chance_precip'])
location = weather_com_result['location']['name']

message_body = 'Today is '+weekday+'. '
message_body += 'There is a '+percentOfPrecip+ \
                '% chance of rain in '+location+'.'


if int(percentOfPrecip) >= 35:
    message_body += '\nBetter pack an umbrella!'

######### Sending Email #########
TO = open('emailList.txt').readlines()
FROM = 'ryansweatherbot@gmail.com'
SUBJECT = weekday+'\'s chance of rain:'

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, message_body)
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login('ryansweatherbot@gmail.com', 'forecast1')
server.sendmail(FROM, TO, message)
server.quit()

print('Email sent')