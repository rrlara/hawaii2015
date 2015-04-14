import urllib2
import urllib
import json
import httplib
import unicodedata
import cStringIO

# def remove_accents(input_str):
#     # nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
#     normal = unicodedata.normalize('NFKD', input_str).encode('ASCII', 'ignore')
#     return normal

awsBucket = "travels2013"
awsObservation = "Observations_SEA.json"

url = urllib2.urlopen('https://s3-us-west-2.amazonaws.com/' + awsBucket + '/' + awsObservation)
json_str = url.read()
json_str = json_str.replace("(null),", "").replace("(null)", "")
 
print json_str 

json_str = json_str.replace("(null),", "").replace("(null)", "")
print json_str
data = json.loads(json_str)

for feature in data['features']:

	print feature

	obsID = (feature['properties']['timestamp']).replace("-", "").replace(" ", "").replace(":", "")
	print obsID

	comment = feature['properties']['comment']
	comment = comment.replace(" ", "-").replace(".", "-").replace("/", "-")

	commentPost = feature['properties']['comment']

	timestamp = (feature['properties']['timestamp']).split(' ')[0]

	image = (feature['properties']['timestamp'])

	imageURL = "https://s3-us-west-2.amazonaws.com/" + awsBucket + "/" + str(image) + ".jpg"
	print imageURL

	file = cStringIO.StringIO(urllib.urlopen(imageURL).read()).getvalue()
	# img = Image.open(file)

	
	# print "valide image"
		# print file

	# if imageURL is None:
	# 		print "Image is null", imageURL
	# else:
	# 	print "All images are valid!"

	file_name = timestamp + "-" + comment

	# filename_encode = file_name.encode('utf8')

	lat = feature['geometry']['coordinates'][1]
	lng = feature['geometry']['coordinates'][0]

	


	normal = unicodedata.normalize('NFKD', file_name).encode('ASCII', 'ignore')

	commentPost = unicodedata.normalize('NFKD', commentPost).encode('ASCII', 'ignore')
	print commentPost

	if (file):
	
		# print "This is the file name", normal
		with open("test/" + normal + '.md', 'wb') as out_file:
			out_file.write("---")
			out_file.write("\n")
			out_file.write("layout: default")
			out_file.write("\n")
			out_file.write("caption_header: " + commentPost)
			out_file.write("\n")
			out_file.write("caption: Leapspot")
			out_file.write("\n")
			out_file.write("lat: " + str(lat))
			out_file.write("\n")
			out_file.write("lng: " + str(lng))
			out_file.write("\n")
			out_file.write("date: " + str(timestamp))
			out_file.write("\n")
			out_file.write("photo: " + imageURL)
			out_file.write("\n")
			out_file.write("observation: " + obsID)
			out_file.write("\n")
			out_file.write("---")
