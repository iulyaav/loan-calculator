import './App.css';
import React from 'react';

import Form from './Form';


class App extends React.Component {

    render() {
        return (
            <div className="container app app-border">
                <div className="content">
                    <h1>Loan Calculator</h1>
                    <hr/>
                    <Form />
                </div>
            </div>
        );
    }
}

export default App;
