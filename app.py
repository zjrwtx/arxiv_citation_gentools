import gradio as gr
from citation import get_arxiv_metadata, format_citation

def process_citations(arxiv_ids, citation_style, add_numbers):
    # Split the input into individual arXiv IDs
    ids = [id.strip() for id in arxiv_ids.split('\n') if id.strip()]
    results = []
    errors = []
    
    for idx, arxiv_id in enumerate(ids, 1):
        try:
            metadata = get_arxiv_metadata(arxiv_id)
            citation = format_citation(metadata, citation_style)
            if add_numbers:
                results.append(f"[{idx}] {citation}\n")
            else:
                results.append(f"✓ {arxiv_id}:\n{citation}\n")
        except Exception as e:
            errors.append(f"✗ {arxiv_id}: {str(e)}\n")
    
    # Combine results and errors
    output = "处理结果：\n\n" + "".join(results)
    if errors:
        output += "\n错误信息：\n" + "".join(errors)
    
    return output

# 创建Gradio界面
demo = gr.Interface(
    fn=process_citations,
    inputs=[
        gr.Textbox(
            label="arXiv ID列表",
            placeholder="每行输入一个arXiv ID，例如：\n2301.12345\n2302.54321",
            lines=5
        ),
        gr.Radio(
            choices=["APA", "MLA", "Chicago", "IEEE"],
            label="引用格式",
            value="APA"
        ),
        gr.Checkbox(
            label="添加引用编号",
            value=True,
            info="在每条引用前添加序号 [1], [2], ..."
        )
    ],
    outputs=gr.Textbox(label="生成的引用", lines=10, show_copy_button=True),
    title="arXiv论文引用生成器（开源在github）",
    description="批量生成arXiv论文的引用格式，支持APA, MLA, Chicago, IEEE等格式，每行输入一个arXiv ID，选择所需的引用格式。开源地址：https://github.com/zjrwtx/arxiv_citation_gentools",
    examples=[
        ["2402.06196", "APA", True],
        ["2303.18223", "MLA", True],
        ["2402.01680", "IEEE", True]
    ],
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(share=False)
