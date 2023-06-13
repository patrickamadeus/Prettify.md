import {useState, FC} from 'react';

import MarkdownRenderer from './MarkdownRenderer';
import MarkdownUploader from './MarkdownUploader';

const MarkdownInput: FC = () =>  {
    const [markdown, setMarkdown] = useState('');
    
    const handleMarkdownUploader = (file: File) => {
        const reader = new FileReader();
    
        reader.onload = (event) => {
            if (event.target) {
                setMarkdown(event.target.result as string);
            }
        };
    
        reader.readAsText(file);
    };
    
    return (
        <div>
            <MarkdownUploader onMarkdownUploader={handleMarkdownUploader} />
            <MarkdownRenderer markdown={markdown} />
        </div>
    );
}

export default MarkdownInput;