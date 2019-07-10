import re 

movie = 'The Force Awakens: Episode 9'


re.sub('[0-9]', '_', movie)

isForce = re.search("Force", movie)

re.split(':', movie)[1].lstrip().rstrip()