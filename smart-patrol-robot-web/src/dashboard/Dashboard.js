import * as React from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Box from '@material-ui/core/Box';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Link from '@material-ui/core/Link';
import Chart from './Chart';
import Unresolved from './Unresolved';
import CasesList from './CasesList';
import firebaseConfig from '../config/Config'

import firebase from 'firebase/app'
require("firebase/firestore");



function Copyright(props) {
  return (
    <Typography variant="body2" color="textSecondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

function createData(time, amount) {
  return { time, amount };
}

// const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  toolbar: {
    paddingRight: 24, // keep right padding when drawer closed
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),

  },
  appBarSpacer: theme.mixins.toolbar,

  alignItemsAndJustifyContent: {
    display: 'flex', 
    flexDirection: 'column',
    height: 240,
    alignItems: 'center',
    justifyContent: 'center',
  }
}));

export default function Dashboard() {
  const classes = useStyles();
  const [casesList, setCasesList] = React.useState([])


  //var currentDate =  new Date()
  var currentDate = new Date("2021-04-09");
  currentDate = currentDate.toISOString().split('T')[0]

  // console.log(currentDate)


  if (!firebase.apps.length) { firebase.initializeApp(firebaseConfig); }

  React.useEffect(() => {

    return firebase.firestore().collection("cases").where("date", "==", currentDate)
    .onSnapshot(querySnapshot => {
      var casesCollection = []

      if (!querySnapshot.empty){

        querySnapshot.forEach(function(doc) {
          var docObj = doc.data();
          docObj["docId"] = doc.id
          casesCollection.push(docObj);
        });
  
        casesCollection.forEach( function(obj, index) {
            obj.id = index.toString();
        })
      }
      setCasesList(casesCollection);
    });
  }, []);

  var casesCounterByHour = {
    "00": 0, 
    "03": 0,
    "06": 0,
    "09": 0,
    "12": 0,
    "15": 0,
    "18": 0,
    "21": 0,
    "24": 0,
  }

  var unresolvedCounter = 0 
  casesList.forEach( doc => {
    if(doc["solved"]==="false"){
      unresolvedCounter++;
    }

    var hour = doc["time"].substring(0, 2)

    if (hour==="00" || hour==="01" || hour==="02"){
      casesCounterByHour["00"]++
    }
    if (hour==="03" || hour==="04" || hour==="05"){
      casesCounterByHour["03"]++
    }
    if (hour==="06" || hour==="07" || hour==="08"){
      casesCounterByHour["06"]++
    }
    if (hour==="09" || hour==="10" || hour==="11"){
      casesCounterByHour["09"]++
    }
    if (hour==="12" || hour==="13" || hour==="14"){
      casesCounterByHour["12"]++
    }
    if (hour==="15" || hour==="16" || hour==="17"){
      casesCounterByHour["15"]++
    }
    if (hour==="18" || hour==="19" || hour==="20"){
      casesCounterByHour["18"]++
    }
    if (hour==="21" || hour==="22" || hour==="23"){
      casesCounterByHour["21"]++
    }
  })

  var chartData = [
    createData('00:00', casesCounterByHour["00"]),
    createData('03:00', casesCounterByHour["03"]),
    createData('06:00', casesCounterByHour["06"]),
    createData('09:00', casesCounterByHour["09"]),
    createData('12:00', casesCounterByHour["12"]),
    createData('15:00', casesCounterByHour["15"]),
    createData('18:00', casesCounterByHour["18"]),
    createData('21:00', casesCounterByHour["21"]),
    createData('24:00', casesCounterByHour["24"]),
  ];

  var unresolvedCounterString = unresolvedCounter.toString()
  console.log(unresolvedCounterString)

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar
        position="absolute"
        className={clsx(classes.appBar)}
      >
        <Toolbar className={classes.toolbar}>
          <Typography
            component="h1"
            variant="h6"
            color="inherit"
            noWrap
            sx={{ flexGrow: 1 }}
          >
            Dashboard
          </Typography>
        </Toolbar>
      </AppBar>

      <Box
        component="main"
        sx={{
          backgroundColor: (theme) =>
            theme.palette.mode === 'light'
              ? theme.palette.grey[100]
              : theme.palette.grey[900],
          flexGrow: 1,
          height: '100vh',
          overflow: 'auto',
          p: 10,
        }}
      >
        <div className={classes.appBarSpacer} />
        <Container maxWidth="lg" sx={{mt: 4, mb: 4,}}>
          <Grid container spacing={3} sx={{}}>

            {/* Today unresolved */}
            <Grid item xs={12} md={4} lg={3}>
              <Paper 
                className={classes.alignItemsAndJustifyContent}
                sx={{ p: 2,  }}
              >
                <Unresolved currentDate={currentDate} counter={unresolvedCounterString}/>
              </Paper>
            </Grid>
            {/* Chart */}
            <Grid item xs={12} md={8} lg={9}>
              <Paper
                sx={{ p: 2, display: 'flex', flexDirection: 'column' }}
              >
                <Chart chartData={chartData} />
              </Paper>
            </Grid>

            {/* Recent Cases */}
            <Grid item xs={12}>
              <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                <CasesList casesCollection={casesList}/>
              </Paper>
            </Grid>
          </Grid>
          <Copyright sx={{ pt: 4 }} />
        </Container>
      </Box>
    </Box>
  );
}