import logo from './logo.svg';
import './App.css';
import { Switch, Route } from 'react-router-dom';
import Home from './components/Home';
import History from './components/History';


function App() {
  return (
    <main>
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/history" component={History} />
        <Route component={Error} />
      </Switch>
    </main>

  );
}

export default App;
