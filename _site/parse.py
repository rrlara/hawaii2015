import json,httplib
import unicodedata
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('GET', '/1/classes/HawaiiTrip/', '', {
       "X-Parse-Application-Id": "f978idlmBlmLY2CnQwovpPtQaFwvALWhDlf6RE53",
       "X-Parse-REST-API-Key": "Q2C42t4493WBJf6X2IAWB9YfvAYKkfuTgEu3OyRC"
     })
result = json.loads(connection.getresponse().read())
# print result

for feature in result['results']:

	# print feature
	comment = feature['comment']
	# print comment
	createdAt = feature['createdAt']

	# obsID = (createdAt).replace("-", "").replace(" ", "").replace(":", "")
	timestamp = (createdAt).split('T')[0]

	thumbnail = feature['thumbnail']['url']

	fullImage = feature['imageFile']['url']
	# print thumbnail

	fileName = comment.replace(" ", "-").replace(".", "-").replace("/", "-")

	file_name = timestamp + "-" + fileName

	normal = unicodedata.normalize('NFKD', file_name).encode('ASCII', 'ignore')

	# print timestamp

	if (file):
	
		# print "This is the file name", normal
		with open("_posts/" + normal + '.md', 'wb') as out_file:
			out_file.write("---")
			out_file.write("\n")
			out_file.write("layout: default")
			out_file.write("\n")
			out_file.write("caption_header: " + comment)
			out_file.write("\n")
			out_file.write("caption: Leapspot")
			out_file.write("\n")
			# out_file.write("lat: " + str(lat))
			# out_file.write("\n")
			# out_file.write("lng: " + str(lng))
			# out_file.write("\n")
			out_file.write("date: " + str(createdAt))
			out_file.write("\n")
			out_file.write("photo: " + thumbnail)
			out_file.write("\n")
			# out_file.write("fullImage: " + fullImage)
			# out_file.write("\n")
			out_file.write("---")