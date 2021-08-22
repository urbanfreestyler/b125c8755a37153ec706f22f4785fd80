from __future__ import absolute_import, unicode_literals

from celery import shared_task
from matplotlib import pyplot as plt
from .py import compute
import datetime
import matplotlib.dates as mdates
import matplotlib
matplotlib.use('Agg')
import io
from django.core.files.images import ImageFile

@shared_task()
def saved_image(graph_id):
    from .models import MyGraph
    import time
    try:
        fun = MyGraph.objects.get(pk=graph_id)
    except MyGraph.DoesNotExist:
        time.sleep(3)
        fun = MyGraph.objects.get(pk=graph_id)

    ax = plt.subplot()
    graph = compute(fun.function_text)
    figure = io.BytesIO() 

    date_1 = datetime.datetime.now()
    date_2 = date_1 + datetime.timedelta(days=fun.interval)
    ax.set_xlim(date_1, date_2)
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    plt.xticks(rotation='45')
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval = fun.dt))
    ax.xaxis.set_major_locator(mdates.DayLocator())

    
    plt.plot(graph)
    plt.savefig(figure, format='png')
    image_file = ImageFile(figure)
    fun.graph.save((str(graph_id)+'.png'), image_file)
    fun.save()