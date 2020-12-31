
import luigi
import importlib
from luigi_build.lib.main import MainTask

if __name__ == "__main__":

    module = "luigi_build.lib.main"
    luigi_class = "MainTask"

    mod = importlib.import_module(module)
    runTask = getattr(mod, luigi_class)

    print("Running from python code!!!")
    luigi.build(
        [runTask()], 
        workers=4, 
        local_scheduler=True,
        parallel_scheduling=True
    )