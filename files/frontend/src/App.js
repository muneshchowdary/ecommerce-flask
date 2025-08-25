import React from 'react';
import ProductList from './components/ProductList';
import ProductEdit from './components/ProductEdit';

function App() {
  return (
    <div>
      <h1>E-commerce Site</h1>
      <ProductList />
      {/* ProductEdit can be shown in a modal or as a separate page */}
    </div>
  );
}

export default App;