
1. activate the venv `source venv/bin/activate`

2. intall the necessary requirements `pip install -r requirements.txt`

3. run the setup.py `python setup.py develop`
Can optionally use intsall if you don't plan on modifying code

--Running

In order to run the tasks from cli, run `PYTHONPATH=. luigi --module luigi_build.lib.main MainTask --local-scheduler --workers 4 --parallel-scheduling`

Can run by running the run module `python -m luigi_build.runner.run`

--Watching

Can watch output with `watch -n .5 'ps aux | grep luigi`



