import os
import re
import json

PROJECT_DIR = r"c:\Users\ASUS\.antigravity\2)_내_스타로프_애드센스_프로젝트\7)_정부지원금_복지정책"
POSTS_DIR = os.path.join(PROJECT_DIR, "posts")
TEMPLATE_PATH = os.path.join(POSTS_DIR, "post-template.html")
SCHEDULE_PATH = os.path.join(PROJECT_DIR, "schedule.json")
DOMAIN = "https://blog7.starrope2023.com"

AUTHOR_BOX_HTML = """      <!-- Author Profile Box (Alphanahm Skill) -->
      <div class="author-box" style="margin-top: 50px; padding: 24px; border: 1px solid var(--border-light); border-radius: var(--border-radius-md); display: flex; align-items: center; gap: 20px; background: rgba(255, 255, 255, 0.02); margin-bottom: 20px;">
        <div style="font-size: 28px; background: linear-gradient(135deg, var(--primary-color), hsl(265, 90%, 60%)); width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; flex-shrink: 0; box-shadow: 0 4px 12px hsla(var(--hue), 95%, 48%, 0.2);">✍️</div>
        <div>
          <h5 style="margin: 0; font-size: 15.5px; font-weight: 700; color: var(--text-main);">스타로프 지원금 에디터</h5>
          <p style="margin: 6px 0 0 0; font-size: 13.5px; color: var(--text-muted); line-height: 1.5;">정부 지원정책 가이드 에디터. 청년, 소상공인, 서민층을 위한 각종 지원금 신청 자격, 구비 서류, 그리고 놓치기 쉬운 국가 복지 혜택을 실시간으로 안내합니다.</p>
        </div>
      </div>
"""

NEW_POSTS_DATA = {
    "unemployment-benefit-apply.html": {
        "title": "2026년 실업급여 조건 및 신청방법 지급액 상하한액 계산 총정리",
        "description": "2026년 최저임금 인상(10,320원)에 따라 7년 만에 상향 조정된 실업급여(구직급여)의 1일 상한액(68,100원) 및 하한액, 비자발적 퇴사 등 수급 자격 요건, 온라인/모바일 신청 절차와 최근 강화된 반복 수급자 제재 및 감액 기준까지 한눈에 알기 쉽게 총정리해 드립니다.",
        "category": "정부지원금",
        "image_url": "https://images.unsplash.com/photo-1521791136368-1a4682773d1a?auto=format&fit=crop&w=800&q=80",
        "table": [
            ("구분", "2026년 실업급여(구직급여) 개편 핵심"),
            ("신청 자격", "이직일 이전 18개월간 고용보험 가입일 180일 이상 & 비자발적 퇴사"),
            ("1일 상한액", "68,100원 (2025년 66,000원에서 2,100원 인상)"),
            ("1일 하한액", "66,048원 (1일 8시간 근무 기준, 최저임금의 80%)"),
            ("신청 기한", "퇴직일로부터 12개월(1년) 이내 (기간 경과 시 소멸)")
        ],
        "faq": [
            ("자발적으로 사표를 냈는데 실업급여를 받을 수 있는 방법이 있나요?", "원칙적으로는 불가능하지만, 임금체불(2개월 이상), 주거지 이전 등으로 왕복 통근이 3시간 이상 소요되는 경우, 직장 내 괴롭힘, 질병으로 인한 근로 곤란 등 정당한 사유가 입증되면 비자발적 퇴사로 인정받아 신청할 수 있습니다."),
            ("퇴사 후 언제까지 신청해야 하나요?", "퇴직한 다음 날부터 12개월(1년) 이내에 신청해야 합니다. 12개월이 지나면 소급 지급이 불가능하므로, 퇴사 후 바로 고용센터를 방문하거나 고용24를 통해 신청하는 것이 좋습니다."),
            ("실업급여를 받는 동안 아르바이트를 하거나 소득이 발생하면 어떻게 되나요?", "실업급여 수급 기간 중 일시적인 알바나 근로 소득이 발생하면 반드시 실업인정 신청 시 신고해야 합니다. 신고하지 않을 경우 부정수급으로 간주되어 급여 반환 및 배액 징수, 형사처벌 등의 불이익을 받을 수 있습니다."),
            ("이직확인서와 피보험자격 상실신고서는 언제 처리되나요?", "원칙적으로 퇴사 후 사업주가 고용노동부에 제출해야 합니다. 처리가 지연될 경우 이전 회사에 요청하거나 관할 고용센터에 문의하여 처리를 촉구할 수 있습니다.")
        ],
        "content": """
      <p>실직은 누구에게나 갑작스럽고 당혹스러운 상황입니다. 이때 구직자의 생계 안정을 돕고 재취업을 지원하는 가장 중요한 안전망이 바로 <strong>실업급여(구직급여)</strong>입니다. 특히 <strong>2026년에는 최저임금 인상(10,320원)</strong>과 함께 실업급여의 상한액 및 하한액 기준이 7년 만에 상향 조정되었으며, 부정수급 및 반복수급에 대한 제재도 대폭 강화되었습니다. 이번 글에서는 2026년 개정된 실업급여의 자격 요건, 금액 계산법, 모바일 신청 방법까지 한 번에 정리해 드립니다.</p>
      
      <h2>1. 2026년 실업급여 수급 자격 요건</h2>
      <p>실업급여를 받기 위해서는 고용보험법에 규정된 몇 가지 핵심 요건을 반드시 충족해야 합니다. 대략적인 기준이 아닌 법적 기준이므로 꼼꼼하게 확인해 보셔야 합니다.</p>
      <ul>
        <li><strong>피보험 단위기간 180일 이상:</strong> 퇴사일(이직일) 이전 18개월 동안 고용보험에 가입된 기간(주휴일 및 유급휴일 포함)이 <strong>통산 180일 이상</strong>이어야 합니다. 단순 근무일이 아닌 유급으로 처리된 날만 합산되므로 실제 일한 기간은 약 7~8개월 이상이어야 안전합니다.</li>
        <li><strong>비자발적인 퇴사 사유:</strong> 경영상 해고, 권고사직, 계약 만료, 정년퇴직, 회사 폐업 등 <strong>근로자 본인의 의사와 상관없이 직장을 잃은 경우</strong>여야 합니다.</li>
        <li><strong>재취업 노력의 의사:</strong> 일할 의사와 능력이 있음에도 불구하고 취업하지 못한 상태여야 하며, 고용센터가 요구하는 적극적인 구직 활동을 성실히 수행해야 합니다.</li>
      </ul>
      
      <blockquote>
        "개인 사정으로 자발적 사직서를 썼더라도 임금체불(2개월 이상), 직장 내 괴롭힘, 종교적 차별, 회사의 원거리 이전으로 왕복 출퇴근이 3시간 이상 소요되는 경우 등 법이 인정하는 '정당한 사유'가 입증된다면 실업급여 수급이 가능합니다."
      </blockquote>

      <h2>2. 2026년 실업급여 지급액 및 상한액·하한액 기준</h2>
      <p>내가 받을 수 있는 실업급여액은 퇴사 전 평균 임금의 60%를 기준으로 하루치 금액을 산정합니다. 다만, 지급액의 급격한 격차를 방지하기 위해 <strong>일일 상한액과 하한액</strong>이 정해져 있습니다.</p>
      
      <h3>① 1일 상한액 (최대 지급액)</h3>
      <p>2026년부터 실업급여 1일 상한액이 <strong>68,100원</strong>으로 인상되었습니다. 기존 66,000원에서 2,100원 상향 조정되어, 한 달(30일) 최대 수령액은 <strong>2,043,000원</strong>입니다.</p>
      
      <h3>② 1일 하한액 (최소 지급액)</h3>
      <p>실업급여 하한액은 최저임금법상 최저임금의 80%로 규정되어 있습니다. 2026년 최저임금(시급 10,320원)의 80%에 해당하는 금액으로, 1일 8시간 근무 기준 <strong>66,048원</strong>이 적용됩니다. 한 달(30일) 최소 수령액은 <strong>1,981,440원</strong>입니다.</p>
      
      <h3>③ 지급 기간</h3>
      <p>고용보험 가입 기간과 퇴사 당시의 연령에 따라 최소 120일(4개월)에서 <strong>최대 270일(9개월)</strong> 동안 실업급여를 수령할 수 있습니다.</p>

      <h2>3. 5년 내 3회 이상 반복 수급자 제재 규정</h2>
      <p>2026년 실업급여 제도의 가장 큰 변화 중 하나는 '반복 수급자'에 대한 제재 강화입니다. 단기 취업과 실업급여 수령을 반복하는 도덕적 해이를 막기 위한 조치입니다.</p>
      <ul>
        <li><strong>급여액 감액 조치:</strong> 최근 5년 동안 실업급여를 3회 이상 받은 경우 세 번째 수급 시점부터 횟수에 따라 실업급여액이 <strong>10%에서 최대 50%까지 삭감</strong>됩니다.</li>
        <li><strong>대기기간 연장:</strong> 실업급여 신청 후 급여가 지급되지 않는 대기기간이 기존 7일에서 <strong>최대 4주일</strong>로 연장됩니다.</li>
        <li><strong>구직활동 의무 강화:</strong> 반복 수급자는 일반 수급자보다 구직활동 인정 주기가 짧아지며, 어학 공부나 자격증 취득 등 단순 훈련 외에 실제 입사지원서 제출 등의 면접 활동만 인정받을 수 있습니다.</li>
      </ul>

      <h2>4. 모바일 및 온라인 신청 절차 (4단계)</h2>
      <p>실업급여 신청은 퇴사 후 <strong>12개월(1년) 이내</strong>에 마쳐야 하며, 기간이 지나면 남은 소정급여일수가 있어도 더 이상 수령할 수 없으므로 지체 없이 신청하셔야 합니다.</p>
      <ol>
        <li><strong>이직확인서 및 상실신고 확인:</strong> 전 직장에서 근로복지공단에 고용보험 피보험자격 상실신고서와 고용센터에 이직확인서를 제출했는지 '고용24' 또는 근로복지공단 웹사이트에서 확인합니다.</li>
        <li><strong>워크넷(Worknet) 구직등록:</strong> [워크넷 공식 사이트]에 접속하여 회원가입 후 이력서를 작성하고 '구직신청'을 완료합니다.</li>
        <li><strong>수급자격 온라인 교육 이수:</strong> [고용24 홈페이지] 또는 모바일 앱에 로그인한 후 '수급자격 신청자 온라인 교육'을 시청합니다. (교육 시작 후 14일 이내에 고용센터를 방문해야 함)</li>
        <li><strong>관할 고용센터 방문 및 수급자격 신청:</strong> 신분증을 지참하고 주민등록상 주소지의 관할 고용복지플러스센터에 직접 방문하여 실업급여 수급자격 인정 신청서를 제출합니다.</li>
      </ol>
        """
    }
}

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = text.strip()
    return text

def extract_headings_and_paragraphs(html_content):
    h2_pattern = re.compile(r'<h2>(.*?)</h2>', re.DOTALL)
    headings = []
    
    for match in h2_pattern.finditer(html_content):
        h_text = clean_text(match.group(1))
        h_clean = re.sub(r'^\d+\.\s*', '', h_text).strip()
        headings.append((match.start(), match.end(), h_clean))
        
    faqs = []
    for i in range(len(headings)):
        h_start, h_end, h_title = headings[i]
        if h_title.lower() in ["결론", "conclusion", "맺음말", "마치며", "결론 및 의견"]:
            continue
            
        next_pos = headings[i+1][0] if i+1 < len(headings) else len(html_content)
        sub_section = html_content[h_end:next_pos]
        
        p_match = re.search(r'<p>(.*?)</p>', sub_section, re.DOTALL)
        if p_match:
            p_text = clean_text(p_match.group(1))
            if len(p_text) > 30:
                q_text = h_title
                if not q_text.endswith("?"):
                     q_text += "의 핵심 내용은 무엇인가요?"
                faqs.append((q_text, p_text[:200] + ("..." if len(p_text) > 200 else "")))
                
        if len(faqs) >= 3:
            break
            
    return headings, faqs

def build_table_html(title, desc, rows):
    html = """      <!-- Key Summary Table (Alphanahm Skill) -->
      <div class="summary-table-container" style="margin: 30px 0;">
        <table style="width: 100%; border-collapse: collapse; border: 1px solid var(--border-light); font-size: 14.5px; background-color: var(--bg-surface);">
          <thead>
            <tr style="background-color: var(--bg-ad); border-bottom: 1px solid var(--border-light);">
              <th style="padding: 12px 16px; border-right: 1px solid var(--border-light); text-align: left; font-weight: 700; color: var(--text-main);">핵심 영역</th>
              <th style="padding: 12px 16px; text-align: left; font-weight: 700; color: var(--text-main);">상세 가이드 & 실전 가치</th>
            </tr>
          </thead>
          <tbody>"""
          
    short_title = title.split(":")[0].strip()
    html += f"""
            <tr style="border-bottom: 1px solid var(--border-light);">
              <td style="padding: 12px 16px; border-right: 1px solid var(--border-light); font-weight: 600; color: var(--primary-color);">주요 목표</td>
              <td style="padding: 12px 16px; color: var(--text-main);">{short_title}를 위한 핵심 전략 및 기초 이론 수립</td>
            </tr>"""

    if rows and all(isinstance(row, tuple) and len(row) >= 2 for row in rows):
        for row in rows:
            key = clean_text(str(row[0]))
            value = clean_text(str(row[1]))
            html += f"""
            <tr style="border-bottom: 1px solid var(--border-light);">
              <td style="padding: 12px 16px; border-right: 1px solid var(--border-light); font-weight: 600; color: var(--primary-color);">{key}</td>
              <td style="padding: 12px 16px; color: var(--text-main);">{value}</td>
            </tr>"""
        html += """
          </tbody>
        </table>
      </div>"""
        return html

    if len(rows) > 0:
        h_name = rows[0][2] if isinstance(rows[0], tuple) and len(rows[0]) > 2 else rows[0]
        html += f"""
            <tr style="border-bottom: 1px solid var(--border-light);">
              <td style="padding: 12px 16px; border-right: 1px solid var(--border-light); font-weight: 600; color: var(--primary-color);">실전 분석</td>
              <td style="padding: 12px 16px; color: var(--text-main);">{h_name} 단계별 구현 가이드 및 세부 실행 방안</td>
            </tr>"""
            
    if len(rows) > 1:
        h_name = rows[1][2] if isinstance(rows[1], tuple) and len(rows[1]) > 2 else rows[1]
        html += f"""
            <tr>
              <td style="padding: 12px 16px; border-right: 1px solid var(--border-light); font-weight: 600; color: var(--primary-color);">최적화 팁</td>
              <td style="padding: 12px 16px; color: var(--text-main);">{h_name} 적용을 통한 성능 고도화 및 리스크 예방</td>
            </tr>"""
    else:
        html += """
            <tr>
              <td style="padding: 12px 16px; border-right: 1px solid var(--border-light); font-weight: 600; color: var(--primary-color);">기대 가치</td>
              <td style="padding: 12px 16px; color: var(--text-main);">정부 복지 혜택 및 수령액 극대화 달성</td>
            </tr>"""
            
    html += """
          </tbody>
        </table>
      </div>"""
    return html

def build_faq_html(faqs):
    if not faqs:
        faqs = [
            ("본 가이드의 핵심 요약은 무엇인가요?", "정부 지원정책과 복지 혜택의 자격 요건을 파악하고, 놓치는 혜택이 없도록 온라인/방문 신청을 돕기 위해 실전 가이드를 제공합니다."),
            ("신청 및 실행 시 주의해야 할 점은 무엇인가요?", "정부 정책은 수시로 세부 기준이 변동되거나 예산 상황에 따라 마감될 수 있으므로, 신청 전 공식 포털(정부24, 복지로, 고용24 등)의 최신 소식을 확인하는 것이 좋습니다."),
            ("추가적인 개별 상담과 질문은 어디에 해야 하나요?", "각 제도 설명 하단에 명시된 소관 고용센터, 보건복지상담센터(129), 고용노동부 고객상담센터(1350) 등 담당 전문 기관에 전화로 문의하시면 상세히 답변받으실 수 있습니다.")
        ]
        
    html = """      <!-- FAQ Section (Alphanahm Skill) -->
      <div class="faq-section" style="margin-top: 40px; border-top: 1px solid var(--border-light); padding-top: 30px; margin-bottom: 30px;">
        <h3 style="font-size: 20px; margin-bottom: 20px; color: var(--text-main);">❓ 자주 묻는 질문 (FAQ)</h3>"""
    for q, a in faqs:
        html += f"""
        <details style="margin-bottom: 16px; padding: 16px; background-color: var(--bg-main); border: 1px solid var(--border-light); border-radius: var(--border-radius-sm); cursor: pointer;">
          <summary style="font-weight: 600; font-size: 15px; color: var(--text-main); outline: none;">{q}</summary>
          <p style="margin-top: 12px; margin-bottom: 0; font-size: 14.5px; color: var(--text-muted); line-height: 1.6;">{a}</p>
        </details>"""
    html += """
      </div>"""
    return html

def create_new_html(filename, data):
    filepath = os.path.join(POSTS_DIR, filename)
    if os.path.exists(filepath):
        print(f"[INFO] File already exists, skipping: {filename}")
        return False
        
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
        
    publish_date = ""
    date_display_clean = ""
    
    with open(SCHEDULE_PATH, 'r', encoding='utf-8') as f:
        schedule = json.load(f)
        for p in schedule['posts']:
            if p['filename'] == filename:
                publish_date = p['publish_date']
                date_display_clean = p['date_display']
                break
                
    if not publish_date:
        print(f"[ERROR] Could not find metadata for {filename} in schedule.json")
        return False
        
    title = data['title']
    desc = data['description']
    tag = data['category']
    img_url = data['image_url']
    
    json_ld = f"""  <!-- JSON-LD Structured Data (Alphanahm Skill) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{desc}",
    "image": "{img_url}",
    "author": {{ "@type": "Person", "name": "Starrope" }},
    "publisher": {{ "@type": "Organization", "name": "스타로프 지원금", "url": "{DOMAIN}" }},
    "datePublished": "{publish_date}",
    "dateModified": "{publish_date}",
    "url": "{DOMAIN}/posts/{filename}",
    "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{DOMAIN}/posts/{filename}" }}
  }}
  </script>"""

    html = template.replace("<title>[포스트 제목 입력] | 정부 지원금 & 복지정책 가이드 | 스타로프</title>", f"<title>{title} | 정부 지원금 & 복지정책 가이드 | 스타로프</title>")
    html = html.replace('<meta name="description" content="[여기에 검색 노출용 글 요약 설명 입력 - 약 80자 내외]">', f'<meta name="description" content="{desc}">')
    
    # Insert JSON-LD and tags into <head>
    head_pos = html.find("<head>")
    if head_pos != -1:
        insert_tags = f"""\n{json_ld}
  <meta name="keywords" content="{tag.replace(' / ', ', ')}, 정부지원금, 복지정책, 보조금24, 소상공인지원, 청년혜택, 스타로프">
  <meta name="author" content="Starrope">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{DOMAIN}/posts/{filename}">"""
        html = html[:head_pos + 6] + insert_tags + html[head_pos + 6:]
        
    html = html.replace("[카테고리명]", tag)
    html = html.replace("[여기에 포스트 메인 대제목을 입력하세요]", title)
    html = html.replace("2026. 05. 30", date_display_clean)
    
    table_html = build_table_html(title, desc, data.get("table", []))
    faq_html = build_faq_html(data.get("faq", []))
      
    body_html = f"""
      <img src="{img_url}" alt="{title}" style="width:100%; border-radius:12px; margin-bottom:32px; box-shadow:var(--shadow-md);">
      
      {table_html}
      
      {data['content']}
      
      <ins class="adsbygoogle ad-slot ad-content"
           style="display:block; text-align:center;"
           data-ad-layout="in-article"
           data-ad-format="fluid"
           data-ad-client="ca-pub-1692428092138510"
           data-ad-slot="5566778899">
        <div class="ad-slot-label">본문 중간 인피드 광고 영역</div>
      </ins>
      
      <!-- HIGH-CONVERTING REDIRECT CTA BOX -->
      <div class="redirect-box" style="margin-top: 40px;">
        <h3 class="redirect-title" style="border: none; padding: 0; margin-bottom: 8px;">📍 실업급여 고용24 공식 신청 페이지 바로가기</h3>
        <p class="redirect-desc">
          아래 버튼을 클릭하시면 고용노동부 고용24 공식 웹사이트로 즉시 이동하여 온라인 신청을 진행하실 수 있습니다.<br>
          (이동 시 1~2초간 데이터 보안성 점검 로딩이 진행될 수 있습니다.)
        </p>
        <a href="../apply.html?target=https://www.work24.go.kr" class="redirect-cta-btn" target="_blank" rel="noopener">
          고용24 공식 홈페이지 바로가기
          <svg xmlns="http://www.w3.org/2000/svg" style="width: 18px; height: 18px;" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 5l7 7-7 7M5 5l7 7-7 7" />
          </svg>
        </a>
      </div>
      
      {faq_html}
      
      {AUTHOR_BOX_HTML}
"""
    
    start_tag = '<article class="post-content">'
    end_tag = '</article>'
    
    start_idx = html.find(start_tag)
    end_idx = html.find(end_tag, start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print(f"[ERROR] Could not find article content block tags in template for {filename}")
        return False
        
    html = html[:start_idx + len(start_tag)] + body_html + html[end_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"[SUCCESS] Created new HTML: {filename}")
    return True

def update_schedule_json():
    with open(SCHEDULE_PATH, 'r', encoding='utf-8') as f:
        schedule = json.load(f)
        
    existing_filenames = {p['filename'] for p in schedule['posts']}
    
    if "unemployment-benefit-apply.html" not in existing_filenames:
        entry = {
            "filename": "unemployment-benefit-apply.html",
            "title": NEW_POSTS_DATA["unemployment-benefit-apply.html"]["title"],
            "description": NEW_POSTS_DATA["unemployment-benefit-apply.html"]["description"],
            "image_url": NEW_POSTS_DATA["unemployment-benefit-apply.html"]["image_url"],
            "tag": NEW_POSTS_DATA["unemployment-benefit-apply.html"]["category"],
            "date_display": "2026.06.23",
            "publish_date": "2026-06-23",
            "publish_time": "22:00"
        }
        schedule['posts'].append(entry)
        with open(SCHEDULE_PATH, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, indent=2, ensure_ascii=False)
        print("[SUCCESS] schedule.json updated for unemployment-benefit-apply.html")
    else:
        print("[INFO] Post unemployment-benefit-apply.html already exists in schedule.json")

def process_file(filepath):
    filename = os.path.basename(filepath)
    if filename == "post-template.html":
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "summary-table-container" in content or "faq-section" in content or "application/ld+json" in content:
        print(f"[INFO] Already processed or skips: {filename}")
        return False
        
    title_match = re.search(r'<title>(.*?)</title>', content)
    if not title_match:
        print(f"[WARN] No title found in {filename}")
        return False
    full_title = clean_text(title_match.group(1)).split(" | ")[0]
    
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content)
    if not desc_match:
        desc_match = re.search(r'<meta\s+property="og:description"\s+content="(.*?)"', content)
    desc = clean_text(desc_match.group(1)) if desc_match else full_title
    
    tag_match = re.search(r'<div class="post-header-tag">(.*?)</div>', content)
    tag = clean_text(tag_match.group(1)) if tag_match else "정부지원금"
    
    date_match = re.search(r'<span>\s*(\d{4}\.\s*\d{2}\.\s*\d{2})\s*</span>', content)
    date_display = date_match.group(1) if date_match else "2026. 06. 22"
    date_clean = date_display.replace(". ", "-").replace(".", "-").strip()
    if len(date_clean) < 10:
        date_clean = "2026-06-22"
        
    img_match = re.search(r'<img\s+src="(.*?)"', content)
    img_url = img_match.group(1) if img_match else "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=800&q=80"
    
    headings, faqs = extract_headings_and_paragraphs(content)
    
    json_ld = f"""  <!-- JSON-LD Structured Data (Alphanahm Skill) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{full_title}",
    "description": "{desc}",
    "image": "{img_url}",
    "author": {{ "@type": "Person", "name": "Starrope" }},
    "publisher": {{ "@type": "Organization", "name": "스타로프 지원금", "url": "{DOMAIN}" }},
    "datePublished": "{date_clean}",
    "dateModified": "{date_clean}",
    "url": "{DOMAIN}/posts/{filename}",
    "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{DOMAIN}/posts/{filename}" }}
  }}
  </script>
  <meta name="keywords" content="{tag.replace(' / ', ', ')}, 정부지원금, 복지정책, 보조금24, 소상공인지원, 청년혜택, 스타로프">
  <meta name="author" content="Starrope">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{DOMAIN}/posts/{filename}">"""

    head_pos = content.find("<head>")
    if head_pos != -1:
        content = content[:head_pos + 6] + "\n" + json_ld + content[head_pos + 6:]
        
    pc_start = content.find('<article class="post-content">')
    if pc_start == -1:
        print(f"[ERROR] Could not find post-content in {filename}")
        return False
        
    img_tag_pos = content.find('<img ', pc_start, pc_start + 1000)
    insert_pos = -1
    if img_tag_pos != -1:
        img_tag_end = content.find('>', img_tag_pos)
        if img_tag_end != -1:
            insert_pos = img_tag_end + 1
            
    if insert_pos == -1:
        first_p_end = content.find('</p>', pc_start)
        if first_p_end != -1:
            insert_pos = first_p_end + 4
            
    if insert_pos == -1:
        print(f"[ERROR] Could not find table insertion point in {filename}")
        return False
        
    table_html = build_table_html(full_title, desc, headings)
    content = content[:insert_pos] + "\n" + table_html + content[insert_pos:]
    
    article_close = content.find('</article>', pc_start + len(table_html))
    if article_close == -1:
        print(f"[ERROR] Could not find closing article tag in {filename}")
        return False
        
    faq_html = build_faq_html(faqs)
    inserted_blocks = "\n" + faq_html + "\n" + AUTHOR_BOX_HTML
    content = content[:article_close] + inserted_blocks + content[article_close:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[SUCCESS] Upgraded {filename}")
    return True

def main():
    print("Starting Blog 7 updates...")
    if not os.path.exists(POSTS_DIR):
        print(f"[INFO] Posts directory does not exist yet: {POSTS_DIR}")
        return
        
    update_schedule_json()
    
    for filename, data in NEW_POSTS_DATA.items():
        create_new_html(filename, data)
        
    files = [os.path.join(POSTS_DIR, f) for f in os.listdir(POSTS_DIR) if f.endswith(".html") and f != "post-template.html" and f not in NEW_POSTS_DATA.keys()]
    count = 0
    for f in files:
        if process_file(f):
            count += 1
    print(f"Blog 7 updates complete! Total existing upgraded: {count}/{len(files)}")

if __name__ == "__main__":
    main()
