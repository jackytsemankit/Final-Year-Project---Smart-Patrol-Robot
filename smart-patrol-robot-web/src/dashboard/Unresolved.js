import * as React from 'react';
import Typography from '@material-ui/core/Typography';
import Title from '../components/Title';


export default function Unresolved(props) {
  return (
    <React.Fragment>
      <Title >Today's unresolved</Title>
      <Typography component="p" variant="h4">
        {props.counter}
      </Typography>
      <Typography color="textSecondary" sx={{ flex: 1 }}>
        on {props.currentDate}
      </Typography>
    </React.Fragment>
  );
}