import { useParams } from "react-router-dom";
import { productInfos } from "../components/ProductList";

function ProductDetailPage() {
    const {productId} = useParams(); // string 타입으로 반환 ex) '2'
    const product = productInfos[Number(productId) - 1];
    return (
        <div>
            <h1>Product Detail Page</h1>
            <ul>
                    <li>상품 번호 : {product.id}</li>
					<li>상품명: {product.name}</li>
                    <li>판매자 : {product.email}</li>
					<li>상세 설명: {product.body}</li>
				</ul>
        </div>
    );
}

export default ProductDetailPage;