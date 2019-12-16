import redis
from datetime import timedelta

r = redis.Redis()

def get_name(request, *args, **kwargs):
  id = request.get('id')
  print("Id: {}".format(id))
  print("r: {}".format(r))
  if id in r: 
    return r.get(id)
  else: 
    name = 'Bob'
    r.setex(id, timedelta(minutes=60), value=name)
    return name

d = {"id": 1, "name": "Guillermo"}
get_name(d, name='Guillermo')

print("Length {}".format(len(list(r.scan_iter("user:*")))))

for key in r.scan_iter(""):
  print(key)