// import logo from './logo.svg';
import './App.css';
import FileUpload from './components/fileupload';
import TransactionsTable from './components/Transactiontable';
import TransactionsInsights from './components/Insights';
import InvoiceViewer from './components/invoicsviewer';

function App() {
  return (
    <div className="App">
     <h1>Financial Transaction Tracker</h1>
     <FileUpload/>
     <TransactionsTable/>
     <TransactionsInsights/>
     <InvoiceViewer/>
    </div>
  );
}

export default App;
