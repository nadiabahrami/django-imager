# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


def home_page(request, *args, **kwargs):
    # kwargstring = argstring = ""
    # if args:
    #     argstring = "args: {}".format(", ".join(args))
    # if kwargs:
    #     kwargstring = "kwargs:\n{}".format(
    #         "".join(["\t {}: {} \n".format(key, val) for key, val in kwargs.items()])
    #     )
    # body = """
    #         Home page body was called with:
    #         {}
    #         {}
    #         """.format(argstring, kwargstring)
    # return HttpResponse(body)
    #___________________________________________
    # template = loader.get_template('home.html')
    # foo = 'dude'
    # body = template.render({'foo': foo})
    # return HttpResponse(body)
    foo = 'dude'
    return render(request, 'home.html', context={'foo': foo})


class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, id):
        foo = 'garbanzo beans'
        return {'foo': foo}