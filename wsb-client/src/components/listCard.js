import Card from 'react-bootstrap/Card'
import Col from 'react-bootstrap/Col'
const ListCard = (props) => {
    return (
        <Card className = 'd-flex'>
            <Col className = 'border'>
            <Card.Title>{props.company}</Card.Title>
            <Card.Subtitle>{props.ticker}</Card.Subtitle>
            </Col>
           <Col className = 'border'>
           <h1>{props.price}</h1>
           <p>Mentions: {props.mentions}</p>
           </Col>
        </Card>
    )
}

export {ListCard} 