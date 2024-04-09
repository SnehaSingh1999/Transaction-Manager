import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TransactionsTable = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const response = await axios.get('/transactions');
        setTransactions(response.data);
      } catch (error) {
        console.error(error); // Error handling
      }
    };

    fetchTransactions();
  }, []); // Empty dependency array to fetch data only once on component mount

  const handleEdit = async (transactionId, updatedData) => {
    try {
      const response = await axios.put(/transactions/${transactionId}, updatedData);
      console.log(response.data); // Success message
      // Update the transactions state locally (optional)
    } catch (error) {
      console.error(error); // Error handling
    }
  };

  const handleDelete = async (transactionId) => {
    try {
      const response = await axios.delete(/transactions/${transactionId});
      console.log(response.data); // Success message
      // Update the transactions state locally (optional)
    } catch (error) {
      console.error(error); // Error handling
    }
  };

  return (
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Amount</th>
          <th>Category</th>
          <th>Status</th>
          <th>Invoice URL</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {transactions.map((transaction) => (
          <tr key={transaction.id}>
            <td>{transaction.date}</td>
            <td>{transaction.amount}</td>
            <td>{transaction.category}</td>
            <td>{transaction.status}</td>
            <td>{transaction.invoice_url}</td>
            <td>
              <button onClick={() => handleEdit(transaction.id, { /* updated data */ })}>Edit</button>
              <button onClick={() => handleDelete(transaction.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TransactionsTable;
