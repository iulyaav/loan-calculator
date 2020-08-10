import './Form.css';
import React from 'react';


class Form extends React.Component {

    onInputChange = (event) => {
        this.props.onInputChange(event.target.value);
    }


    onFormSubmit = (event) => {
        event.preventDefault();
        this.props.onSubmit(100);
    }

    render() {
        return (
            <form onSubmit={this.onFormSubmit}>
                <div className="row">
                    <div className="column">
                        <label htmlFor="amount">Loan amount</label>
                        <input type="text"  value={this.props.amount} onChange={this.onInputChange} id="amount"></input>
                    </div>
                    <div className="column">
                        <label htmlFor="payments">Tenure</label>
                        <input type="text"  value={this.props.payments} placeholder="*No. months" id="payments"></input>
                    </div>
                    <div className="column">
                        <label htmlFor="monthlyRate">Monthly rate</label>
                        <input type="text"  value={this.props.monthlyRate} id="monthlyRate"></input>
                    </div>
                    <div className="column">
                        <label htmlFor="interest">Interest (our rate)</label>
                        <input type="text"  value={this.props.interest} id="interest" disabled></input>
                        <p className="under-text">Some text</p>
                    </div>
                </div>
                <div className="row row-button">
                    <input className="button-primary column" type="submit" value="Check loan"/>
                </div>
                <hr/>
            </form>
        );
    }
}

export default Form;
