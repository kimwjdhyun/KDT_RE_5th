import { Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import './styles/App.css';
import MainPage from './pages/MainPage';
import ProductPage from './pages/ProductPage';
import ProductDetailPage from './pages/ProductDetailPage';
import { useEffect, useState } from 'react';
import axios from 'axios'
import PracticePage from './pages/PracticePage';
import Practice from './components/Practice';
import Practice2 from './components/Practice2';

function App() {
	const [products, setProducts] = useState([]);

	const getProducts = async () => {
		const res = await axios.get(
			'https://jsonplaceholder.typicode.com/comments'
		);
		console.log(res.data);
		setProducts(res.data.slice(0,10));
	}
	useEffect(() => {
		getProducts();
	}, []);
	return (
		<div className='App'>
			<Header />
			<Routes>
				<Route path='/' element={<MainPage />} />
				<Route path='/products' element={<ProductPage products={products} />} />
				<Route
					path='/products/:productId'
					element={<ProductDetailPage products={products} />}
				/>
				<Route path="/practice" element={<PracticePage />} />
				<Route path="/student/:name" element={<Practice />} />
				<Route path="/student/new" element={<Practice2 />} />
			</Routes> 
		</div>
	);
}

export default App;
