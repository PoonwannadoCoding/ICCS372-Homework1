# ICCS372: Homework1

## How to set up the project
First type
```
sudo docker compose up
```
This will setup what you need to run the project and also setup the mysql

Then what you have to do next is run the app.py to run the project

## Tutorial for the project
### ADD NEW MACHINE
```
url: 127.0.0.1/5000/add/machine
```
we will use json form and select POST method
```
{"name": ___, "location":____}
````

## ADD NEW STOCK
```
url: 127.0.0.1/5000/add/stock
```
we will use json form and select POST method
```
{"name":___, "machine_id":___, "items":___}
```

### EDIT MACHINE
```
url: 127.0.0.1/5000/edit/machine
```
we will use json form and select PUT method
```
{"id":___,"name": ___, "location":____}
```

### EDIT STOCK
```
url: 127.0.0.1/5000/edit/stock
```
we will use json form and select PUT method
```
{"id":___,"name":___, "machine_id":___, "items":___}
```

### DELETE MACHINE
```
url: 127.0.0.1/5000/delete/machine
```
we will use json form and select DELETE method
```
{"id":___}
```

### DELETE STOCK
```
url: 127.0.0.1/5000/delete/stock
```
we will use json form and select DELETE method
```
{"id":___}
```

### GET MACHINE INVENTORY
```
url: 127.0.0.1/5000/get/machine/inventory
```
we will use json form and select GET method
```
{"id":___}
```

### GET ALL MACHINE

```
url: 127.0.0.1/5000/get/all/machine/
```
we will select GET method

### GET ALL STOCK

```
url: 127.0.0.1/5000/get/all/stock/
```
we will select GET method

