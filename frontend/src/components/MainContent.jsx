import useUser from '../hooks/useUser';
import Dashboard from './Dashboard';
import Login from './Login';

export default function MainContent() {
  const { user } = useUser();

  if (user) {
    return <Dashboard />;
  } else {
    return <Login />;
  }
}
