// Components
import MarkdownInput from './components/MarkdownInput';
import Title from './components/Title';

import './App.css';
import React from 'react';

const App: React.FC = () => {
  return (
    <div className="App">
      <Title title="Prettify.md" subtitle="Refine markdown. Empower content." />
      <MarkdownInput />
    </div>
  );
}

export default App;
