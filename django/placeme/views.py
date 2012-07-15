from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth import login as base_login
from django.contrib.auth.models import User
from django.contrib.auth.views import logout as base_logout_view
from django.views.decorators.http import require_GET, require_POST
from django.template import RequestContext
from django.template.loader import render_to_string


@require_GET
def search(request):
    ''' returns snippet search results '''
    query_set = Snippet.query(request.GET.get('q'))
    ctx = {
        'next' : request.GET.get('next') or '',
        'snippets' : query_set,
        }
    return render_snippets(request, 'index.jinja', ctx)


@require_GET
def search_json(request):
    ''' returns a JSON response of rendered snippets '''
    # TODO: Add paging.
    query_set = Snippet.query(request.GET.get('q'))
    ctx = snippets_context(request, query_set)
    resp = {'html':render_to_string('_snippets.jinja', ctx)}
    return json_response(resp)


def index(request):
    return render(request, 'index.jinja')

def results(request):
    return render(request, 'results.jinja')

