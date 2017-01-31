# README #
Assignment 3


### What is this repository for? ###
Client-side sharding for the expense management application using consistent hashing client.

### Set up steps ###

* use Makefile to build and run the application and mysql containers in docker
* run ch_client.py

### Output ###

Seemas-MacBook-Pro:Assignment3 seemarohilla$ python ch_client.py
Request: 1
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo1@bar.com", "estimated_costs": "700", "id": "1", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 1", "status": "pending", "submit_date": "12-10-2016"}
Request: 2
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo2@bar.com", "estimated_costs": "700", "id": "2", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 2", "status": "pending", "submit_date": "12-10-2016"}
Request: 3
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo3@bar.com", "estimated_costs": "700", "id": "3", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 3", "status": "pending", "submit_date": "12-10-2016"}
Request: 4
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo4@bar.com", "estimated_costs": "700", "id": "4", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 4", "status": "pending", "submit_date": "12-10-2016"}
Request: 5
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo5@bar.com", "estimated_costs": "700", "id": "5", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 5", "status": "pending", "submit_date": "12-10-2016"}
Request: 6
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo6@bar.com", "estimated_costs": "700", "id": "6", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 6", "status": "pending", "submit_date": "12-10-2016"}
Request: 7
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo7@bar.com", "estimated_costs": "700", "id": "7", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 7", "status": "pending", "submit_date": "12-10-2016"}
Request: 8
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo8@bar.com", "estimated_costs": "700", "id": "8", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 8", "status": "pending", "submit_date": "12-10-2016"}
Request: 9
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo9@bar.com", "estimated_costs": "700", "id": "9", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 9", "status": "pending", "submit_date": "12-10-2016"}
Request: 10
{"category": "office supplies", "decision_date": "", "description": "iPad for office use", "email": "foo10@bar.com", "estimated_costs": "700", "id": "10", "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", "name": "Foo 10", "status": "pending", "submit_date": "12-10-2016"}