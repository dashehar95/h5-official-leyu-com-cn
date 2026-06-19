import json
from datetime import datetime

SITES = [
    {
        "name": "乐鱼体育",
        "url": "https://h5-official-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育平台", "在线体育", "赛事资讯"],
        "tags": ["体育", "资讯", "娱乐"],
        "description": "乐鱼体育提供丰富的体育赛事资讯与互动体验，是体育爱好者的首选平台。",
        "created": "2024-01-15"
    },
    {
        "name": "乐鱼电竞",
        "url": "https://h5-official-leyu.com.cn/esports",
        "keywords": ["电竞", "乐鱼电竞", "电子竞技", "赛事直播"],
        "tags": ["电竞", "直播", "竞技"],
        "description": "乐鱼电竞覆盖主流电竞赛事，提供实时比分、赛程与深度分析。",
        "created": "2024-03-01"
    },
    {
        "name": "乐鱼彩票",
        "url": "https://h5-official-leyu.com.cn/lottery",
        "keywords": ["彩票", "乐鱼彩票", "数字彩", "竞彩"],
        "tags": ["彩票", "游戏", "博彩"],
        "description": "乐鱼彩票提供多种数字彩与竞彩玩法，安全合规，开奖快速。",
        "created": "2024-05-20"
    },
    {
        "name": "乐鱼棋牌",
        "url": "https://h5-official-leyu.com.cn/chess",
        "keywords": ["棋牌", "乐鱼棋牌", "扑克", "麻将", "棋牌游戏"],
        "tags": ["棋牌", "牌类", "休闲"],
        "description": "乐鱼棋牌集合经典棋牌游戏，界面精美，公平竞技。",
        "created": "2024-07-10"
    }
]


def compute_summary_rating(site: dict) -> float:
    """根据关键词数量和描述长度计算一个简单的评分（仅供演示）。"""
    kw_count = len(site.get("keywords", []))
    desc_len = len(site.get("description", ""))
    return round(kw_count * 1.5 + desc_len * 0.1, 2)


def format_site_summary(site: dict, index: int) -> str:
    """格式化单个站点的摘要文本。"""
    rating = compute_summary_rating(site)
    lines = [
        f"站点 #{index}",
        f"名称    : {site['name']}",
        f"URL     : {site['url']}",
        f"关键词  : {', '.join(site['keywords'])}",
        f"标签    : {', '.join(site['tags'])}",
        f"描述    : {site['description']}",
        f"创建日期: {site['created']}",
        f"摘要评分: {rating}",
        "-" * 40
    ]
    return "\n".join(lines)


def build_summary_report(sites: list) -> str:
    """构建所有站点摘要报告。"""
    header = f"站点摘要报告 - 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    sep = "=" * 50
    parts = [header, sep]
    for idx, site in enumerate(sites, start=1):
        parts.append(format_site_summary(site, idx))
    parts.append(f"共 {len(sites)} 个站点")
    return "\n".join(parts)


def save_summary_to_file(report: str, filename: str = "site_summary.txt") -> bool:
    """将摘要报告保存到文件，返回是否成功。"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        return True
    except IOError as err:
        print(f"[错误] 写入文件失败: {err}")
        return False


def main():
    print("正在生成站点摘要...")
    report = build_summary_report(SITES)
    print(report)
    if save_summary_to_file(report):
        print(f"\n摘要已保存至 site_summary.txt")
    else:
        print("\n摘要未保存至文件，仅输出到控制台。")


if __name__ == "__main__":
    main()