
import luigi
from luigi_build.lib.basic_tasks import BasicWaitTask
import datetime
import os


class MainTask(luigi.Task):

    dateMin = luigi.DateMinuteParameter(default=datetime.datetime.now())
    basePath = luigi.Parameter(default=os.getcwd())

    def output(self):
        return luigi.LocalTarget(f"{self.basePath}/done.txt")

    def run(self):

        yield [
            BasicWaitTask(self.dateMin, 1, self.basePath),
            BasicWaitTask(self.dateMin, 2, self.basePath),
            BasicWaitTask(self.dateMin, 3, self.basePath),
            BasicWaitTask(self.dateMin, 4, self.basePath),
            BasicWaitTask(self.dateMin, 5, self.basePath),
        ]

        with self.output().open('w') as f:
            f.write("Completed All Tasks")

