apiuser="tester"
apipwd="tester"
apiauthbase="dGVzdGVyOnRlc3Rlcg=="
apiport = 8000
# apiauthbase is generated by:
#encoded = base64.b64encode((apiuser+':'+apipwd).encode('ascii')).decode('ascii')
# enable 'apikey' endpoint of get_apikey(), and call: curl http://localhost:444/apikey

apiport = 8000
apihostip = '0.0.0.0'

# come from client tools
apicallerid ="fastapiuserA"

# in minutes
healthcheck_interval = 3