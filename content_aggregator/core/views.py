from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect

from aggregator.models import aggregation
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from aggregator.models import aggregation
from aggregator.tasks import scrape_url  # import your extraction task

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


def aggregation_list_view(request):
    aggregations = aggregation.objects.all()
    return render(request, 'aggregation_list.html', {'aggregations': aggregations})

def aggregation_detail_view(request, pk):
    aggregation = get_object_or_404(aggregation, pk=pk)
    return render(request, 'aggregation_detail.html', {'aggregation': aggregation, 'url': 'https://blog.georg-nikola.com/'})

def error_404(request, pk):
    if not aggregation.objects.filter(pk=pk).exists():
        raise Http404("aggregation does not exist")

def home_view(request):
    context = {
        "title": "Content Aggregator",
    }
    return render(request, "index.html", context)




from aggregator.tasks import scrape_url  # import your extraction task

@csrf_exempt
def extract(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        result = scrape_url.delay(url)  # start the extraction task

        # Wait for the task to complete and retrieve the result
        while not result.ready():
            pass
        title, summary = result.get()

        # Save the scraped data to the database
        agg = aggregation(title=title, summary=summary, url=url)
        agg.save()

        # Return the scraped data as a JSON response
        data = {'title': title, 'summary': summary, 'url': url}
        return JsonResponse(data)

    # handle other request methods if necessary...