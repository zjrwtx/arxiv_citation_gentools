
import requests
import re

def get_arxiv_metadata(arxiv_id):
    # 检查arXiv ID格式
    if not re.match(r'^\d{4}\.\d{4,5}(v\d+)?$', arxiv_id):
        raise ValueError("请输入有效的arXiv编号，例如：2301.12345")
    
    # 构建API请求URL
    url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("无法从arXiv获取数据，请检查网络连接和arXiv编号。")
    
    # 解析XML响应
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.text)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    entry = root.find('atom:entry', ns)
    if entry is None:
        raise Exception("未找到该arXiv编号的论文信息。")
    
    # 获取论文标题
    title = entry.find('atom:title', ns).text.strip()
    
    # 获取作者列表
    authors = entry.findall('atom:author/atom:name', ns)
    author_names = [author.text.strip() for author in authors]
    
    # 获取出版年份（使用发表日期的年份）
    published = entry.find('atom:published', ns).text
    year = published[:4]
    
    # 获取版本号
    arxiv_url = entry.find('atom:id', ns).text
    version_search = re.search(r'v(\d+)$', arxiv_url)
    version = version_search.group(0) if version_search else ''
    
    # 返回元数据
    metadata = {
        'title': title,
        'authors': author_names,
        'year': year,
        'arxiv_id': arxiv_id,
        'version': version
    }
    return metadata

def format_citation(metadata, style='APA'):
    authors = metadata['authors']
    title = metadata['title']
    arxiv_id = metadata['arxiv_id']
    version = metadata['version']
    year = metadata['year']
    
    # 处理作者姓名格式
    if style.upper() == 'APA':
        formatted_authors = ', '.join(authors)
        citation = f"{formatted_authors}. ({year}). {title}. *arXiv*预印本arXiv:{arxiv_id}{version}"
    elif style.upper() == 'MLA':
        formatted_authors = '、'.join(authors)
        citation = f"{formatted_authors}。《{title}》。*arXiv*预印本 arXiv:{arxiv_id}{version} ({year})。"
    elif style.upper() == 'CHICAGO':
        formatted_authors = ', '.join(authors)
        citation = f"{formatted_authors}。“{title}。” *arXiv*预印本 arXiv:{arxiv_id}{version}，{year}。"
    elif style.upper() == 'IEEE':
        # IEEE风格通常使用英文名，需要将中文名转为拼音或使用英文名
        formatted_authors = ' and '.join(authors)
        citation = f"{formatted_authors}, \"{title},\" *arXiv* preprint arXiv:{arxiv_id}{version}, {year}."
    else:
        raise ValueError("不支持的引用格式。请选择APA、MLA、Chicago或IEEE。")
    
    return citation

def main():
    arxiv_id = input("请输入arXiv编号（例如2301.12345）：").strip()
    style = input("请输入引用格式（APA、MLA、Chicago、IEEE）：").strip()
    
    try:
        metadata = get_arxiv_metadata(arxiv_id)
        citation = format_citation(metadata, style)
        print("\n生成的引用：\n")
        print(citation)
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == '__main__':
    main()