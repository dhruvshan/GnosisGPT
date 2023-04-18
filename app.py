import os
from decouple import config
from flask import Flask, render_template, request, jsonify
from llama_index import GPTSimpleVectorIndex, download_loader
# import pickle
# import json

# from openai.error import RateLimitError
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow

app = Flask(__name__)
os.environ['OPENAI_API_KEY'] = config('OPENAI_KEY')

# def authorize_gdocs():
#     google_oauth2_scopes = [
#         "https://www.googleapis.com/auth/documents.readonly"
#     ]
#     cred = None
#     if os.path.exists("token.pickle"):
#         with open("token.pickle", 'rb') as token:
#             cred = pickle.load(token)
#     if not cred or not cred.valid:
#         if cred and cred.expired and cred.refresh_token:
#             cred.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", google_oauth2_scopes)
#             cred = flow.run_local_server(port=0)
#         with open("token.pickle", 'wb') as token:
#             pickle.dump(cred, token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt4', methods=['GET', 'POST'])
def ask_gpt():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']

    # authorize_gdocs()
    # initialize LlamaIndex google doc reader 
    # GoogleDocsReader = download_loader('GoogleDocsReader')
    # list of google docs we want to index 
    # gdoc_ids = [
    #     '1ku46TShS33j8-I6-Yp1mnnXC8jEchPSa3AymNQMFQiQ',
    #     '16V_vp4VONvhjgYA1zyI8TKQyywyKu4YfiRMX8fZaCTg',
    #     '1ZDAH7qt0MLZIjUA7MB4dBhsv64V6KSu0MBHMpg9H7xM',
    #     '1dCAjbWkVFKXMrE0VTyIXFqdyDiCr5vNexPHXLLPiUnE',
    #     '1cnOPHaLTrdzy6Rvu0dXg1VBwqkxph6Tx1hggio26DOM',
    #     '13HJhQeh9WAjIBNp76zgt23oSOLBTVeIPlx4nyt0-SAY',
    #     '1fbb9NL0DJLVndUDt_BvSW-KjcUB_-8oDdh_P4iCG9Zs',
    #     '1S7lV-zazbKq5L_Imvb-Sb84xR-nxm3D-qmL35NTtiwY',
    #     '16a30HSlfqauyTOnf0twp2NGroSH8pNVpvnTJ134b59c',
    #     '1gxC0aMLqukr_p7S3ddW_ILc6-mDC7hhg-pMv7NNxdHw', 
    #     '1M4LbgIbpxEWu5uFivebsyZc6y56wDGdJBBIJxS8qNuw']
    # loader = GoogleDocsReader()
    # load gdocs and index them 
    # documents = loader.load_data(document_ids=gdoc_ids)
    # index = GPTSimpleVectorIndex.from_documents(documents)

    # Save your index to a index.json file
    # index.save_to_disk('index.json')
    # # Load the index from your saved index.json file
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

    response = index.query(user_input)
    content = response
    print(content)
    return jsonify(content)

        # Get the last token usage
        # last_token_usage = index.llm_predictor.last_token_usage
        # print(f"last_token_usage={last_token_usage}")


# function to authorize or download latest credentials 
if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run()