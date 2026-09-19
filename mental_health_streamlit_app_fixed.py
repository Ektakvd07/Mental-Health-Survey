
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Mental Health in Tech | EDA Dashboard", page_icon="🧠", layout="wide")

REQUIRED = [
    "timestamp","age","gender","country","state","self_employed","family_history",
    "treatment","work_interfere","no_employees","remote_work","tech_company",
    "benefits","care_options","wellness_program","seek_help","anonymity","leave",
    "mental_health_consequence","phys_health_consequence","coworkers","supervisor",
    "mental_health_interview","phys_health_interview","mental_vs_physical","obs_consequence"
]

@st.cache_data
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("mental_health_tech_survey_cleaned.csv")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    if "timestamp" in df:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    if "age" in df:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
    return df

def yes_pct(s):
    x = s.astype(str).str.strip().str.lower()
    return (x.eq("yes").mean() * 100) if len(x) else 0

def count_plot(data, x, title):
    counts = data[x].astype(str).value_counts(dropna=False).reset_index()
    counts.columns = [x, "count"]
    return px.bar(counts, x=x, y="count", title=title)


def show_chart(fig, key):
    """Display a Plotly chart with an explicit unique Streamlit key."""
    st.plotly_chart(
        fig,
        use_container_width=True,
        key=key
    )

st.sidebar.title("🧠 Mental Health in Tech")
st.sidebar.caption("Interactive EDA dashboard")
uploaded = st.sidebar.file_uploader("Upload CSV (optional)", type=["csv"])
df = load_data(uploaded)

missing_required = [c for c in REQUIRED if c not in df.columns]
if missing_required:
    st.error("Missing expected columns: " + ", ".join(missing_required))
    st.stop()

st.sidebar.markdown("### Filters")
gender_options = sorted(df["gender"].dropna().astype(str).unique())
gender_sel = st.sidebar.multiselect("Gender", gender_options, default=gender_options)
treat_options = sorted(df["treatment"].dropna().astype(str).unique())
treat_sel = st.sidebar.multiselect("Treatment", treat_options, default=treat_options)
country_options = sorted(df["country"].dropna().astype(str).unique())
country_sel = st.sidebar.multiselect("Country", country_options, default=country_options)
remote_options = sorted(df["remote_work"].dropna().astype(str).unique())
remote_sel = st.sidebar.multiselect("Remote Work", remote_options, default=remote_options)

age_min = int(np.nanmin(df["age"])) if df["age"].notna().any() else 18
age_max = int(np.nanmax(df["age"])) if df["age"].notna().any() else 100
age_range = st.sidebar.slider("Age range", min_value=age_min, max_value=age_max, value=(age_min, age_max))

filtered = df[
    df["gender"].astype(str).isin(gender_sel) &
    df["treatment"].astype(str).isin(treat_sel) &
    df["country"].astype(str).isin(country_sel) &
    df["remote_work"].astype(str).isin(remote_sel) &
    df["age"].between(age_range[0], age_range[1], inclusive="both")
].copy()

st.title("🧠 Mental Health in Tech Survey — EDA Dashboard")
st.markdown("Explore demographic, workplace, treatment, support, and mental-health survey patterns interactively.")
st.caption(f"Showing **{len(filtered):,}** of **{len(df):,}** respondents.")

n = len(filtered)
k1,k2,k3,k4,k5,k6 = st.columns(6)
k1.metric("Respondents", f"{n:,}")
k2.metric("Treatment %", f"{yes_pct(filtered['treatment']):.1f}%")
k3.metric("Family History %", f"{yes_pct(filtered['family_history']):.1f}%")
k4.metric("Remote Work %", f"{yes_pct(filtered['remote_work']):.1f}%")
k5.metric("Tech Company %", f"{yes_pct(filtered['tech_company']):.1f}%")
k6.metric("Avg Age", f"{filtered['age'].mean():.1f}" if n else "N/A")

tabs = st.tabs(["📌 Overview","👤 Demographics","🏢 Workplace","🧠 Mental Health","🔗 Relationships","📋 Data Explorer"])

with tabs[0]:
    st.subheader("Dataset Snapshot")
    a,b = st.columns(2)
    with a:
        st.write("**Shape:**", df.shape)
        st.write("**Columns:**", df.shape[1])
        st.write("**Missing cells:**", int(df.isna().sum().sum()))
        st.write("**Duplicate rows:**", int(df.duplicated().sum()))
    with b:
        summary = pd.DataFrame({
            "Metric":["Rows","Columns","Missing Cells","Duplicate Rows"],
            "Value":[df.shape[0],df.shape[1],int(df.isna().sum().sum()),int(df.duplicated().sum())]
        })
        st.dataframe(summary, use_container_width=True, hide_index=True)
    c1,c2 = st.columns(2)
    with c1:
        show_chart(px.pie(filtered, names="treatment", title="Treatment Distribution", hole=.45),
                    "overview_treatment_distribution")
    with c2:
        show_chart(px.histogram(filtered, x="age", nbins=20, marginal="box", title="Age Distribution"),
                    "overview_age_distribution")
    c3,c4 = st.columns(2)
    with c3:
        show_chart(px.bar(filtered["gender"].value_counts().reset_index(), x="gender", y="count", title="Gender Distribution"),
                    "overview_gender_distribution")
    with c4:
        show_chart(px.bar(filtered["country"].value_counts().head(10).sort_values().reset_index(),
                               x="count", y="country", orientation="h", title="Top 10 Countries"),
                    "overview_top_10_countries")

with tabs[1]:
    st.subheader("Demographic EDA")
    c1,c2 = st.columns(2)
    with c1:
        show_chart(count_plot(filtered,"gender","Gender Distribution"), "demographics_gender_distribution")
    with c2:
        show_chart(px.box(filtered, x="treatment", y="age", title="Age by Treatment"),
                    "demographics_age_by_treatment")
    c3,c4 = st.columns(2)
    with c3:
        show_chart(px.violin(filtered, x="gender", y="age", color="treatment", box=True, title="Age + Gender + Treatment"),
                    "demographics_age_gender_treatment")
    with c4:
        ct = pd.crosstab(filtered["gender"], filtered["treatment"], normalize="index")*100
        ct = ct.reset_index().melt(id_vars="gender", var_name="treatment", value_name="percent")
        show_chart(px.bar(ct, x="gender", y="percent", color="treatment", barmode="group", title="Treatment Rate by Gender"),
                    "demographics_treatment_by_gender")
    c5,c6 = st.columns(2)
    with c5:
        show_chart(px.bar(filtered["family_history"].value_counts().reset_index(), x="family_history", y="count", title="Family History Distribution"),
                    "demographics_family_history")
    with c6:
        ct = pd.crosstab(filtered["family_history"], filtered["treatment"], normalize="index")*100
        ct = ct.reset_index().melt(id_vars="family_history", var_name="treatment", value_name="percent")
        show_chart(px.bar(ct, x="family_history", y="percent", color="treatment", barmode="group", title="Treatment Rate by Family History"),
                    "demographics_treatment_by_family_history")
    c7,c8 = st.columns(2)
    with c7:
        show_chart(px.bar(filtered["country"].value_counts().head(15).reset_index(), x="country", y="count", title="Top 15 Countries"),
                    "demographics_top_15_countries")
    with c8:
        show_chart(px.histogram(filtered, x="age", color="gender", nbins=20, barmode="overlay", title="Age Distribution by Gender"),
                    "demographics_age_by_gender")

with tabs[2]:
    st.subheader("Workplace EDA")
    c1,c2 = st.columns(2)
    with c1:
        show_chart(count_plot(filtered,"no_employees","Company Size Distribution"), "workplace_company_size")
    with c2:
        show_chart(count_plot(filtered,"remote_work","Remote Work Distribution"), "workplace_remote_work")
    c3,c4 = st.columns(2)
    with c3:
        show_chart(count_plot(filtered,"tech_company","Technology Company Distribution"), "workplace_technology_company")
    with c4:
        show_chart(count_plot(filtered,"benefits","Mental Health Benefits"), "workplace_benefits")
    c5,c6 = st.columns(2)
    with c5:
        show_chart(count_plot(filtered,"care_options","Care Options"), "workplace_care_options")
    with c6:
        show_chart(count_plot(filtered,"wellness_program","Wellness Program"), "workplace_wellness_program")
    c7,c8 = st.columns(2)
    with c7:
        show_chart(px.bar(filtered["supervisor"].value_counts().reset_index(), x="supervisor", y="count", title="Supervisor Support"),
                    "workplace_supervisor_support")
    with c8:
        show_chart(px.bar(filtered["coworkers"].value_counts().reset_index(), x="coworkers", y="count", title="Coworker Support"),
                    "workplace_coworker_support")
    c9,c10 = st.columns(2)
    with c9:
        ct = pd.crosstab(filtered["remote_work"], filtered["treatment"], normalize="index")*100
        ct = ct.reset_index().melt(id_vars="remote_work", var_name="treatment", value_name="percent")
        show_chart(px.bar(ct, x="remote_work", y="percent", color="treatment", barmode="group", title="Treatment Rate by Remote Work"),
                    "workplace_treatment_by_remote")
    with c10:
        ct = pd.crosstab(filtered["no_employees"], filtered["treatment"], normalize="index")*100
        ct = ct.reset_index().melt(id_vars="no_employees", var_name="treatment", value_name="percent")
        show_chart(px.bar(ct, x="no_employees", y="percent", color="treatment", barmode="group", title="Treatment Rate by Company Size"),
                    "workplace_treatment_by_company_size")

with tabs[3]:
    st.subheader("Mental Health EDA")
    c1,c2 = st.columns(2)
    with c1:
        show_chart(count_plot(filtered,"work_interfere","Work Interference"), "mental_work_interference")
    with c2:
        show_chart(count_plot(filtered,"anonymity","Perceived Anonymity"), "mental_anonymity")
    c3,c4 = st.columns(2)
    with c3:
        show_chart(count_plot(filtered,"mental_health_consequence","Mental Health Consequence"), "mental_health_consequence")
    with c4:
        show_chart(count_plot(filtered,"mental_vs_physical","Mental vs Physical Health"), "mental_vs_physical")
    c5,c6 = st.columns(2)
    with c5:
        show_chart(px.bar(filtered["seek_help"].value_counts().reset_index(), x="seek_help", y="count", title="Seeking Help at Work"),
                    "mental_seek_help")
    with c6:
        show_chart(px.bar(filtered["leave"].value_counts().reset_index(), x="leave", y="count", title="Difficulty Taking Mental Health Leave"),
                    "mental_leave")
    c7,c8 = st.columns(2)
    with c7:
        show_chart(px.bar(filtered["mental_health_interview"].value_counts().reset_index(), x="mental_health_interview", y="count", title="Mental Health Discussion in Interview"),
                    "mental_health_interview")
    with c8:
        show_chart(px.bar(filtered["phys_health_interview"].value_counts().reset_index(), x="phys_health_interview", y="count", title="Physical Health Discussion in Interview"),
                    "physical_health_interview")
    c9,c10 = st.columns(2)
    with c9:
        ct = pd.crosstab(filtered["work_interfere"], filtered["treatment"], normalize="index")*100
        ct = ct.reset_index().melt(id_vars="work_interfere", var_name="treatment", value_name="percent")
        show_chart(px.bar(ct, x="work_interfere", y="percent", color="treatment", barmode="group", title="Treatment Rate by Work Interference"),
                    "mental_treatment_by_work_interference")
    with c10:
        show_chart(px.bar(filtered["obs_consequence"].value_counts().reset_index(), x="obs_consequence", y="count", title="Observed Workplace Consequences"),
                    "mental_observed_consequence")

with tabs[4]:
    st.subheader("Relationship & Multivariate Analysis")
    c1,c2 = st.columns(2)
    with c1:
        ct = pd.crosstab(filtered["family_history"], filtered["treatment"], normalize="index")*100
        show_chart(px.imshow(ct, text_auto=".1f", aspect="auto", title="Family History × Treatment (%)"),
                    "relationship_family_history_treatment")
    with c2:
        ct = pd.crosstab(filtered["work_interfere"], filtered["treatment"], normalize="index")*100
        show_chart(px.imshow(ct, text_auto=".1f", aspect="auto", title="Work Interference × Treatment (%)"),
                    "relationship_work_interference_treatment")
    c3,c4 = st.columns(2)
    with c3:
        ct = pd.crosstab(filtered["benefits"], filtered["treatment"], normalize="index")*100
        show_chart(px.imshow(ct, text_auto=".1f", aspect="auto", title="Benefits × Treatment (%)"),
                    "relationship_benefits_treatment")
    with c4:
        ct = pd.crosstab(filtered["care_options"], filtered["treatment"], normalize="index")*100
        show_chart(px.imshow(ct, text_auto=".1f", aspect="auto", title="Care Options × Treatment (%)"),
                    "relationship_care_options_treatment")
    st.markdown("### Numerical Correlation")
    num = filtered.select_dtypes(include=np.number)
    if num.shape[1] >= 2:
        show_chart(px.imshow(num.corr(), text_auto=".2f", aspect="auto", title="Correlation Heatmap"),
                        "relationship_correlation_heatmap")
    else:
        st.info("Not enough numerical columns for a correlation matrix.")
    st.markdown("### Cross-tab Explorer")
    col1,col2 = st.columns(2)
    all_vars = [c for c in REQUIRED if c in filtered.columns]
    with col1:
        row_var = st.selectbox("Rows", all_vars, index=min(6, len(all_vars)-1), key="cross_tab_rows")
    with col2:
        col_var = st.selectbox("Columns", all_vars, index=min(7, len(all_vars)-1), key="cross_tab_columns")
    cross = pd.crosstab(filtered[row_var], filtered[col_var], normalize="index")*100
    st.dataframe(cross.round(2), use_container_width=True)

with tabs[5]:
    st.subheader("Data Explorer & Data Quality")
    st.dataframe(filtered, use_container_width=True, height=500)
    st.download_button(
        "⬇️ Download Filtered CSV",
        filtered.to_csv(index=False).encode("utf-8"),
        file_name="mental_health_filtered.csv",
        mime="text/csv",
        key="download_filtered_csv"
    )
    st.markdown("### Missing Values")
    miss = pd.DataFrame({"column":df.columns, "missing":df.isna().sum().values})
    miss["missing_%"] = (miss["missing"]/len(df)*100).round(2)
    st.dataframe(miss.sort_values("missing", ascending=False), use_container_width=True, hide_index=True)
    st.markdown("### Descriptive Statistics")
    st.dataframe(df.describe(include="all").T, use_container_width=True)

st.divider()
st.caption("Note: Survey associations are descriptive and should not be interpreted as causal relationships.")
