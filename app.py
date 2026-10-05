from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CAPEX Dashboard 2027 & Business Plan 2027-2031",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SECRET_KEY = "capex2027"

# Safe query parameters retrieval for all Streamlit versions
url_key = ""
try:
    if hasattr(st, "query_params"):
        raw_key = st.query_params.get("key", "")
        if isinstance(raw_key, list):
            url_key = raw_key[0] if raw_key else ""
        else:
            url_key = str(raw_key)
    elif hasattr(st, "experimental_get_query_params"):
        raw_key = st.experimental_get_query_params().get("key", [""])
        url_key = raw_key[0] if isinstance(raw_key, list) else str(raw_key)
except Exception:
    url_key = ""

url_key = url_key.strip()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Auto-unlock immediately if valid VIP key is in URL
if url_key.lower() == SECRET_KEY.lower():
    st.session_state.authenticated = True

@st.cache_data
def load_html():
    p = Path(__file__).parent / "dashboard.html"
    return p.read_text(encoding="utf-8")

if st.session_state.authenticated:
    # Hide Streamlit menu for clean executive presentation
    st.markdown(
        """
        <style>
            #MainMenu {visibility: hidden;}
            .block-container {padding: 0.2rem 0.5rem 0 0.5rem; max-width: 100%;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    try:
        html_content = load_html()
        components.html(html_content, height=2600, scrolling=True)
    except Exception as e:
        st.error(f"Error loading dashboard: {e}")
else:
    # Professional Corporate Lock Screen for unauthorized viewers
    st.markdown(
        """
        <style>
            #MainMenu {visibility: hidden;}
            .stApp {
                background: linear-gradient(135deg, #f0fdf4 0%, #f8fafc 100%);
            }
            .lock-card {
                max-width: 520px;
                margin: 4rem auto 1.5rem auto;
                padding: 2.2rem 2.5rem;
                background: #ffffff;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 84, 61, 0.08), 0 2px 6px rgba(0,0,0,0.04);
                border-top: 5px solid #00543D;
                text-align: center;
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            }
            .lock-icon {
                font-size: 3rem;
                margin-bottom: 0.8rem;
            }
            .lock-title {
                font-size: 1.45rem;
                font-weight: 700;
                color: #00543D;
                margin-bottom: 0.4rem;
            }
            .lock-subtitle {
                font-size: 0.95rem;
                color: #4b5563;
                margin-bottom: 1.2rem;
                line-height: 1.5;
            }
            .lock-notice {
                font-size: 0.88rem;
                color: #64748b;
                background: #f1f5f9;
                border: 1px dashed #cbd5e1;
                border-radius: 8px;
                padding: 0.85rem;
                line-height: 1.45;
                text-align: left;
            }
        </style>
        <div class="lock-card">
            <div class="lock-icon">🔒</div>
            <div class="lock-title">Aboitiz Foods — Agri B Group</div>
            <div class="lock-subtitle">CAPEX Budget 2027 & Business Plan (2027–2031)<br><strong>Báo cáo Nội bộ — Giới hạn truy cập</strong></div>
            <div class="lock-notice">
                ℹ️ <strong>Thông báo bảo mật:</strong> Dữ liệu tài chính và kế hoạch kinh doanh được giới hạn lưu hành nội bộ. Nếu bạn chưa có quyền truy cập, vui lòng liên hệ <strong>Quản trị viên (Người tạo báo cáo)</strong> để được cấp mật mã phê duyệt.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        entered_key = st.text_input(
            "Mật mã truy cập:",
            type="password",
            placeholder="Nhập mã được cấp để mở báo cáo...",
            key="lock_input",
        )
        if st.button("🔓 Mở Dashboard", use_container_width=True, type="primary"):
            if entered_key.strip().lower() == SECRET_KEY.lower():
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Mật mã không chính xác. Vui lòng liên hệ Quản trị viên để nhận mã phê duyệt.")
