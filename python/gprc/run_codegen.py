from os import path, getenv
import time

from grpc_tools import protoc
from dotenv import load_dotenv


load_dotenv()

protoFiles = open(file=f'{path.dirname(__file__)}/protos/template.proto')

rawData = protoFiles.read()

newFile = rawData.replace("serviceName", getenv('SERVICE_NAME') )

# protoFiles.flush()

open(f'{path.dirname(__file__)}/protos/service.proto', "w+").write(newFile)

time.sleep(5)

protoc.main((
    '',
    f'-I{path.dirname(__file__)}/protos',
    f'--python_out={path.dirname(__file__)}/py-protos',
    f'--grpc_python_out={path.dirname(__file__)}/py-protos',
    f'{path.dirname(__file__)}/protos/service.proto',
))