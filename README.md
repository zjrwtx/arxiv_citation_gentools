---
title: ArXiv Citation Generator
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "5.12.0"
app_file: app.py
pinned: false
tags:
  - arxiv
  - citation
  - academic
  - research
---
在线体验地址：https://zjrwtxtechstudio-arxiv-citation-gentools.hf.space

# arXiv论文引用生成器

一个简单易用的工具，用于批量生成arXiv论文的引用格式。支持多种引用样式，包括APA、MLA、Chicago和IEEE格式。

## 功能特点

- 批量处理多个arXiv ID
- 支持多种引用格式（APA、MLA、Chicago、IEEE）
- 可选的引用编号功能
- 友好的Web界面
- 一键复制生成的引用
- 错误处理和提示

## 安装说明

1. 克隆仓库：
```bash
git clone https://github.com/zjrwtx/arxiv_citation_gentools.git
cd arxiv_citation_gentools
```

2. 安装依赖：
```bash
pip install gradio requests
```

## 使用方法

1. 运行应用：
```bash
python app.py
```

2. 在浏览器中打开显示的本地URL（通常是 http://127.0.0.1:7860）

3. 使用方式：
   - 在文本框中输入arXiv ID（每行一个）
   - 选择所需的引用格式
   - 选择是否添加引用编号
   - 点击提交按钮生成引用

## 示例输入

```
2301.12345
2302.54321
```

## 支持的引用格式

- **APA** (American Psychological Association)
- **MLA** (Modern Language Association)
- **Chicago**
- **IEEE** (Institute of Electrical and Electronics Engineers)

## 错误处理

- 程序会检查arXiv ID的有效性
- 对于无效或不存在的ID，会显示相应的错误信息
- 网络连接问题会有适当的错误提示

## 依赖项

- Python 3.6+
- gradio
- requests

## 许可证

本项目基于MIT许可证开源。

## 贡献

欢迎提交问题和改进建议！如果您想贡献代码：

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 推送到您的分支
5. 创建Pull Request

## 联系方式

如有问题或建议，请通过GitHub Issues联系我们。
