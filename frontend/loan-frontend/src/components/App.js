import './App.css';
import React from 'react';

import Form from './Form';
import axios from 'axios';


class App extends React.Component {

    state = {
        amount: 0,
        monthlyRate: 0.0,
        payments: 0,
        interest: 5.5,
        interestMsg: ''
    };

    sendQuery = async (queryParams) => {
        const response = await axios.get('http://localhost:3001/loans', {
            params: queryParams,
        });
        if (response.data[0]) {
            this.setState({ 
                amount: response.data[0].amount, 
                monthlyRate: response.data[0].monthlyRate, 
                payments: response.data[0].payments, 
                interest: response.data[0].interest 
            });
            if (response.data[0].interestMsg) {
                this.setState({interestMsg: response.data[0].interestMsg});
            }
        }
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
                    />
                </div>
            </div>
        );
    }
}

export default App;
