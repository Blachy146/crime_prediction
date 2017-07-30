import urllib.request

data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/communities/communities.data"

data = urllib.request.urlopen(data_url).read()
data = data.decode('utf-8')
