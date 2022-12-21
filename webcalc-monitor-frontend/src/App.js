import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import {WebServices} from "./components/webServices"
import { Container } from "semantic-ui-react";

function App() {
  const [webServices, setServices] = useState([]);
  useEffect(() => {
    fetch('/testWebServices').then(response =>
      response.json().then(data => {
        setServices(data);
      })
    );
  }, [])
  ;

  return (
    <div className="App">
    <Container style = {{marginTop: 40}}>
      <WebServices webServices = {webServices}/>
    </Container>
    </div>
  );
}

export default App;
