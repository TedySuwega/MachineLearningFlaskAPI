import requests

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
InputJson = {
	"hist_current" : 1,
    "hist_xday" : 3,
    "hist_30dpd" : 3,
    "hist_60dpd" : 0,
    "hist_npl" : 4,
    "percentage" : 32.3,
    "all_hist_current" :3,
    "all_hist_xday" : 0,
    "all_hist_30dpd" : 0,
    "all_hist_60dpd" : 9,
    "all_hist_npl" : 9,
    "all_hist_percentage" : 20.45
}

r = requests.post(url,json=InputJson)
print(r.json())