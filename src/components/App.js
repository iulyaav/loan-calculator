import './App.css';
import React from 'react';

import Form from './Form';
import applyCaseMiddleware from 'axios-case-converter';
import axios from 'axios';


class App extends React.Component {

    state = {
        amount: 0,
        monthlyRate: 0.0,
        payments: 0,
        interest: 5.5,
        interestMsg: '',
        errorMsg: ''
    };

    sendQuery = async (queryParams) => {
        this.setState({errorMsg: ''});
        this.setState({interestMsg: ''});
        const client = applyCaseMiddleware(axios.create());
        const response = await client.get('http://localhost:8000/loan/', {
            params: queryParams,
        })
        .then( response =>  {
            if (response.data) {
                this.setState({ 
                    amount: response.data.amount, 
                    monthlyRate: response.data.monthlyRate, 
                    payments: response.data.payments, 
                    interest: response.data.interest 
                });
                if (response.data.interestMsg) {
                    this.setState({interestMsg: response.data.interestMsg});
                }
            }
          })
        .catch(error => {
            this.setState({errorMsg: "There was some problem with your request. Try again later!"});
        });
        
    }

    onInputChange = (target, value) => {
        this.setState({ [target]: value });
    }

    onFormSubmit = async () => {

        const queryParams = query => (
            {
            ...query.amount && { amount: query.amount },
            ...query.monthlyRate && { monthlyRate: query.monthlyRate },
            ...query.payments && { payments: query.payments }
          });
        
        this.sendQuery(queryParams(this.state));
    }


    render() {
        return (
            <div className="app">
                <div className="containerr">
                    <h1>Loan Calculator</h1>
                    <hr/>
                    <Form 
                        onSubmit={this.onFormSubmit}
                        onInputChange={this.onInputChange}
                        amount={this.state.amount}
                        monthlyRate={this.state.monthlyRate}
                        payments={this.state.payments}
                        interest={this.state.interest}
                        interestMsg={this.state.interestMsg}
                        errorMsg={this.state.errorMsg}
                    />
                </div>
            </div>
        );
    }
}

export default App;
