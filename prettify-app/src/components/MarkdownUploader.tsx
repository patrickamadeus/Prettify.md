import React from 'react';

interface MarkdownUploaderProps {
  onMarkdownUploader: (file: File) => void;
}

const MarkdownUploader: React.FC<MarkdownUploaderProps> = ({ onMarkdownUploader }) => {
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files && event.target.files[0];

    if (file && file.name.endsWith('.md')) {
      onMarkdownUploader(file);
    } else {
      // File format not supported
      console.log('Please select a .md file.');
    }
  };

  return (
    <div>
      <input type="file" accept=".md" onChange={handleFileChange} />
    </div>
  );
};

export default MarkdownUploader;
