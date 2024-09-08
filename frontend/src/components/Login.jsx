import { useState } from 'react';

export default function Login() {
  const [isRegistered, setIsRegistered] = useState(true);
  const [email, setEmail] = useState('');
  const [fullName, setFullName] = useState('');
  const [password, setPassword] = useState('');

  const handleToggle = (isLogin) => {
    setIsRegistered(isLogin);
  };

  return (
    <>
      <div className="tabs is-centered is-large is-toggle is-toggle-rounded">
        <ul>
          <li
            className={isRegistered ? 'is-active' : ''}
            onClick={() => handleToggle(true)}
          >
            <a>
              <span>Login</span>
            </a>
          </li>
          <li
            className={!isRegistered ? 'is-active' : ''}
            onClick={() => handleToggle(false)}
          >
            <a>
              <span>Register</span>
            </a>
          </li>
        </ul>
      </div>
      <div className="box">
        {isRegistered ? (
          <div>
            <h2 className="title is-4">Login</h2>
            <div className="field">
              <label className="label">Email</label>
              <div className="control">
                <input
                  className="input"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Password</label>
              <div className="control">
                <input
                  className="input"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            </div>
            <button className="button is-primary">Login</button>
          </div>
        ) : (
          <div>
            <h2 className="title is-4">Register</h2>
            <div className="field">
              <label className="label">Full Name</label>
              <div className="control">
                <input
                  className="input"
                  type="text"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Email</label>
              <div className="control">
                <input
                  className="input"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            </div>
            <div className="field">
              <label className="label">Password</label>
              <div className="control">
                <input
                  className="input"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            </div>
            <button className="button is-primary">Register</button>
          </div>
        )}
      </div>
    </>
  );
}
