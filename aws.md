# aws cluster usage

create some example code to be executed

```python
# script.py
from collections import Counter
import socket
import time

import ray

# auto is important to connect to remote
ray.init(address='auto')

print('''This cluster consists of
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

@ray.remote
def f():
    time.sleep(0.001)
    # Return IP address.
    return socket.gethostbyname(socket.gethostname())

object_ids = [f.remote() for _ in range(10000)]
ip_addresses = ray.get(object_ids)

print('Tasks executed')
for ip_address, num_tasks in Counter(ip_addresses).items():
    print('    {} tasks on {}'.format(num_tasks, ip_address))
```

a yaml file for minimal cluster configuration
```yaml
# An unique identifier for the head node and workers of this cluster.
cluster_name: minimal

# Cloud-provider specific configuration.
provider:
    type: aws
    region: us-west-2
```

launch a cluster on the cloud
```bash
ray up -y config.yaml
```


submit the task to the cluster
```bash
ray submit config.yaml script.py
```

shutting down the cluster
```
ray down -y config.yaml
```