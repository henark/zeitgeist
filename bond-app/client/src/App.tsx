import React, { useState } from 'react';
import './App.css';

function App() {
  const [stopPrice, setStopPrice] = useState('');
  const [amount, setAmount] = useState('');
  const [tokenPair, setTokenPair] = useState('ETH/USD'); // Default token pair

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    const order = {
      tokenPair,
      stopPrice: parseFloat(stopPrice),
      amount: parseFloat(amount),
    };

    try {
      const response = await fetch('/orders/stop-loss', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(order),
      });

      if (response.ok) {
        alert('Stop-loss order submitted successfully!');
        // Clear the form
        setStopPrice('');
        setAmount('');
      } else {
        alert('Failed to submit stop-loss order.');
      }
    } catch (error) {
      console.error('Error submitting stop-loss order:', error);
      alert('An error occurred while submitting the order.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Bond - 1inch Limit Order Extensions</h1>
      </header>
      <main>
        <h2>Create a Stop-Loss Order</h2>
        <form onSubmit={handleSubmit} className="order-form">
          <div className="form-group">
            <label htmlFor="token-pair">Token Pair</label>
            <select
              id="token-pair"
              value={tokenPair}
              onChange={(e) => setTokenPair(e.target.value)}
            >
              <option value="ETH/USD">ETH/USD</option>
              <option value="BTC/USD">BTC/USD</option>
              {/* Add more token pairs as needed */}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="stop-price">Stop Price</label>
            <input
              id="stop-price"
              type="number"
              value={stopPrice}
              onChange={(e) => setStopPrice(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="amount">Amount</label>
            <input
              id="amount"
              type="number"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="submit-button">Submit Order</button>
        </form>
      </main>
    </div>
  );
}

export default App;
