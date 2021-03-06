import ListGroup from 'react-bootstrap/ListGroup'
import {ListCard} from './listCard'
import {useState} from 'react'

const ListDisplay = () => {
    let [data, setData] = useState([
            {
                "Company": "Apple",
                "Ticker": "AAPL",
                "Price":100,
                "Mentions": 12,
            },
            {
                "Company": "Tesla",
                "Ticker": "TSLA",
                "Price": 750,
                "Mentions": 10,
            },
            {
                "Company": "Amazon",
                "Ticker": "AMZN",
                "Price": 2000,
                "Mentions": 5,
            },
            {
                "Company": "FB",
                "Ticker": "FB",
                "Price": 150,
                "Mentions": 2
            }

    ])
    const dataMap = data.map((info, index) => 
        <ListGroup.Item className = 'bg-dark'>
            <ListCard company = {info.Company} ticker = {info.Ticker} price = {info.Price} mentions = {info.Mentions} rank = {index + 1} />
        </ListGroup.Item>
    )
    return (
        <ListGroup style = {{width: '60%'}}>
            {dataMap}
            
        </ListGroup>
    )
}

export {ListDisplay}