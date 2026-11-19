
# Task 1 - Using httpx

We will use a simple source of web data: [HTTPbin](https://httpbin.io/json)

This provides synthetic data and a REST API, with no authentication, for testing code.

## Create a virtual environment

See slide on `Installing httpx CLI`

## Instal httpx

`pip install 'httpx[cli]'`

## Command-line use

We can fetch data for a single post from the API with

`httpx https://httpbin.io/json​`

Note the reply and identify:
- HTTP status code : 200 OK

- HTTP header : 
    HTTP/1.1 200 OK
    Access-Control-Allow-Credentials: true
    Access-Control-Allow-Origin: *
    Content-Type: application/json; charset=utf-8
    Date: Wed, 18 Nov 2026 15:50:46 GMT
    Content-Length: 421

- Data (this format is called JSON, we will discuss it next)
 _Note: slideshow is the main JSON object_
    Author: Yours Truly
    Date: Date of publication
    Slide title: Sample Slide Show
    Two slides with their respective titles and content


## Other response codes

What is the difference if we request content that does not exist?

`httpx https://httpbin.io/jsoon​`

- Shows status code "404 Not Found" and an error message
