import logo from './logo.svg';
import './App.css';
import { Switch, Route } from 'react-router-dom';
import Home from './components/Home';
import History from './components/History';
import Dashboard from './dashboard/Dashboard';
import DetailPage from './detailPage/DetailPage';


function App() {
  return (
    <main>
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/history" component={History} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/detail/:paramsdocid" component={DetailPage} />
        <Route path="/detail" component={DetailPage} />
        <Route component={Error} />
      </Switch>
    </main>

  );
}

export default App;
