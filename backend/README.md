## Loan Calculator Backend

The Loan Calculator API is a small server with a single endpoint that helps in making queries about loan terms.
Based on the parameters sent with the request, the missing terms are being computed. The flows go as follows:

1. Given an interest rate, input the amount and monthly rate to find out the number of payments 
2. Given an interest rate, input the amount and the number of payments to get the montly rate
3. Given an amount, the number of payments and the monthly rate, check whether the interest rate is different from the given one.

The API endpoint can be accessed without authentication for the time being (the assumption is that this should be a calculator accessible to anyone interested). The parameters it accepts are:

```
- amount (int) - the total sum of the loan
- payments (int) - the tenure of the loan measured in number of months
- monthly_rate (float) - the monthly amount of money to pay back
```

### How to run it

To start the server, you need to have `pipenv` installed on your machine. You can easily accomplish this by running the pip install command inside a terminal.

```
$ pip install pipenv
``` 

Then assuming you are inside the `backend` folder, install the project requirements and activate the shell.

```
$ pipenv install

$ pipenv shell
```

The just start up the server by running

```
$ pipenv run python manage.py runserver
```

The server will be accessible at `localhost` on port `8000`. 
After that you can run queries either by using the `curl` command inside a terminal, or a tool such as `Postman`.

```
$ curl http://localhost:8000/?amount=12&payments=2
```

### Questions to ponder

The implementation of this loan calculator is as simple as it gets. There are many things that I would have improved or that could spark an interesting conversation.


- Should we authenticate the user?
- Should we save these queries somewhere? Would we like to analyse this data at some point in the future?
- Would be benefit from using caching? 
- Numpy could prove to be not very memory efficient, should we implement those computations ourselves? Is the risk of having bugs in our calculations worth the advanatge of having everything in house?

This, together with the question about the third party calls from the coding challenge statement would be very interesting talking points. 

