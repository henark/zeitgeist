import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

// Mock the global fetch function
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve({}),
  })
) as jest.Mock;

describe('App component', () => {
  beforeEach(() => {
    // Clear mock history before each test
    (global.fetch as jest.Mock).mockClear();
  });

  it('renders the main heading', () => {
    render(<App />);
    const headingElement = screen.getByText(/Bond - 1inch Limit Order Extensions/i);
    expect(headingElement).toBeInTheDocument();
  });

  it('renders the stop-loss order form', () => {
    render(<App />);
    expect(screen.getByLabelText(/Token Pair/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Stop Price/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Amount/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Submit Order/i })).toBeInTheDocument();
  });

  it('submits the form with the correct data', async () => {
    render(<App />);

    // Fill out the form
    fireEvent.change(screen.getByLabelText(/Stop Price/i), { target: { value: '3000' } });
    fireEvent.change(screen.getByLabelText(/Amount/i), { target: { value: '1' } });

    // Submit the form
    fireEvent.click(screen.getByRole('button', { name: /Submit Order/i }));

    // Wait for the fetch call to be made
    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledTimes(1);
    });

    // Check if fetch was called with the correct data
    expect(global.fetch).toHaveBeenCalledWith('/orders/stop-loss', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        tokenPair: 'ETH/USD',
        stopPrice: 3000,
        amount: 1,
      }),
    });
  });
});
