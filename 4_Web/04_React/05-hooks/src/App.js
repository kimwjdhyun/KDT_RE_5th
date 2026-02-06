import './App.css';
import CssModule from './components/CssModule';
import Faq from './components/Faq';
import Practice from './components/Practice';
import StyledComponent from './components/StyledComponent';
import UseMemoEx from './components/UseMemoEx'

function App() {
  return (
    <div className="App">
      <UseMemoEx />
      <hr />
      <Faq></Faq>
      <hr />
      {/* CSS Styling */}
      <CssModule />
      {/* Styled Component */}
      <h2>styled0components</h2>
      <StyledComponent />
      {/* 종합 실습. pronps, state, event */}
      <h2>종합 실습</h2>
      <Practice />
    </div>
  );
}

export default App;