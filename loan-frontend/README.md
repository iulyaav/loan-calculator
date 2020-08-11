## Loan Calculator frontend 

The frontend part is a small React app that has a form and makes call to an API to gather information about the loan terms (amount, tenure, monthly rate and interest).


### How to run the project

To start the app, you need to have `npm` running on your machine. Open two tabs, one for the mock API server and the other for the React app. In the first tab, you will need to first install all the packages and the start the app by running these commands in succession:
```
$ npm install
$ npm start
```
In the other tab, start the mock server by running 

```
$ json-server -p 3001 loans.json
```
inside the project folder (`loan_frontend`). 

The React App will be available at `http://localhost:3000/`, and the mock API will be sending out information from `http://localhost:3001`.


### How to use the application

This application is made up of a simple form with 4 inputs, out of which 3 are active and one is disabled. As it implemented right now, it makes calls to the API when pressing on the "Check interest" button. To simulate the cases when the app calculates the terms and the one when it checks if the interest is above or below a certain threshold, I have mocked two reponse calls (see more in `loan_frontend/loans.json`).

### Things to improve
This application is far from perfect. Here are some of the things that I am considering improving:
* make API calls on input change to have the values dynamically update when modifying a value.
* add input value validation on the frontend to prevent receiving errors from the backend
* make the page more user-responsive by highlighting the value inside an input when clicking on it (to ease having to delete a value before updating it) 
* add tests for the frontend
