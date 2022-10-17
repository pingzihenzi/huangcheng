import yaml
import os
import sys

config_url = r'./test-selenium/config/test.yaml'

currentPath1 = os.path.abspath('.')
currentPath2 = os.path.dirname(sys.path[0])
print(currentPath2)
# os.chdir(currentPath2)
print(os.getcwd())

with open(config_url,'r',encoding='utf-8') as file:
    cfg = file.read()
    yaml.warnings({'YAMLLoadWarning':False})
    d = yaml.safe_load_all(cfg)
    print(type(d))
    for i in d:
        for k,v in i.items():
            print(k,v)
    file.close()

