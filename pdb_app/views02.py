from django.http import HttpResponse
from django.template import loader

from pdb_app.models import Item  # Load the Model


def index(request):
    """
    Home Page of your website
    :param request:
    :return:
    """
    # return HttpResponse("<h1>Programming Database</h1>")  #way #1 to display html
    # +++++++++++++++++++++++++++
    template = loader.get_template("index.html")  # way #2 to display html
    context = {'java': Item.objects.get(id=2)}  # data to send into the index.html file ie. the template. We sending the "object" to html.
    return HttpResponse(template.render(context, request))
