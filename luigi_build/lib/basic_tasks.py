
import luigi
import time
import datetime

class BasicWaitTask(luigi.Task):

    dateMin = luigi.DateMinuteParameter()
    waitTime = luigi.IntParameter()
    basePath = luigi.Parameter(significant=False)

    def requires(self):
        return BasicCalculateTask(
            self.dateMin,
            self.waitTime,
            self.basePath
        )

    def output(self):
        return luigi.LocalTarget(f"{self.basePath}/output/wait-{self.waitTime}-{int(self.dateMin.timestamp())}.txt")

    def run(self):

        time.sleep(self.waitTime)

        with self.output().open('w') as f:
            f.write("Completed Wait")


class BasicCalculateTask(luigi.Task):

    dateMin = luigi.DateMinuteParameter()
    waitTime = luigi.IntParameter()
    basePath = luigi.Parameter(significant=False)

    def output(self):
        return luigi.LocalTarget(f"{self.basePath}/output/calc-{self.waitTime}-{int(self.dateMin.timestamp())}.txt")

    def run(self):

        time.sleep(self.waitTime)

        with self.output().open('w') as f:
            f.write(str(float(self.waitTime) ** 2))
