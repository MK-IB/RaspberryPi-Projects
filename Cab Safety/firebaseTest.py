import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate('G:/ServiceAccountKey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
response = getQuote()
quote = response.body['quote']
author = response.body['author']

doc_ref = db.collection(u'sampleData').document(u'inspiration')
doc_ref.self ({
  u'quote' : quote,
  u'author' : author,
  })
print(quote+ " and "+author+" successfully written to the database")
