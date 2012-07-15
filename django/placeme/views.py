import os, oauth2, urllib, urllib2, json
from django.shortcuts import render 
from django.views.decorators.http import require_GET
from django.utils import simplejson
from django.http import HttpResponse

CONSUMER_KEY = "KthO8dNdeYTgBFnBlIIdHA" 
CONSUMER_SECRET = "Tm8COLLLfk2U5_YQmBEpSZtN6p4" 
TOKEN = "wQqdIJKCWDFNTSunGYjsoC-ebF3qy7lo" 
TOKEN_SECRET = "IXMeyVMwlKawX9yNJxCBXS-Zo4Y"

def yelp_request(url_params, host='api.yelp.com', path='/v2/search'):
  """Returns response for API request."""
  # Unsigned URL
  encoded_params = ''
  if url_params:
    encoded_params = urllib.urlencode(url_params)
  url = 'http://%s%s?%s' % (host, path, encoded_params)

  # Sign the URL
  consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': TOKEN,
                        'oauth_consumer_key': CONSUMER_KEY})

  token = oauth2.Token(TOKEN, TOKEN_SECRET)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()

  # Connect
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return json.dumps(response, sort_keys=True, indent=2)

def json_response(data):
    ''' 
    Turns a data dict into a json response
    '''
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')


@require_GET
def query(request):
    location = request.GET.get('location', '')
    term = request.GET.get('term', '')
    cache_name = '{0}-{1}.json'.format(
        location.replace(' ', '_').replace(',', '_'),
        term.replace(' ', '_').replace(',', '_')
    )

    json_cache = os.path.join(os.getcwd(), 'json_cache', cache_name)
    print 'finding {0}'.format(json_cache)
    json_resp = ''
    if (os.path.exists(json_cache)):
        json_resp = open(json_cache, 'r').read()
    #else:
        #json_resp = yelp_request({'term': term, 'location': location})
        #out_cache = open(json_cache, 'w')
        #out_cache.write(json_resp)
    #    out_cache.close()

    return HttpResponse(json_resp, mimetype='application/json')

def index(request):
    return render(request, 'index.jinja')

