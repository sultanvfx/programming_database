from django.http import HttpResponse
from django.template import loader


def index(request):
    """
    Home Page of your website
    :param request:
    :return:
    """
    # return HttpResponse("<h1>Programming Database</h1>")  #way #1 to display html
    # +++++++++++++++++++++++++++
    template = loader.get_template("index.html")  # way #2 to display html
    context = {'message': 'Welcome .. welcome'}  # data to send into the index.html file ie. the template
    return HttpResponse(template.render(context, request))
