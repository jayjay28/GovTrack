#GovTrack Vote API
#The Class should be able to allow a user to pull whether or not a congress member voted yes or no on a specific bill.
#Get the persons ID#

class GovTrack():
	import pprint
	import urllib2
	import json
	import pprint

	def __init__(self):
		self.a ="Hillary Clinton"
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/person?q=' + self.a.replace(" ","%20"))
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)
		f.close()
		self.congress_members = {}
		for items in self.parsed_json['objects']:
			self.congress_members[items['firstname'] + ' ' + items['lastname'] ] = items['id']	
	
	def get_Member_ID(self):
		return str(self.parsed_json['objects'][0]['id'])

	def get_Bill_ID(self):
		#This queries the GovTrack Database for bills and returns the ID of that specific bills
		a = str(input('Whats the Bill ID: '))
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/bill/' + a)
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)
		f.close()
		print self.parsed_json['title']
		print self.parsed_json['current_status_date']
		return a

	def search_Bill_ID(self):
		#This queries the GovTrack Database for bills and returns the ID of that specific bills
		a = str(raw_input('What bill are you looking for?: '))
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/bill?q=' + self.a.replace(" ","%20")+ '&bill_type=house_bill')
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)["objects"]
		f.close()
		self.counter = 5

		for items in self.parsed_json:
			for items in range(5):
				print items['title'] + '--- Bill ID ---' + str(items['id']) + '--- Introduced Year ---' + str(items['introduced_date'])
				self.counter -= 1
				print self.counter

		#You can filter out whether or non someone was in office of the time of the bill and they weren't in office, you can just not run the program.

	def get_Vote_Voter(self):
		#id number
		try:
			ref_id = str(GovTrack().getMemberID())
			f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/vote_voter?person='+ GovTrack().getMemberID() +'&vote='+GovTrack().getBillID())
			json_string = f.read()
			self.parsed_json = GovTrack.json.loads(json_string)['objects'][0]['option']
			print self.parsed_json
			f.close()

			return self.parsed_json.get('value')
		except IndexError, ValueError:
			print 'Please select someone who is supposed to be voting on this bill.'

	# def getVote(self):
	# 	f = GovTrack.urllib2.urlopen("https://www.govtrack.us/api/v2/vote/" + str((GovTrack().getMemberID())))
	# 	json_string = f.read()
	# 	self.parsed_json = GovTrack.json.loads(json_string)['objects']
	# 	f.close()

	# 	print parsed_json

		
		#billID
#76416
print GovTrack().search_Bill_ID()