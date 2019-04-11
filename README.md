# Master Mind REST API GAME

Master Mind REST API GAME is a game based on real board game MasterMind Codemaker.

### Prerequisites

 1- [Python 2.7](https://www.python.org/) 
 
 2- [Flask '1.0.2'](http://flask.pocoo.org/) - Flask is a microframework for Python 
 

#Deploy and run

1-Clone repository\
2-Install software required\
3- run on your terminal 
```
python  ServiceMasterMind.py  
```
4- Make request from your navigator or a request software like [Postman](https://www.getpostman.com/)


#Play!

####Instructions to play:
 
 ``
 Make requests on: http:/127.0.0.1:5000/MasterMind or http://localhost:5000/MasterMind
 ``
 
 
####Create new game

Make a POST request 
```
POST http://localhost:5000/MasterMind  
```


#### Make a attempt to discover de code

Make a PUT request 
```
http://localhost:5000/MasterMind?id=id_game&move="green"&move="yellow"&move="violet"&move="blue"
```

#### Recover your unfinished game
Make a GET request 
```
http://localhost:5000/MasterMind?id=your_id
```


## Authors

* *[Nacho Lopez](https://github.com/NachoLR/MasterMind)*  



