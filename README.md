# Flask-API-template
This is the clear Rest-API grounded on the combination of **Flask** and **MongoDB** with **3** simple outputs. Easy to transform to any real world application.

## Resource Method Chart

| Resource | Address | Protocol | Parameters | Response |
| ---- | ---- | ---- | ---- | ---- |
| Register User | <code>/register</code> | POST | <ul><li><code>username</code></li><li><code>password</code></li></ul> | <ul><li><code>200</code> - OK</li></ul> |
| Store Sentence | <code>/store</code> | POST | <ul><li><code>username</code></li><li><code>password</code></li><li><code>sentence</code></li></ul> | <ul><li><code>200</code> - OK</li><li><code>301</code> - Out of Tokens</li><li><code>302</code> - Invalid Password</li></ul> |
| Retrieve Sentence | <code>/get</code> | POST | <ul><li><code>username</code></li><li><code>password</code></li></ul> | <ul><li><code>200</code> - OK</li><li><code>301</code> - Out of Tokens</li><li><code>302</code> - Invalid Password</li></ul> |

## Before launch the API

Before launch the Rest-API I reccomend to check if Docker is installed correctly on your machine and install both *bcrypt* Python module and *MongoDB client* (*pymongo*).

> **Check if Docker is installed correctly**<br>
> <code>docker-compose -version</code>

> **Install bcrypt Python module**<br>
> <code>pip install bcrypt</code>

> **Install PyMongo Client**<br>
> <code>pip install pymongo</code>

## Run the API

Open Terminal and run the following commands sequentelly:

<ul><li><code>docker-compose build</code></li><li><code>docker-compose up</code></li></ul>

*Notes*:
> - The Terminal commands has been tested on *Mac Catalina*.
> - *Docker* (v. 17.03.1-ce-rc1-mac3) has been used for testing the repo.
> - *MongoDB* must be installed before testing (see commands above).

Vytautas.
