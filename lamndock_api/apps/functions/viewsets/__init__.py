import os

from tempfile import NamedTemporaryFile, mkdtemp

from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from functions.models import Function, FunctionVersion
from functions.serializers import FunctionSerializer, FunctionVersionSerializer

from docker import Client


class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer


class FunctionVersionViewSet(viewsets.ModelViewSet):
    queryset = FunctionVersion.objects.all()
    serializer_class = FunctionVersionSerializer

    @detail_route(methods=['put'])
    def execute(self, request, pk=None):
        function_version = self.get_object()

        # TODO: schedule the function to run on a suitable node based on the desired computing power
        # TODO: Make sure images are pulled when stacks are defined.

        cli = Client(base_url='unix://var/run/docker.sock')

        # temp_dir = mkdtemp()
        temp_dir = '/Users/gyoanis/tmp'

        runner_file = open(os.path.join(temp_dir, 'runner.py'), 'w')
        function_file = open(os.path.join(temp_dir, 'function.py'), 'w')

        runner_content = """
try:
    module = __import__('function')
    module.handler({})
except Exception, e:
    print e
"""

        runner_file.write(runner_content)
        runner_file.close()

        function_file.write(function_version.body)
        function_file.close()

        bindings = {
            temp_dir: {
                'bind': '/tmp/python',
                'mode': 'ro'
            }
        }

        # TODO: Launch container on background
        container = cli.create_container(image=function_version.function.stack.docker_image,
                                         host_config=cli.create_host_config(binds=bindings),
                                         working_dir='/tmp/python',
                                         command='python runner.py'.format(temp_dir))
        cli.start(container=container.get('Id'))

        return Response(status=status.HTTP_202_ACCEPTED, data=[])
