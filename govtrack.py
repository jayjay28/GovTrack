#GovTrack Vote API
#The Class should be able to allow a user to pull whether or not a congress member voted yes or no on a specific bill.
#Get the persons ID#

class GovTrack():
	import pprint
	import urllib2
	import json

	def __init__(self):
		a = "Barry Goldwater"
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/person?q=' + a.replace(" ","%20"))
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)
		f.close()

		self.congress_members = {}
		for items in self.parsed_json['objects']:
			self.congress_members[items['firstname'] + ' ' + items['lastname'] ] = items['id']
	
	def getMemberID(self):
		return self.parsed_json['objects'][0]['bioguideid']

	def getBillID(self):
		#This queries the GovTrack Database for bills and returns the ID of that specific bills

		a = "A resolution electing officers of the House of Representatives"
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/bill?q=' + a.replace(" ","%20"))
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)
		f.close()
		return self.parsed_json['objects'][0]["id"]

		#You can filter out whether or non someone was in office of the time of the bill and they weren't in office, you can just not run the program.

	def getVote_Voter(self):
		#id number
		ref_id = str(GovTrack().getMemberID())
		f = GovTrack.urllib2.urlopen('https://www.govtrack.us/api/v2/vote_voter/'+ ref_id)
		json_string = f.read()
		self.parsed_json = GovTrack.json.loads(json_string)['objects'][0]['option']
		f.close()

		return self.parsed_json.get('value')
		#billID
		billID = str(GovTrack().getBillID())



print GovTrack().getVote_Voter()