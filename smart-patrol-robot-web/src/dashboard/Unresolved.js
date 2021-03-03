import * as React from 'react';
import Typography from '@material-ui/core/Typography';
import Title from '../components/Title';

function preventDefault(event) {
  event.preventDefault();
}

export default function Unresolved() {
  return (
    <React.Fragment>
      <Title >Today's unresolved</Title>
      <Typography component="p" variant="h4">
        3
      </Typography>
      <Typography color="textSecondary" sx={{ flex: 1 }}>
        on 11 March, 2019
      </Typography>
    </React.Fragment>
  );
}