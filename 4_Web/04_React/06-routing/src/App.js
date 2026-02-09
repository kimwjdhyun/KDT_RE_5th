import { Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import './styles/App.css';
import MainPage from './pages/MainPage';
import ProductPage from './pages/ProductPage';
import ProductDetailPage from './pages/ProductDetailPage';

function App() {
	return (
		<div className='App'>
			<Header />
			<Routes>
				<Route path='/' element={<MainPage />} />
				<Route path='/products' element={<ProductPage />} />
				<Route
					path='/products/:productId'
					element={<ProductDetailPage />}
				/>
			</Routes>
		</div>
	);
}

export default App;
