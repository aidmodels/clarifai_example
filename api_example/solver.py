from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from cvpm.solver import Solver
from api_example.bundle import ApiExampleBundle as Bundle

class ImageRecognitionSolver(Solver):
    def __init__(self, toml_file=None):
        super().__init__(toml_file)
        self.app = ClarifaiApp(Bundle.API_KEY)
        self.set_bundle(Bundle)
        self.set_ready()
    
    def infer(self, image_file, config):
        image = ClImage(file_obj=open(image_file, 'rb'))
        model = self.app.models.get(config["model"])
        result = model.predict([image])
        return result
        