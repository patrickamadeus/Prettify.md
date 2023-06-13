import React from 'react';

// const marked = require('marked');
import {marked} from 'marked';
const styles = require('../styles/MarkdownRenderer.module.css');

interface MarkdownRendererProps {
  markdown: string;
}

const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({ markdown }) => {
  const html = marked(markdown);

  return  (
    <div className={styles.outer}>
      <div className={styles.container} dangerouslySetInnerHTML={{ __html: html }}>
      </div>
    </div>
  );
};

export default MarkdownRenderer;
