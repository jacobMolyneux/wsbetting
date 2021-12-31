import {ListDisplay} from './components/listDisplay'
import Row from 'react-bootstrap/Row';

function App() {
  return (
    <div className="d-flex-column justify-content-center">
      <Row className = 'bg-white' style = {{width: '110%'}}> 
      <h1>Wall Street Betting</h1>
      
      </Row>
      <Row style={{width: '100%'}} className = 'd-flex justify-content-center'>
      <ListDisplay/>
      </Row>
    </div>
  );
}

export default App;
