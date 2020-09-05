import React, {Component} from 'react';
import './App.css';
import { Jumbotron, Button, Form } from 'react-bootstrap';
import axios from 'axios'

// Currently setup to be the navbar

export class Landing extends Component {

    constructor(props) {
        super(props)

        this.state = {
            email: '',
            phone: ''
        }
    }

    changeHandler = (e) => {
        this.setState({[e.target.name]: e.target.value})
    }

    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        axios.post('https://jsonplaceholder.typicode.com/posts', this.state)
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        const { email, phone } = this.state
        return (
            <div>
                <Jumbotron>
                    <h1 className="display-3">Breach Detector</h1>
                    <hr className="my-2" />
                    <form onSubmit={this.submitHandler}>
                        <div>
                            <input 
                                type="text" 
                                placeholder="E-mail" 
                                name="email" 
                                value={email} 
                                onChange={this.changeHandler}>
                            </input>
                        </div>
                        <div>
                            <input type="text" 
                                placeholder="Phone Number" 
                                name="phone"
                                value={phone}
                                onChange={this.changeHandler}>
                            </input>
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                    
                </Jumbotron>
            </div>
        );
    }
}
