import * as React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from '../components/Title';
import { useHistory } from "react-router";

function getRowStyle(status) {
  return { background: status==="Solved" ? '#ebebeb' : 'white',
            hover: {color: '#7EA5FF'}};
}

// function cellClicked (rowId) {
//   console.log(rowId)
// }

export default function CasesList(props) {
  const history = useHistory();
  var casesCollection = []
  var casesCollectionSolved = []
  var casesCollectionUnsolved = []
  if (props.casesCollection.length>0){
    casesCollection = props.casesCollection

    casesCollection.forEach( row => {
      if (row['solved']==="true"){
        row['solved'] = "Solved"
        casesCollectionSolved.push(row)
      }

      if (row['solved']==="false"){
        row['solved'] = "Unsolved"
        casesCollectionUnsolved.push(row)
      }

    })

    casesCollectionSolved.sort((a, b) => (a.time < b.time) ? 1 : -1)
    casesCollectionUnsolved.sort((a, b) => (a.time < b.time) ? 1 : -1)
    casesCollection = casesCollectionUnsolved.concat(casesCollectionSolved)

    var rowCount = casesCollection.length
    casesCollection.forEach( row => {
      row["rowCount"] = rowCount
      rowCount = rowCount-1
    })

  } 

  return (
    <React.Fragment>
      <Title>Unresolved Case</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Case Number</TableCell>
            <TableCell>Date</TableCell>
            <TableCell>Time</TableCell>
            <TableCell>Body Temperature (C)</TableCell>
            <TableCell>With Mask On</TableCell>
            <TableCell>Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {casesCollection.map((row) => (
            <TableRow key={row.id} hover style={{...getRowStyle(row.solved)}}
            onClick={() => history.push(
              {pathname: "/integrated-detail/".concat(row.docId),
              // state: {caseDetail: row}
              })}>
              <TableCell>{row.rowCount}</TableCell>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.time}</TableCell>
              <TableCell>{row.temp}</TableCell>
              <TableCell>{row.wearmask}</TableCell>
              <TableCell>{row.solved}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      {/* <Link color="primary" href="#" onClick={preventDefault} sx={{ mt: 3 }}>
        See more orders
      </Link> */}
    </React.Fragment>
  );
}