import './App.css';
import React from 'react';

import Form from './Form';
import axios from 'axios';


class App extends React.Component {

    state = {
        amount: 0,
        monthlyRate: 0.0,
        payments: 0,
        interest: 1.0
    };

    onInputChange = (value) => {
        this.setState({amount: value});
    }

    onFormSubmit = async (amount) => {
        const response = await axios.get('http://localhost:3001/loans', {
            params: {
                amount: amount
            },
        });
        console.log(response);
        this.setState({ amount: 10, monthlyRate: 5.5, payments: 2, interest: 1.5 });
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
                    />
                </div>
            </div>
        );
    }
}

export default App;
