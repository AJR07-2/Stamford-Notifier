import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate('notifier/ServiceAccountKey.json')

default_app = firebase_admin.initialize_app(cred)
dataBase = firestore.client()

doc_ref = dataBase.collection(u'sampleData').document(u'lol')
doc_ref.set({
    u'quote': 100,
    u'lol': 'meh',
})
