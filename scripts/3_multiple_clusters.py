import ray
# Create a default client.
ray.init("ray://<head_node_host_cluster>:10001")

# Connect to other clusters.
cli1 = ray.init("ray://<head_node_host_cluster_1>:10001", allow_multiple=True)
cli2 = ray.init("ray://<head_node_host_cluster_2>:10001", allow_multiple=True)

# Data is put into the default cluster.
obj = ray.put("obj")

with cli1:
    obj1 = ray.put("obj1")

with cli2:
    obj2 = ray.put("obj2")

with cli1:
    assert ray.get(obj1) == "obj1"
    try:
        ray.get(obj2)  # Cross-cluster ops not allowed.
    except:
        print("Failed to get object which doesn't belong to this cluster")

with cli2:
    assert ray.get(obj2) == "obj2"
    try:
        ray.get(obj1)  # Cross-cluster ops not allowed.
    except:
        print("Failed to get object which doesn't belong to this cluster")
assert "obj" == ray.get(obj)
cli1.disconnect()
cli2.disconnect()
