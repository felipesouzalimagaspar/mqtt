![GitHub](https://img.shields.io/github/license/felipesouzalimagaspar/ciesta-project?label=license&style=for-the-badge)
![IDE](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/downloads/)
[![Mosquitto](https://img.shields.io/badge/Mosquitto-2.0.12-blue)](https://mosquitto.org/)



# Sketches for mosquito tests using python

## Running mosquito
```unix
mosquitto -v -p 1883
```
## Running redis
```unix
service redis-server start
```

## running sub
```unix
python3 sketches/example/pub.py pub1 localhost topic1 message
```

## running pub
```unix
python3 sketches/example/sub.py sub1 localhost topic1
```
