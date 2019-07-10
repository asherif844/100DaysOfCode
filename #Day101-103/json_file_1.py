import json 
import numpy as np 

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open('#Day101-103/data_file.json','w') as write_file:
    json.dump(data, write_file)


json_string = json.dumps(data, indent=4)

blackjack_hand = (8,"Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)