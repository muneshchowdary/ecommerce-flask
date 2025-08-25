import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProductEdit from './ProductEdit';

function ProductList() {
  const [products, setProducts] = useState([]);
  const [editingProduct, setEditingProduct] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/products')
      .then(res => setProducts(res.data));
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <button onClick={() => setEditingProduct({})}>Add Product</button>
      <ul>
        {products.map(product => (
          <li key={product._id}>
            <img src={`http://localhost:5000${product.imageUrl}`} width="100" alt={product.name} />
            <div>
              <strong>{product.name}</strong>
              <p>{product.description}</p>
              <p>${product.price}</p>
              <button onClick={() => setEditingProduct(product)}>Edit</button>
            </div>
          </li>
        ))}
      </ul>
      {editingProduct && (
        <ProductEdit
          product={editingProduct}
          onClose={() => setEditingProduct(null)}
        />
      )}
    </div>
  );
}

export default ProductList;