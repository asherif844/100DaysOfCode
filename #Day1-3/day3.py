import csv
from datetime import date, datetime, timedelta

from azure.storage.blob import BlockBlobService

# print(date.today(), datetime.today())

csvDate = datetime.today()

folder = '/Users/asherif844/p_v_e/100DaysOfCode/#Day1-3/'
filename = folder+'trigger.csv'

with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow([csvDate])

# with open(filename, 'r') as fread:
#     reader = csv.reader(fread)
#     for row in reader:
#         print(row)

accountName = "blobv2dataengineering"
accountKey = "n95TV+PwtS7OhRd+R1N8KHXyPK5AvkfM/MjE8WTM8AMC2erbO6GLHGY8UZGatOT5/dia0Yv6sQkGI5CVexcOrg=="
containerName = "trigger"
blobName = "trigger.csv"

blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

# blobService.create_blob_from_text(containerName,  'trigger2.csv', accountName)
blobService.create_blob_from_path(containerName, 'trigger_from_path.csv', filename)