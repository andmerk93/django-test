from django.shortcuts import render
from rest_framework.schemas.openapi import SchemaGenerator


def schema(request):
    title = 'Django Test Site'
    generator = SchemaGenerator(title=title)
    getted_schema = generator.get_schema() or {
        'info': {'title': title}, 'paths': {}
    }
    schema = {
        'title': getted_schema['info']['title'],
        'endpoints': []
    }
    for path in getted_schema['paths']:
        for method in getted_schema['paths'][path].keys():
            schema['endpoints'].append({'path': path, 'method': method})

    return render(request, 'index.html', {'schema': schema})
