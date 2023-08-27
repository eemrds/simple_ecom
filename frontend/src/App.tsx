import React, { useEffect, useState } from "react";


interface Product {
  id: string;
  name: string;
  price: number;
}

interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
}

const API_BASE = 'http://0.0.0.0:8000';

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [cart, setCart] = useState<CartItem[]>([]);

  useEffect(() => {
    fetch(`${API_BASE}/products/`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Network response was not ok: ${res.statusText}`);
        }
        return res.json();
      })
      .then(setProducts)
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
      });

    fetch(`${API_BASE}/cart/`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Network response was not ok: ${res.statusText}`);
        }
        return res.json();
      })
      .then(setCart)
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
      });
  }, []);

  const addToCart = (product: Product) => {
    fetch("/cart/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(product),
    })
      .then((res) => res.json())
      .then((newCart) => setCart(newCart));
  };

  const removeFromCart = (productId: string) => {
    fetch(`/cart/${productId}/`, {
      method: "DELETE",
    })
      .then((res) => res.json())
      .then((newCart) => setCart(newCart));
  };

  return (
    <div>
      <h1>Products</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - ${product.price}
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </li>
        ))}
      </ul>
      <h1>Cart</h1>
      <ul>
        {cart.map((item) => (
          <li key={item.id}>
            {item.name} - ${item.price} x {item.quantity}
            <button onClick={() => removeFromCart(item.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;