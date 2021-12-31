import Card from 'react-bootstrap/Card'
import Col from 'react-bootstrap/Col'
const ListCard = (props) => {
    return (
        <Card className = 'd-flex'>
            <h1>{props.rank}</h1>
            <Col className = 'border-bottom'>
            <Card.Title className = 'text-primary'>{props.company}</Card.Title>
            <Card.Subtitle>Ticker Symbol: {props.ticker}</Card.Subtitle>
            </Col>
           <Col style = {{width: '50%'}}>
           <h3>Price: ${props.price}</h3>
           <p>Mentions: {props.mentions}</p>
           </Col>
        </Card>
    )
}

export {ListCard} 