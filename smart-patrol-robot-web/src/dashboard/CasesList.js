import * as React from 'react';
import Link from '@material-ui/core/Link';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from '../components/Title';

// Generate Order Data
function createData(id, date, temp, status) {
  return { id, date, temp, status };
}

const rows = [
  createData(
    0,
    '16 Mar, 2019',
    '38.8',
    'Unresolved',
  ),
  createData(
    1,
    '16 Mar, 2019',
    '38.8',
    'Unresolved',
  ),
  createData(2, 
    '16 Mar, 2019',
    '38.8', 
    'Unresolved'
    ),
  createData(
    3,
    '16 Mar, 2019',
    '38.8',
    'Unresolved',
  ),
  createData(
    4,
    '15 Mar, 2019',
    'Long Branch, NJ',
    'Unresolved',
  ),
];

function preventDefault(event) {
  event.preventDefault();
}

export default function CasesList() {
  return (
    <React.Fragment>
      <Title>Unresolved Case</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Case Number</TableCell>
            <TableCell>Date And Time</TableCell>
            <TableCell>Body Temperature (C)</TableCell>
            <TableCell>Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.id}</TableCell>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.temp}</TableCell>
              <TableCell>{row.status}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
        See more orders
      </Link>
    </React.Fragment>
  );
}