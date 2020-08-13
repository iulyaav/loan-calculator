import './Form.css';
import React from 'react';


class Form extends React.Component {

    onInputChange = (event) => {
        this.props.onInputChange(event.target.id, event.target.value);
    }


    onFormSubmit = (event) => {
        event.preventDefault();
        this.props.onSubmit();
    }

    render() {
        return (
            <form onSubmit={this.onFormSubmit}>
                <div className="row">
                    <div className="column">
                        <label htmlFor="amount">Loan amount</label>
                        <input type="text" value={this.props.amount} onChange={this.onInputChange} id="amount"></input>
                    </div>
                    <div className="column">
                        <label htmlFor="payments">Tenure</label>
                        <input type="text" value={this.props.payments} onChange={this.onInputChange} placeholder="*No. months" id="payments"></input>
                        <p className="under-text">*in number of months</p>
                    </div>
                    <div className="column">
                        <label htmlFor="monthlyRate">Monthly rate</label>
                        <input type="text" value={this.props.monthlyRate} onChange={this.onInputChange} id="monthlyRate"></input>
                    </div>
                    <div className="column">
                        <label htmlFor="interest">Interest</label>
                        <input type="text"  value={this.props.interest} id="interest" disabled></input>
                        {this.props.interestMsg && <p className="under-text">{this.props.interestMsg}</p>}
                    </div>
                </div>
                <div className="row row-button">
                    <input className="button-primary column" type="submit" value="Check loan"/>
                </div>
                <div className="row">
                    {this.props.errorMsg && <p className="under-text">{this.props.errorMsg}</p>}
                </div>
                <hr/>
            </form>
        );
    }
}

export default Form;
