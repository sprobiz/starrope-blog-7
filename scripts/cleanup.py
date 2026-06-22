import os
import re

def clean_post_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # 1. 브릿지 리다이렉트 링크 직링크로 치환 (../apply.html?target=https://... -> https://...)
    # 따옴표에 싸인 주소를 매칭
    bridge_pattern = r'\.\./apply\.html\?target=(https?://[^\s"]+)'
    content = re.sub(bridge_pattern, r'\1', content)

    # 2. 가짜 보안 로딩 안내 문구 제거 및 자연스러운 리다이렉트 문구로 변환
    # (이동 시 1~2초간 보안 점검 로딩이 진행될 수 있습니다.) 또는 (이동 시 1~2초간 데이터 보안성 점검 로딩이 진행될 수 있습니다.) 제거
    fake_desc_patterns = [
        r'\(이동 시 1~2초간 보안 점검 로딩이 진행될 수 있습니다\.\)',
        r'\(이동 시 1~2초간 데이터 보안성 점검 로딩이 진행될 수 있습니다\.\)'
    ]
    for pattern in fake_desc_patterns:
        content = re.sub(pattern, '', content)

    # 부가적인 안내 멘트 정돈 (보안 로딩 관련 잔재 텍스트 수정)
    content = content.replace("아래 버튼을 클릭하시면 공식 신청 페이지(안전 연결)로 즉시 이동합니다.<br>", 
                              "아래 버튼을 클릭하시면 공식 신청 페이지로 즉시 이동합니다.")
    content = content.replace("아래 버튼을 클릭하시면 보건복지부 공식 복지포털인 '복지로' 기초연금 신청 페이지로 즉시 이동합니다.<br>", 
                              "아래 버튼을 클릭하시면 보건복지부 공식 복지포털인 '복지로' 기초연금 신청 페이지로 즉시 이동합니다.")
    content = content.replace("아래 버튼을 클릭하시면 공식 복지로 포털의 긴급복지지원 상세 가이드 및 온라인 모의계산 페이지로 이동합니다.<br>", 
                              "아래 버튼을 클릭하시면 공식 복지로 포털의 긴급복지지원 상세 가이드 및 온라인 모의계산 페이지로 이동합니다.")

    # 3. 하단 무효 애드센스 push 루프 스크립트 제거
    ad_loop_pattern = r'<!-- Trigger Adsense rendering loop -->\s*<script>\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);\s*</script>'
    content = re.sub(ad_loop_pattern, '', content)
    
    # 띄어쓰기나 포맷이 살짝 다른 경우도 대비하여 일반적인 패턴으로 매칭 시도
    general_ad_loop_pattern = r'<script>\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);\s*</script>'
    content = re.sub(general_ad_loop_pattern, '', content)

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 수정 완료: {os.path.basename(file_path)}")
        return True
    else:
        print(f"ℹ️ 변경 사항 없음: {os.path.basename(file_path)}")
        return False

def main():
    project_root = r"c:\Users\ASUS\..antigravity\2)_내_스타로프_애드센스_프로젝트\7)_정부지원금_복지정책"
    # 상대경로로 프로젝트 루트 탐색
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    posts_dir = os.path.join(project_root, "posts")

    print(f"블로그 프로젝트 클린업 시작 (경로: {project_root})")
    
    # 1. posts 폴더 내 모든 HTML 파일 클린업
    modified_count = 0
    if os.path.exists(posts_dir):
        for file_name in os.listdir(posts_dir):
            if file_name.endswith(".html"):
                file_path = os.path.join(posts_dir, file_name)
                if clean_post_file(file_path):
                    modified_count += 1
    
    # 2. apply.html 파일 무력화 (삭제 대신 구글 정책 위반 소지 제거를 위해 index.html로 다이렉트 리다이렉트하게 변경)
    apply_path = os.path.join(project_root, "apply.html")
    if os.path.exists(apply_path):
        with open(apply_path, "r", encoding="utf-8") as f:
            apply_content = f.read()
        
        # apply.html 내부에서 자동 리다이렉트 1.5초 지연 코드 및 광고 스크립트 제거
        # index.html로 직접 보내거나, 그냥 "잘못된 접근" 화면으로 고정
        original_apply = apply_content
        
        # 애드센스 스크립트 제거 (브릿지 페이지에 광고를 로드하는 것은 정책 위반이므로 광고 태그를 아예 삭제)
        apply_content = re.sub(r'<!-- Pre-configured Google AdSense Auto Ads Tag -->\s*<script.*?</script>', '', apply_content)
        
        # 1.5초 지연 및 버퍼 제거 -> 바로 이동하게 0초로 변경하고 주석 변경
        apply_content = apply_content.replace("// 1.5초 후 자동 리다이렉션 (전면 광고 노출 시간 버퍼 확보)\n      setTimeout(() => {\n        window.location.href = targetUrl;\n      }, 1500);", 
                                              "// 즉시 공식 사이트로 안전하게 리다이렉션\n      window.location.href = targetUrl;")
        
        if apply_content != original_apply:
            with open(apply_path, "w", encoding="utf-8") as f:
                f.write(apply_content)
            print("✅ apply.html 브릿지 광고 및 지연 코드 제거 완료 (안전화 처리)")

    print(f"\n작업 완료! 총 {modified_count}개의 포스트 파일이 안전하게 수정되었습니다.")

if __name__ == "__main__":
    main()
