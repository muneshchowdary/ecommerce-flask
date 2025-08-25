import React, { useState } from 'react';
import axios from 'axios';
import ImageCropModal from './ImageCropModal';

function ProductEdit({ product, onClose }) {
  const [form, setForm] = useState(product || {});
  const [image, setImage] = useState(null);
  const [croppedImage, setCroppedImage] = useState(null);
  const [showCrop, setShowCrop] = useState(false);

  const handleFileChange = (e) => {
    setImage(e.target.files[0]);
    setShowCrop(true);
  };

  const handleSave = async () => {
    const formData = new FormData();
    formData.append('name', form.name);
    formData.append('price', form.price);
    formData.append('description', form.description);
    if (croppedImage) {
      formData.append('image', croppedImage, croppedImage.name);
    }
    let res;
    if (form._id) {
      res = await axios.put(`http://localhost:5000/api/products/${form._id}`, formData);
    } else {
      res = await axios.post('http://localhost:5000/api/products', formData);
    }
    onClose();
  };

  return (
    <div style={{ background: "#fff", padding: 20 }}>
      <h3>{form._id ? "Edit Product" : "Add Product"}</h3>
      <input
        type="text"
        placeholder="Name"
        value={form.name || ""}
        onChange={e => setForm({ ...form, name: e.target.value })}
      />
      <input
        type="number"
        placeholder="Price"
        value={form.price || ""}
        onChange={e => setForm({ ...form, price: e.target.value })}
      />
      <textarea
        placeholder="Description"
        value={form.description || ""}
        onChange={e => setForm({ ...form, description: e.target.value })}
      />
      <input type="file" onChange={handleFileChange} />
      {showCrop &&
        <ImageCropModal
          image={image}
          onCrop={(croppedFile) => {
            setCroppedImage(croppedFile);
            setShowCrop(false);
          }}
          onCancel={() => setShowCrop(false)}
        />
      }
      <button onClick={handleSave}>Save</button>
      <button onClick={onClose}>Cancel</button>
    </div>
  );
}

export default ProductEdit;