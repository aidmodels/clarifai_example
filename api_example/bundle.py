from pkg_resources import resource_filename
from cvpm.bundle import Bundle
import os

class ApiExampleBundle(Bundle):
    API_KEY = os.environ['CLARIFAI_API_KEY']
    SOLVERS = []