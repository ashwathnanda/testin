from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
from flashtext import KeywordProcessor


app = Flask(__name__)
api = Api(app)

key_processor = KeywordProcessor()
data = pd.read_csv('dataset/data_tag.csv')
l = list(data['Tag'])
my_list2 = []
for i in range(len(l)):
	m = l[i]
	my_list2.extend(m.split(','))
	
#adding the tags onto the processor
key_processor.add_keywords_from_list(my_list2)

class Fetch_code(Resource):
   def get(self, name):
      name.lower()
      ans = key_processor.extract_keywords(name)
      ans.sort()
      ans = ','.join(ans)
      for i in range(len(l)):
         if(ans == l[i]):
            return data['Snippet'][i], 200
      return 'requirement not found' , 404
      

api.add_resource(Fetch_code, "/fetch/<string:name>")
app.run(debug=True, port = 8080 , host = '0.0.0.0')