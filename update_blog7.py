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
    "small-business-support-grant-2026.html": {
        "title": "2026년 소상공인 저금리 대출 및 경영안정지원금 신청자격 조건 신청방법 총정리",
        "description": "2026년 고금리와 경기 불황으로 어려움을 겪는 영세 자영업자 및 소상공인을 위한 최저 연 2.0%대 저금리 정부 정책자금 대출(경영안정자금), 대환대출 자격 조건, 지원 금액 한도, 그리고 소상공인시장진흥공단 온라인 신청 절차와 제출 서류까지 알기 쉽게 총정리해 드립니다.",
        "category": "소상공인 혜택",
        "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=800&q=80",
        "table": [
            ("지원 사업명", "2026년 소상공인 정책자금 (경영안정자금/대환대출)"),
            ("대출 금리", "최저 연 2.0% ~ 4.0%대 변동 또는 고정금리 (정책 우대금리 적용)"),
            ("대출 한도", "업체당 최대 7,000만 원 (일반경영안정자금 기준)"),
            ("상환 기간", "5년 (2년 거치, 3년 균등분할상환)"),
            ("주요 신청자격", "소상공인 보호 및 지원에 관한 법률상 소상공인 (상시근로자 5인/10인 미만)")
        ],
        "faq": [
            ("저신용 소상공인도 정책자금 대출을 신청할 수 있나요?", "네, 가능합니다. 신용평점(NICE 기준 744점 이하 등)이 낮은 저신용·취약 소상공인을 위한 전용 자금(소상공인 특화자금, 재도전특별자금 등)이 별도로 마련되어 있어 일반 시중은행 대출이 어려운 분들도 신청하실 수 있습니다."),
            ("대환대출은 어떤 정책인가요?", "고금리 대출(연 7% 이상)을 이용 중인 소상공인을 대상으로 최저 연 4.5% 수준의 저금리 장기 저리 융자로 전환해 주는 지원 정책입니다. 이자 부담을 획기적으로 낮출 수 있습니다."),
            ("법인 소상공인도 신청이 가능한가요?", "네, 개인사업자뿐만 아니라 상시 근로자 수 등 소상공인 기준을 충족하는 법인사업자도 신청 가능합니다. 다만, 법인의 경우 법인인감증명서 및 등기사항전부증명서 등의 추가 서류가 필요합니다."),
            ("연체 중이거나 세금 체납이 있어도 신청할 수 있나요?", "세금 체납, 금융기관 연체, 휴·폐업 중인 사업자는 원칙적으로 정책자금 지원 대상에서 제외됩니다. 단, 국세청 체납처분 유예를 받았거나 연체정보가 해제된 경우에는 신청이 가능할 수 있습니다.")
        ],
        "content": """
      <p>지속되는 고금리 기조와 내수 진작 부진으로 인해 많은 자영업자 및 소상공인분들이 자금난을 겪고 있습니다. 정부와 소상공인시장진흥공단은 이러한 영세 소상공인의 연쇄 부도를 막고 경영 안정을 돕기 위해 <strong>2026년 소상공인 정책자금 지원계획</strong>을 확정하고 대규모 융자 공급에 나섰습니다. 특히 올해는 <strong>연 2.0%~3.0%대의 초저금리 경영안정자금</strong>과 <strong>고금리 대환대출</strong>의 지원 요건을 대폭 완화하여 문턱을 낮췄습니다. 이번 글에서는 내가 받을 수 있는 2026년 소상공인 저금리 대출 조건부터 신청 방법까지 핵심만 명쾌하게 정리해 드립니다.</p>
      
      <h2>1. 2026년 소상공인 정책자금 핵심 분류 및 지원 한도</h2>
      <p>소상공인 정책자금은 크게 소진공에서 직접 대출해 주는 '직접대출'과 금융기관을 통하는 '대리대출'로 나뉩니다. 사업의 목적과 신용도에 따라 알맞은 자금을 선택해야 승인율을 높일 수 있습니다.</p>
      <ul>
        <li><strong>일반경영안정자금:</strong> 업력 1년 미만의 초기 소상공인이나 경영 애로를 겪는 자영업자를 위한 자금으로, <strong>업체당 최대 7,000만 원</strong>까지 지원됩니다.</li>
        <li><strong>소상공인 특화자금:</strong> 제조업을 영위하는 소공인(상시근로자 10인 미만)을 대상으로 기계설비 도입이나 원자재 구매 비용을 지원하며, <strong>최대 5억 원(운전자금 1억 원)</strong>까지 대출이 가능합니다.</li>
        <li><strong>대환대출 (고금리 대환):</strong> 제2금융권 등에서 연 7% 이상의 고금리 대출을 성실 상환 중인 소상공인에게 연 4.5% 고정금리 정책대출로 전환해 주며, <strong>최대 5,000만 원</strong> 한도로 지원합니다.</li>
        <li><strong>재도전특별자금:</strong> 폐업 후 재창업을 준비 중이거나 채무조정을 성실히 이행 중인 소상공인의 재기를 돕기 위한 특수 자금입니다.</li>
      </ul>
      
      <blockquote>
        "2026년 정책자금은 한정된 예산으로 운영되므로 매월 초(대체로 첫째 주 월요일) 접수 개시 후 며칠 이내에 선착순으로 마감되는 경향이 있습니다. 자금이 필요한 소상공인 분들은 미리 서류를 구비해 두고 접수 당일 신속하게 신청하셔야 합니다."
      </blockquote>

      <h2>2. 신청 자격 조건 (상시근로자 및 소상공인 기준)</h2>
      <p>아무리 혜택이 좋더라도 소상공인 법적 요건을 충족하지 못하면 신청이 불가능합니다. 아래 3가지 기본 조건을 체크해 보세요.</p>
      
      <h3>① 상시 근로자 수 기준</h3>
      <p>제조업, 건설업, 운수업, 광업은 <strong>상시 근로자 10인 미만</strong>이어야 하며, 도소매업, 서비스업, 음식점업 등 그 밖의 모든 업종은 <strong>상시 근로자 5인 미만</strong>(4인 이하)인 사업장만 소상공인으로 인정받습니다.</p>
      
      <h3>② 업종별 매출액 기준</h3>
      <p>중소기업기본법 시행령에 따른 연간 매출액이 업종별 기준(소매업 50억 원 이하, 음식점업 10억 원 이하 등) 이하인 소기업이어야 합니다.</p>
      
      <h3>③ 지원 제외 대상 업종</h3>
      <p>사행성 업종, 유흥업소, 부동산 임대 및 공급업, 전문 직종(변호사, 병원, 약국 등), 금융 및 보험업 등 일부 업종은 정부 지원금 및 정책자금 융자 대상에서 제외되므로 본인의 사업자등록증상 업종을 반드시 확인해야 합니다.</p>

      <h2>3. 2026년 대출 금리 및 상환 조건</h2>
      <p>2026년 소상공인 정책자금 금리는 분기별 정책금리에 가산금리를 합산하여 결정됩니다.</p>
      <ul>
        <li><strong>적용 금리:</strong> 기준금리(연 2.0% 내외)에 사업별 가산금리(0.2%~0.6%)가 더해져 최종 <strong>연 2.2% ~ 3.5% 수준</strong>으로 이용할 수 있어 시중 1금융권 대출보다 훨씬 유리합니다.</li>
        <li><strong>상환 기간:</strong> 거치기간 2년을 포함하여 총 <strong>5년 분할 상환</strong> 조건이 적용됩니다. 초기 2년 동안은 원금 상환 없이 매달 이자만 납부하므로 창업 초기나 경영 악화 시기에 비용 부담을 크게 덜 수 있습니다.</li>
        <li><strong>중도상환수수료 면제:</strong> 정부 정책자금은 대출 기간 중 원금을 언제든지 상환해도 중도상환수수료가 전액 면제되므로, 여유 자금이 생기면 바로 갚아 이자 지출을 줄일 수 있습니다.</li>
      </ul>

      <h2>4. 100% 비대면 온라인 신청 방법 및 구비 서류</h2>
      <p>소상공인시장진흥공단은 소상공인의 편의를 위해 직접 방문 없이 공단 누리집을 통해 <strong>모바일 및 온라인 접수</strong>를 진행하고 있습니다.</p>
      <ol>
        <li><strong>소상공인정책자금 누리집 접속:</strong> [소상공인정책자금 온라인 플랫폼]에 접속하여 공인인증서 또는 간편인증으로 로그인합니다.</li>
        <li><strong>자가진단 및 동의서 작성:</strong> 대출 신청 자격 조건에 부합하는지 비대면 설문을 작성하고 개인정보 및 신용정보 조회 동의를 진행합니다.</li>
        <li><strong>제출 서류 자동 수집(마이데이터):</strong> 국세청 홈택스 등과 연동되어 사업자등록증명원, 부가가치세과세표준증명, 국세/지방세 완납증명서 등 필수 서류는 마이데이터를 통해 자동으로 제출되므로 매우 편리합니다.</li>
        <li><strong>신청 완료 및 서류 심사:</strong> 서류 제출이 완료되면 공단에서 사업장 실사(필요시) 및 재무 상태 심사를 거쳐 대출 약정을 체결하게 됩니다. 직접대출은 공단에서 바로 송금되며, 대리대출은 보증서 발급 후 시중은행을 방문하여 대출을 실행합니다.</li>
      </ol>
        """
    },

    "unemployment-benefit-apply.html": {
        "title": "2026년 실업급여 조건 및 신청방법 지급액 상하한액 계산 총정리",
        "description": "2026년 최저임금 인상(10,320원)에 따라 7년 만에 상향 조정된 실업급여(구직급여)의 1일 상한액(68,100원) 및 하한액, 비자발적 퇴사 등 수급 자격 요건, 온라인/모바일 신청 절차와 최근 강화된 반복 수급자 제재 및 감액 기준까지 한눈에 알기 쉽게 총정리해 드립니다.",
        "category": "정부지원금",
        "image_url": "https://images.unsplash.com/photo-1521790797524-b2497295b8a0?auto=format&fit=crop&w=800&q=80",
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
            ("이직확인서 and 피보험자격 상실신고서는 언제 처리되나요?", "원칙적으로 퇴사 후 사업주가 고용노동부에 제출해야 합니다. 처리가 지연될 경우 이전 회사에 요청하거나 관할 고용센터에 문의하여 처리를 촉구할 수 있습니다.")
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
    updated = False
    
    for filename, post_data in NEW_POSTS_DATA.items():
        if filename not in existing_filenames:
            date_display = "2026.07.03" if filename == "small-business-support-grant-2026.html" else "2026.06.23"
            publish_date = "2026-07-03" if filename == "small-business-support-grant-2026.html" else "2026-06-23"
            publish_time = "07:00" if filename == "small-business-support-grant-2026.html" else "22:00"
            
            entry = {
                "filename": filename,
                "title": post_data["title"],
                "description": post_data["description"],
                "image_url": post_data["image_url"],
                "tag": post_data["category"],
                "date_display": date_display,
                "publish_date": publish_date,
                "publish_time": publish_time
            }
            schedule['posts'].append(entry)
            existing_filenames.add(filename)
            updated = True
            print(f"[SUCCESS] schedule.json updated for {filename}")
        else:
            print(f"[INFO] Post {filename} already exists in schedule.json")
            
    if updated:
        with open(SCHEDULE_PATH, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, indent=2, ensure_ascii=False)

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