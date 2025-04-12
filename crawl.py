import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CrawlMCPServer")

@mcp.tool()
def crawl_left_press(date: str) -> str:
    """
    Naver 진보 언론사 랭킹 크롤링
    Args:
        date (str): 날짜 (YYYYMMDD)
    Returns:
        str: 크롤링 결과
    """
    # 언론사 ID 리스트 (프레시안==002, 한겨레==028, 경향==032)
    press_ids = ["002", "028", "032"]  # 추가 가능
    
    results = []
    for press_id in press_ids:
        results.append(f"\n🔍 언론사 ID: {press_id}")
        
        url = f"https://media.naver.com/press/{press_id}/ranking?type=section&date={date}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 정치 섹션 찾기
        politics_section = None
        sections = soup.select("div.press_ranking_box.is_section")

        for section in sections:
            title_tag = section.select_one("strong.press_ranking_tit")
            if title_tag and title_tag.text.strip() == "정치":
                politics_section = section
                break

        # 정치 기사 추출
        if politics_section:
            articles = politics_section.select("ul.press_ranking_list > li")
            for idx, article in enumerate(articles[:3], start=1):  # 상위 3개만
                a_tag = article.select_one("a")
                if a_tag:
                    title = a_tag.select_one("strong.list_title").text.strip()
                    link = a_tag["href"]
                    results.append(f"{idx}위: {title}")
                    results.append(f"URL: {link}\n")
        else:
            results.append("⚠️ 정치 섹션을 찾을 수 없습니다.")
    
    return "\n".join(results)

@mcp.tool()
def crawl_right_press(date: str) -> str:
    """
    Naver 진보 언론사 랭킹 크롤링
    Args:
        date (str): 날짜 (YYYYMMDD)
    Returns:
        str: 크롤링 결과
    """
    # 언론사 ID 리스트 (동아==020, 조선==023, 중앙==025)
    press_ids = ["020", "023", "025"]  # 추가 가능
    
    results = []
    for press_id in press_ids:
        results.append(f"\n🔍 언론사 ID: {press_id}")
        
        url = f"https://media.naver.com/press/{press_id}/ranking?type=section&date={date}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 정치 섹션 찾기
        politics_section = None
        sections = soup.select("div.press_ranking_box.is_section")

        for section in sections:
            title_tag = section.select_one("strong.press_ranking_tit")
            if title_tag and title_tag.text.strip() == "정치":
                politics_section = section
                break

        # 정치 기사 추출
        if politics_section:
            articles = politics_section.select("ul.press_ranking_list > li")
            for idx, article in enumerate(articles[:3], start=1):  # 상위 3개만
                a_tag = article.select_one("a")
                if a_tag:
                    title = a_tag.select_one("strong.list_title").text.strip()
                    link = a_tag["href"]
                    results.append(f"{idx}위: {title}")
                    results.append(f"URL: {link}\n")
        else:
            results.append("⚠️ 정치 섹션을 찾을 수 없습니다.")
    
    return "\n".join(results)

# 아래 코드는 직접 실행 시 테스트를 위한 코드입니다
if __name__ == "__main__":
    mcp.run()