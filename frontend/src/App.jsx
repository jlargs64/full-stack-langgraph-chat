import './App.css';
import MainContent from './components/MainContent';
import UserProvider from './components/UserProvider';

function App() {
  return (
    <UserProvider>
      <div className="container">
        <h1 className="title">LangGraph Agent Example</h1>
        <h2 className="subtitle">A Customer Support Use Case</h2>
        <MainContent />
      </div>
    </UserProvider>
  );
}

export default App;
