import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/header';
import AboutMe from './components/about';
import Experience from './components/experience';
import Education from './components/education';
import Skills from './components/skills';
import Footer from './components/footer';

function App() {
 return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={AboutMe} />
          <Route path="/experience" component={Experience} />
          <Route path="/education" component={Education} />
          <Route path="/skills" component={Skills} />
          {/* Add more routes as needed */}
        </Switch>
        <Footer />
      </div>
    </Router>
 );
}

export default App;