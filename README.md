# Single-Cell RNA-seq RAG Analysis Toolkit

A retrieval-augmented generation (RAG) system for single-cell RNA-seq analysis, combining established R/Seurat workflows with AI-powered code adaptation.

## Overview

This repository contains a complete single-cell RNA-seq analysis pipeline with two key components:

1. **R Analysis Scripts**: A comprehensive set of R Markdown files covering the full scRNA-seq workflow from demultiplexing to advanced analysis
2. **Python RAG System**: An AI-powered assistant that helps adapt and customize the R scripts for specific datasets and research questions

## R Analysis Pipeline

The core analysis workflow consists of five sequential R Markdown scripts:

- `01_DemultiplexMULTIseq.Rmd` - Sample demultiplexing for multiplexed experiments
- `02_GEX_QC.Rmd` - Gene expression quality control and filtering
- `03_ADT_QC.Rmd` - Antibody-derived tag (ADT) quality control for CITE-seq data
- `04_GEX_Annotation.Rmd` - Cell type annotation and clustering
- `05_GEX_Analysis.Rmd` - Advanced analysis including differential expression and pathway analysis

These scripts provide a robust foundation for analyzing 10X Genomics single-cell data using the Seurat ecosystem.

## RAG Assistant

The `prototype.py` file implements a specialized chatbot that:

- Indexes the R analysis scripts in a vector database
- Provides contextual code recommendations based on user queries
- Helps customize scripts for specific datasets and research objectives
- Guides parameter selection with biological and computational context

### Key features

- **Smart code adaptation**: Identifies hard-coded parameters that need customization
- **Interactive guidance**: Prompts users for dataset-specific information
- **Educational explanations**: Provides rationale for parameter choices and method selection
- **R/Seurat focus**: Specialized for the R single-cell analysis ecosystem

## Getting started

### Prerequisites

**For R analysis:**
- R (≥4.0)
- Required packages: Seurat, dplyr, ggplot2, and others specified in each script

**For RAG assistant:**
- Python ≥3.13
- Dependencies: `llamabot[all]`, `marimo`

### Running the RAG assistant

```bash
# Launch the interactive assistant using uvx
uvx marimo edit --sandbox prototype.py
```

The assistant will automatically index the R scripts and provide an interactive interface for querying and adapting the analysis code.

### Using the R scripts

Each R Markdown file can be run independently or as part of the sequential workflow. Scripts include detailed documentation and can be customized for different experimental designs and datasets.

## Credits

The R analysis scripts were developed by **Emma Bishop** (@emjbishop) from Fred Hutchinson Cancer Center, with contributions from Jolie Phan. These scripts represent best practices for single-cell RNA-seq analysis in the Seurat ecosystem.

## Contributing

When modifying the analysis scripts, please maintain compatibility with the RAG indexing system and preserve the educational documentation that makes the code accessible to researchers with varying computational backgrounds.
