import './App.css';
import { Switch, Route } from 'react-router-dom';
import Dashboard from './dashboard/Dashboard';
import DetailPage from './detailPage/DetailPage';
import IntegratedDetailPage from './integratedDetailPage/IntegratedDetailPage';


function App() {
  return (
    <main>
      <Switch>
        <Route path="/" component={Dashboard} exact />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/detail/:paramsdocid" component={DetailPage} />
        <Route path="/integrated-detail/:paramsdocidprocessed" component={IntegratedDetailPage} />
        <Route component={Error} />
      </Switch>
    </main>

  );
}

export default App;
