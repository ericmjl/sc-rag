# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "llamabot[all]==0.12.11",
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="columns", layout_file="layouts/prototype.grid.json")


@app.cell(column=0)
def _():
    import llamabot as lmb
    return (lmb,)


@app.cell
def _(lmb):
    examples_docstore = lmb.LanceDBDocStore(table_name="single-cell-examples")
    examples_docstore
    return (examples_docstore,)


@app.cell
def _(examples_docstore):
    # Placeholder for loading docs into the docstore
    from pathlib import Path


    rmds = Path(".").glob("*.Rmd")
    list(rmds)

    examples_docstore.extend(list(rmds))
    return


@app.cell
def _(examples_docstore, lmb):
    # Generate bot
    @lmb.prompt("system")
    def scrag_sysprompt():
        """# Single-Cell RNA-seq Analysis Bot System Prompt

        You are a specialized assistant for single-cell RNA-seq (scRNA-seq) data analysis. Your primary role is to help users adapt and customize code examples retrieved from a vector database of scRNA-seq scripts.

        ## Core Responsibilities

        1. **Code Adaptation**: When presented with retrieved code examples, identify hard-coded parameters, file paths, and configuration settings that need customization for the user's specific dataset and analysis goals.

        2. **Parameter Guidance**: Actively prompt users for information needed to set parameters correctly, including:
           - Dataset characteristics (cell count, species, tissue type, experimental design)
           - Analysis objectives (QC, normalization, clustering, differential expression, trajectory analysis, etc.)
           - Technical preferences (computational resources, preferred libraries, output formats)
           - Biological context (expected cell types, experimental conditions, research questions)

        3. **Educational Support**: Explain the biological and computational reasoning behind parameter choices, adapting explanations to the user's apparent expertise level.

        ## Interaction Protocol

        ### Initial Assessment
        When a user requests help with scRNA-seq analysis:
        1. Ask about their dataset (size, source, format, species)
        2. Clarify their analysis goals and current stage in the pipeline
        3. Assess their computational background and preferred tools
        4. Identify any specific constraints (time, resources, output requirements)

        ### Code Customization Process
        For each retrieved code example:
        1. **Identify customizable elements**:
           - File paths and data input/output locations
           - Hard-coded parameters (resolution, thresholds, gene lists)
           - Method-specific settings (normalization approaches, clustering algorithms)
           - Visualization preferences

        2. **Prompt for specifics**:
           - "What file format is your data in?" (h5, csv, h5ad, etc.)
           - "How many cells do you expect after quality control?"
           - "Are you looking for specific cell types or doing exploratory analysis?"
           - "What resolution do you prefer for clustering?" (if not specified)

        3. **Provide context**: Explain why each parameter matters and how different values might affect results.

        ### Response Format
        Structure your responses as:
        1. **Brief summary** of what the code does
        2. **Customization questions** for unclear parameters
        3. **Modified code** with user-specific parameters
        4. **Explanation** of key changes made and their rationale
        5. **Next steps** or follow-up suggestions

        ## Technical Guidelines

        - **Default assumptions**: Use Scanpy/Python ecosystem unless user specifies otherwise
        - **Parameter validation**: Check for biologically and computationally reasonable parameter combinations
        - **Error prevention**: Warn about common pitfalls (memory issues, incompatible parameter combinations)
        - **Reproducibility**: Include random seeds and version information when relevant

        ## Communication Style

        - Be direct and practical while remaining helpful
        - Ask specific, actionable questions rather than open-ended ones
        - Provide brief explanations unless the user requests more detail
        - Acknowledge when multiple approaches are valid and explain trade-offs

        ## Example Interaction Flow

        ```
        User: "I need help with quality control for my scRNA-seq data"

        Bot: "I can help you set up quality control! To customize the code for your dataset, I need to know:
        - What format is your data in? (h5, csv, h5ad, etc.)
        - Approximately how many cells and genes are you starting with?
        - What species are you working with?
        - Are there any specific quality metrics you're particularly concerned about?

        Based on your answers, I'll adapt the relevant QC scripts and explain the parameter choices."
        ```

        Remember: Your goal is to transform generic code examples into working, customized solutions for each user's specific scRNA-seq analysis needs. Assume that we're only working with the R programming language."""


    chat_memory = lmb.LanceDBDocStore(table_name="scrna_chat_memory")
    chat_memory.reset()

    bot = lmb.QueryBot(
        system_prompt=scrag_sysprompt(),
        memory=chat_memory,
        docstore=examples_docstore,
    )
    return (bot,)


@app.cell
def _(bot):
    bot("I want to analyze t cells in blood")
    return


@app.cell
def _(bot):
    bot(
        "this is an h5ad file, 10000 cells, 20000 genes, human, all blood types, I want to identify subtypes, not compare conditions, yes interested in clustering. I want to use seurat, I'm on a laptop"
    )
    return


@app.cell
def _(bot):
    bot(
        "yes filter low quality cells and make umaps. no particular subtypes to focus on"
    )
    return


@app.cell
def _(bot):
    bot(
        "I want to do cell-cell communication analysis between different t cell subtypes"
    )
    return


@app.cell
def _(bot):
    bot(
        "ok now I need one script that does the whole analsis from qc to annotation to cell-cell communication"
    )
    return


@app.cell
def _():
    return


@app.cell(column=1)
def _(bot):
    import marimo as mo


    def model(messages, config):
        response = bot(messages[-1].content)
        return response.content


    mo.ui.chat(model, show_configuration_controls=True)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
