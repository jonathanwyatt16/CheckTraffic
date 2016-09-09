import sys
import json
import urllib.request

#Base URL for Google Maps Distance Matrix API
st_base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

#Parameters for HTTP get request
st_api_key = 'XXX'
st_units = 'imperial'
st_traffic_model = 'best_guess'
st_departure_time = 'now'
st_origin = ''
st_destination = ''

n_arg = 0
for arg in sys.argv:
    if n_arg == 1:
        st_origin = str(arg).replace(' ', '+')

    elif n_arg == 2:
        st_destination = str(arg).replace(' ', '+')

    n_arg += 1

d_params = {'key' : st_api_key, 'units' : st_units, 'traffic_model' : st_traffic_model,
            'departure_time' : st_departure_time, 'origins' : st_origin, 'destinations' : st_destination}

st_request = st_base_url;
for key, value in d_params.items():
    st_request += '&' + key + '=' + value

st_response = urllib.request.urlopen(st_request).read().decode('UTF-8')
d_response = json.loads(st_response)
d_elements = d_response['rows'][0]['elements'][0]

print('Origin: ' +str(d_response['origin_addresses'][0]));
print('Destination: ' + str(d_response['destination_addresses'][0]));
print('Distance: ' + str(d_elements['distance']['text']))
print('Estimated time: ' + str(d_elements['duration_in_traffic']['text']))
