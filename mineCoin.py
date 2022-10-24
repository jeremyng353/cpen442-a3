import hashlib as hash
import time
import base64 as b64
#import requests
#import json

hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
id_of_miner = "Laughing Seagulls"

coin_blob = ""

count = 0

#source: https://docs.python.org/3/library/hashlib.html for hashlib
hashed = hash.sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id_of_miner).encode('utf-8'))

checker = "0000"

start = time.time()
while True:
    #convert coin_blob integer(number) to string
    coin_blob = str(count)
    
    #generate the hash using SHA256
    hashed = hash.sha256(("CPEN 442 Coin" + "2022" + hash_of_preceding_coin + coin_blob + id_of_miner).encode('utf-8'))
    
    #iterate through numbers for coin_blob
    count += 1

    #check the first few bytes of the hash
    if hashed.hexdigest()[0:len(checker)] == checker:    
        end = time.time()
        
        print(f"Time taken to find valid coin_blob, for a hash that starts with {len(checker)} zeros: {end - start}")
        
        #convert the coin_blob to base64 encoding
        base64 = b64.b64encode(coin_blob.encode("utf-8"))
        print(f"coin_blob found: {base64}")
        
        #look for hashes with more leading zeroes
        checker = checker + "0"
        
        # restart counter and timer for the new checker
        count = 0
        start = time.time()


#check the coin_blob using verify_example_coin api
#def api_call(base64_coin, miner_id):
 #   payload = {"coin_blob": base64_coin, "id_of_miner": miner_id}
  #  # json_object = json.dumps(payload, indent=4) 
   # r = requests.post("http://cpen442coin.ece.ubc.ca/verify_example_coin", data=payload)
    #print(r.text)
