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
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import HomeIcon from '@material-ui/icons/Home';
import TempChart from './TempChart';

import { useParams, Route } from 'react-router-dom';
import { useHistory } from "react-router-dom";

import Title from '../components/Title';

import firebaseConfig from '../config/Config'

import firebase from 'firebase/app'
import { TrendingUpRounded } from '@material-ui/icons';
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


function CamImages(props) {
  return (
    <Grid item xs={12} md={4}>
      <Paper className={props.classes.alignItemsAndJustifyContent}>
          <img src={props.caseDetail['img'][props.index]} style={{width:'100%', height:'auto'}}/>
      </Paper>
  </Grid>
  );
}

function EmptyImages(props) {
  return (
    <Grid item xs={12} md={4} >
      <Paper className={props.classes.alignItemsAndJustifyContent}>
      </Paper>
  </Grid>
  );
}

function createData(time, amount) {
    return { time, amount };
  }


const drawerWidth = 240;

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
  },

  detailBox: {
    display: 'flex', 
    flexDirection: 'column',
    alignItems: 'flex-start',
    justifyContent: 'center',
    padding: 24
  }
}));

export default function IntegratedDetailPage(props) {
  const classes = useStyles();
  const { paramsdocidprocessed } = useParams();
  console.log(paramsdocidprocessed)
  const history = useHistory();
  const [caseDetail, setCaseDetail] = React.useState({})
  const [fetched, setFetched] = React.useState(false)
  const [docId, setDocId] = React.useState(paramsdocidprocessed)

  if (!firebase.apps.length) { firebase.initializeApp(firebaseConfig); }

  React.useEffect(() => {

    return firebase.firestore().collection("processed_cases").where(firebase.firestore.FieldPath.documentId(), "==", paramsdocidprocessed)
    .onSnapshot(querySnapshot => {
      var queryResult = {}
      var id;
      if (!querySnapshot.empty){
        queryResult = querySnapshot.docs[0].data()
        id = querySnapshot.docs[0].id
        if (queryResult['solved']==="true"){
          queryResult['solved'] = "Solved"
        }
  
        if (queryResult['solved']==="false"){
          queryResult['solved'] = "Unsolved"
        }
      }
      console.log(queryResult)
      setCaseDetail(queryResult)
      setFetched(true)
      setDocId(id)
    });
  }, []);

  if (fetched){
      var chartDataObj = caseDetail.tempdict
      var tempKey = Object.keys(chartDataObj)
      var chartData = []

      tempKey.forEach( key => {
          var temp = createData(key, parseFloat(chartDataObj[key]))
          chartData.push(temp)
      })
  }


  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar
        position="absolute"
        className={clsx(classes.appBar)}
      >
        <Toolbar className={classes.toolbar}>
        <IconButton
            edge="start"
            color="inherit"
            onClick={() => history.push(
              {pathname: "/dashboard/",
              })}
          >
            <HomeIcon />
          </IconButton>
          <Typography
            component="h1"
            variant="h6"
            color="inherit"
            noWrap
            sx={{ flexGrow: 1 }}
          >
            Case Detail 
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
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Grid container spacing={3} mt={8}>

          {/* Thermal image */}
          {fetched ? (
            <CamImages index={0} classes={classes} caseDetail={caseDetail}></CamImages>
          ):(
            <EmptyImages classes={classes}/>
          )
          }

          {fetched ? (
            <CamImages index={1} classes={classes} caseDetail={caseDetail}></CamImages>
          ):(
            <EmptyImages classes={classes}/>
          )
          }

          {fetched ? (
            <CamImages index={2} classes={classes} caseDetail={caseDetail}></CamImages>
          ):(
            <EmptyImages classes={classes}/>
          )
          }

          {fetched ? (
            <Grid item xs={12} >
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                            <TempChart chartData={chartData} />
                </Paper>
            </Grid>
          ):(
            <Grid item xs={12} >
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                Loading
                </Paper>
            </Grid>
          )}

          {fetched ? (
                        <Grid item xs={12}>
                        <Paper 
                          className={classes.detailBox}
                        >
                          <Title > Unresolved Case #{caseDetail["caseid"]}</Title>
                          <Typography component="p" variant="h6">
                              Date: {caseDetail["date"]}
                          </Typography>
                          <Typography component="p" variant="h6">
                              Time: {caseDetail["time"].trim()}
                          </Typography>
                          <Typography component="p" variant="h6">
                              Average Temperature: {caseDetail["temp"].trim()}
                          </Typography>
                          <Typography component="p" variant="h6">
                              Status: {caseDetail["solved"].trim()}
                          </Typography>
                          <Typography component="p" variant="h6">
                              Zone: {caseDetail["zoneNo"]}
                          </Typography>
                          
                          {caseDetail["solved"]==="Unsolved" ? (
                            <Button onClick={() => { 
                              firebase.firestore().collection("cases").doc(docId)
                              .update({solved: "true" })
                              .then(
                                history.push({pathname: "/dashboard"})
                              );
                            }} variant="outlined">Solve</Button>
                          ):(
                            <Button onClick={() => { 
                              firebase.firestore().collection("cases").doc(docId)
                              .update({solved: "false" })
                              .then(
                                history.push({pathname: "/dashboard"})
                              );
                            }} color="secondary">Undo solved</Button>
                          )
                          }


                        </Paper>
                      </Grid>
          ):(
            <Grid item xs={12}>
            <Paper 
              className={classes.detailBox}
            >
              <Title > Unresolved Case </Title>
              <Typography component="p" variant="h6">
                  Loading
              </Typography>
            </Paper>
          </Grid>
          )
          }



          
          </Grid>
          <Copyright sx={{ pt: 4 }} />
        </Container>
      </Box>
    </Box>
  );
}