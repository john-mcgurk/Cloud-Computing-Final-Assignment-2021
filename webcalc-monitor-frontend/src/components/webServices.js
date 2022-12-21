import React from 'react';
import { List, Header } from "semantic-ui-react";

export const WebServices = ({ webServices }) => {
  return (
    <List>
      {webServices.map(service => {
        return (
          <List.Item key={service.name}>
            <h3 class="ui header">Server: {service.name}</h3><br></br>
            <main>{service.active}</main>
            <main>{service.functional}</main>
            <main>{service.errors}</main><br></br><br></br>
          </List.Item>
        );
      })}
    </List>
  );
};
