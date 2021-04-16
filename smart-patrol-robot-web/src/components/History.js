import React from "react";
import { useHistory } from "react-router";
import Link from '@material-ui/core/Link';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';

function History () {
  const history = useHistory();

  return (
  <div>
    <h1 className="title is-1">This is the About Page</h1>
    <p>
      Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
      inceptos himenaeos. Vestibulum ante ipsum primis in faucibus orci luctus
      et ultrices posuere cubilia curae; Duis consequat nulla ac ex consequat,
      in efficitur arcu congue. Nam fermentum commodo egestas.
    </p>

    <Button onClick={() => history.push(
              {pathname: "/integrated-detail/".concat("z50vqTLF8sS1drQcnf2c"),
              })} color="secondary">try</Button>
    
  </div>
  )};

export default History;