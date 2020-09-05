import React, {Component} from 'react';
import './App.css';
import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'

// Currently setup to be the navbar

export class Landing extends Component {
    render() {
        return (
            <div>
                <Jumbotron fluid>
                    <Container>
                        <h1>Breach Alert</h1>
                        <p>
                        This is a modified jumbotron that occupies the entire horizontal space of
                        its parent.
                        </p>
                    </Container>
                </Jumbotron>
            </div>
        );
    }
}
