Flappy_api
===========

A small REST API using flask and mongodb, for a small game made by a friend on unity. 

DOC
===

### ['GET'] /flappy_api/getscore/num_score
Return the n highest score in form of json

### ['GET'] /flappy_api/getscore
Return all the scores store in database

### ['POST'] /flappy_api/setscore'
implements player's score & name in database