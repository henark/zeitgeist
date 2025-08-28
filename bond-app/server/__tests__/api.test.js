const request = require('supertest');
const express = require('express');
const oneInchWrapper = require('../oneInchWrapper');

// Mock the oneInchWrapper
jest.mock('../oneInchWrapper', () => ({
  createStopLossOrder: jest.fn(),
}));

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello from the backend!');
});

app.post('/orders/stop-loss', (req, res) => {
  const order = req.body;
  oneInchWrapper.createStopLossOrder(order);
  res.status(201).send('Stop-loss order received');
});

describe('API Endpoints', () => {
  it('should respond with "Hello from the backend!" for GET /', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Hello from the backend!');
  });

  it('should respond with 201 for POST /orders/stop-loss', async () => {
    const order = {
      tokenPair: 'ETH/USD',
      stopPrice: 3000,
      amount: 1,
    };

    const response = await request(app)
      .post('/orders/stop-loss')
      .send(order);

    expect(response.statusCode).toBe(201);
    expect(response.text).toBe('Stop-loss order received');
    expect(oneInchWrapper.createStopLossOrder).toHaveBeenCalledWith(order);
  });
});
