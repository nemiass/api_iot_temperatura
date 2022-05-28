# Api-temperaturas-iot

### Guía
##### Prerequisitos:
- python versión mayor a ***3.10*** instalado
#### - 1 Crer base de datos
- Base de datos mysql, nombre  de la bd: "**iot_temperatura**"
![alt text](https://github.com/nemiass/api_iot_temperatura/blob/main/imgs/bd.jpg?raw=true)
#### - 2 Instalación de las librerías
```sh
pip install -r requirements.txt
```
#### - 3 Ejecutando
```sh
python run.py
```
![alt text](https://github.com/nemiass/api_iot_temperatura/blob/main/imgs/run.png?raw=true)
### Endpoints de la API
La "ip" puede cambiar, se coloca la ip que sale cuando se hace el paso Nro. ***- 3 Ejecutando***
```sh
http://192.168.4.18:3000/api/temperatura/registrar  | method: POST
http://192.168.4.18:3000/api/temperatura/listar     | method: GET
```
- Ejemplo de registrar en postman
![alt text](https://github.com/nemiass/api_iot_temperatura/blob/main/imgs/ejemplo_registrar.jpg?raw=true)