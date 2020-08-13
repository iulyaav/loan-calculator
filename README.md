# Load Calculator

For the purpose of this exercise, I've chosen to use a mono-repo just for the convenience of it. Usually, although there are some tangible benefits in using a monorepo, my preference is for a clear separation between concerns. Thus I would opt for multiple repositories for such a project.


## How to run the project

### Running the frontend and backend together
With this method we will be serving the frontend and backend from the same URI. A nice side-effect is that it removes any CORS overhead as well. To get the application going, assuming you have all the packages already installed (see more information about how to do this in the next section), just run:

```
$ npm build
$ pipenv install
$ pipenv shell
$ python manage.py runserver
```

The website will be statically served from inside the `build` folder which will be created when running `npm build`. 

### Running the frontend and backend separately
To start the React app, you need to have `npm` running on your machine. Open two tabs, one for the mock API server and the other for the React app. In the first tab, you will need to first install all the packages and the start the app by running these commands in succession:
```
$ npm install
$ npm start
``` 

The React App will be available at `http://localhost:3000/`. Right now, there isn't any mock server to make up for the call to the backend, so you will have to separately start the backend server as well. To do this you need to have `pipenv` installed on your machine. You can easily accomplish this by running the pip install command inside a terminal. After that install the requirements and activate the shell.

```
$ pip install pipenv

$ pipenv install

$ pipenv shell
``` 

The just start up the server by running

```
$ python manage.py runserver
```

The server will be accessible at `localhost` on port `8000`. 
After that you can run queries either by using the `curl` command inside a terminal, or a tool such as `Postman`.

```
$ curl http://localhost:8000/?amount=12&payments=2
```


## Backend

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

### Questions to ponder

The implementation of this loan calculator is as simple as it gets. There are many things that I would have improved or that could spark an interesting conversation.


- Should we authenticate the user?
- Should we save these queries somewhere? Would we like to analyse this data at some point in the future?
- Would be benefit from using caching? 
- Numpy could prove to be not very memory efficient, should we implement those computations ourselves? Is the risk of having bugs in our calculations worth the advanatge of having everything in house?

This, together with the question about the third party calls from the coding challenge statement would be very interesting talking points. 



## Frontend

The frontend part is a small React app that has a form and makes call to an API to gather information about the loan terms (amount, tenure, monthly rate and interest).


### How to use the application

This application is made up of a simple form with 4 inputs, out of which 3 are active and one is disabled. As it implemented right now, it makes calls to the API when pressing on the "Check interest" button.

### Things to improve
This application is far from perfect. Here are some of the things that I am considering improving:
* make API calls on input change to have the values dynamically update when modifying a value.
* add input value validation on the frontend to prevent receiving errors from the backend
* make the page more user-responsive by highlighting the value inside an input when clicking on it (to ease having to delete a value before updating it) 
* add tests for the frontend
