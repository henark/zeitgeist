const express = require('express');
const app = express();
const port = 3001;
const oneInchWrapper = require('./oneInchWrapper');

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello from the backend!');
});

// Example endpoint for creating a stop-loss order
app.post('/orders/stop-loss', (req, res) => {
    // In a real application, you would get the order details from the request body
    const order = req.body;
    oneInchWrapper.createStopLossOrder(order);
    res.status(201).send('Stop-loss order received');
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
