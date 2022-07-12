# Job Submission


start a local or remote cluster first
note that .yml conf files can also be used here

```bash
ray start --head
```

set RAY_ADDRESSS
```bash
export RAY_ADDRESS="http://127.0.0.1:8265"
```

next send one of the random scripts to the job q

```bash
ray job submit -- python scripts/1_basic_task.py
```


results:
```
Tailing logs until the job exits (disable with --no-wait):
[0, 1, 4, 9]

------------------------------------------
Job 'raysubmit_x2fyHSirCWNX5mvQ' succeeded
------------------------------------------
```

now we can check job history

```
$ ray job list
Job submission server address: http://127.0.0.1:8265
{'raysubmit_x2fyHSirCWNX5mvQ': JobInfo(status='SUCCEEDED', entrypoint='python scripts/1_basic_task.py', message='Job finished successfully.', error_type=None, start_time=1657626440391, end_time=1657626444434, metadata={}, runtime_env={})}
```


the prometheus dash board is also available at:
http://127.0.0.1:8265/#/