import React from 'react';
// You can use react-easy-crop or similar

function ImageCropModal({ image, onCrop, onCancel }) {
  // Implement cropping logic here or use a package
  // For now, just return the original image for demo
  return (
    <div>
      <h4>Crop Image</h4>
      <img src={URL.createObjectURL(image)} width="200" alt="To crop" />
      {/* Crop UI */}
      <button onClick={() => onCrop(image)}>Done</button>
      <button onClick={onCancel}>Cancel</button>
    </div>
  );
}

export default ImageCropModal;