#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class JaneDoe:

	'''
	Fake Person Generator:
	Source: https://www.fakepersongenerator.com/random-los-angeles-address-generator
	'''

	FIRST_NAME = 'Jane'
	LAST_NAME = 'Doe'
	ADDRESS = '3227 Libby Street'
	CITY = 'Los Angeles'
	STATE = 'California'
	ZIP_CODE = '90017'
	PHONE = '310-238-1380'

	USERNAME = 'janedoe'
	PASSWORD = USERNAME + ZIP_CODE

	'''
	NATIONAL ID (Social Security Number)
	Audit(s):
		SSNs beginning with 8 or 9 are not valid (e.g., 891-40-8025).
		SSNs with zeros in the fourth and fifth digits are not valid (e.g., 565-00-8035).
		
	Source: http://www.calstate.edu/hrpims/awppm/Fields/NATIONAL_ID_Social_Security_Number_.htm
	
	Social Security Administration (SSA) had never issued these Social Security Numbers:
		123-45-6789
		SSN’s having “000” or "666” as the first three left-most digits
		SSN’s equal to or greater than “773” as the first three left-most digits
		SSN’s having “00” as the fourth and fifth digits
		SSN’s having “0000” as the last four digits
	
	Source: https://primepay.com/blog/valid-social-security-number
	
	Generate Social Security Numbers:
	Source: https://www.ssn-verify.com/generate
	'''
	SSN = '563-04-0995'

	INIT_BALANCE = 5125.00
	MIN_BALANCE = 100.00

