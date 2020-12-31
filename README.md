
1. activate the venv `source venv/bin/activate`

2. intall the necessary requirements `pip install requirements.txt`

3. run the setup.py `python setup.py develop`
Can optionally use intsall if you don't plan on modifying code

--Running

In order to run the tasks from cli, run `PYTHONPATH=. luigi --module runner.run MainTask --local-scheduler`

Can run by running the run module `python -m src.runner.run`




