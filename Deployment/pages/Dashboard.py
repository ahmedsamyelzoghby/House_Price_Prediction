
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

PRIMARY_COLOR = "#636EFA"
SECONDARY_COLOR = "#00CC96"
ACCENT_COLOR = "#EF553B"
BG_COLOR = "#0E1117"
GRID_COLOR = "#2A2E39"

custom_template = dict(
    layout=dict(
        font=dict(family="Cairo, Arial", size=14, color="white"),
        title=dict(x=0.05, xanchor="left"),
        plot_bgcolor=BG_COLOR,
        paper_bgcolor=BG_COLOR,
        xaxis=dict(showgrid=True, gridcolor=GRID_COLOR),
        yaxis=dict(showgrid=True, gridcolor=GRID_COLOR),
        margin=dict(l=40, r=40, t=50, b=40)
    )
)

# =========================
# Page Config
# =========================
st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("🏠 House Price EDA Dashboard")
st.markdown("Full Interactive Analysis 🔥")

#==========================
# Data path
#==========================
BASE_DIR = Path(__file__).resolve()
while not (BASE_DIR / "dataset").exists():
    BASE_DIR = BASE_DIR.parent
data_path = BASE_DIR / "dataset" / "clean_house_prices_df.csv"

# =========================
# Load Data
# =========================
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df

df = load_data(data_path)

# =========================
# Sidebar Filters
# =========================
st.sidebar.header("🔎 Filters")

location = st.sidebar.multiselect(
    "Location", df["location"].unique(), default=df["location"].unique()
)

bhk = st.sidebar.multiselect(
    "BHK", sorted(df["BHK"].unique()), default=sorted(df["BHK"].unique())
)

furnishing = st.sidebar.multiselect(
    "Furnishing", df["Furnishing"].unique(), default=df["Furnishing"].unique()
)

filtered_df = df[
    (df["location"].isin(location)) &
    (df["BHK"].isin(bhk)) &
    (df["Furnishing"].isin(furnishing))
]

# =========================
# Tabs
# =========================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📌 Overview",
    "📊 Univariate",
    "📈 Bivariate",
    "📉 Multivariate",
    "📍 Location"
])

# =========================
# TAB 1: Overview
# =========================
with tab1:
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(filtered_df))
    col2.metric("Avg Price", int(filtered_df["Amount(in rupees)"].mean()))
    col3.metric("Avg Area", int(filtered_df["Super Area"].mean()))

    st.dataframe(filtered_df.head())

# =========================
# TAB 2: Univariate
# =========================
# =========================
# TAB 2: Univariate
# =========================
with tab2:
    st.subheader("📊 Univariate Analysis")

    # 🔥 Sub Tabs
    num_tab, cat_tab = st.tabs(["📈 Numerical", "📊 Categorical"])

    # =========================
    # 📈 Numerical Features
    # =========================
    with num_tab:

        # Price
        fig = px.histogram(
            filtered_df,
            x="Amount(in rupees)",
            nbins=50,
            title="💰 Price Distribution",
            color_discrete_sequence=[PRIMARY_COLOR]
        )
        fig.update_layout(template=custom_template)
        fig.update_traces(marker_line_width=1, marker_line_color="white")
        st.plotly_chart(fig, use_container_width=True)

        # Area
        fig = px.histogram(
            filtered_df,
            x="Super Area",
            nbins=50,
            title="📐 Super Area Distribution",
            color_discrete_sequence=[SECONDARY_COLOR]
        )
        fig.update_layout(template=custom_template)
        fig.update_traces(marker_line_width=1, marker_line_color="white")
        st.plotly_chart(fig, use_container_width=True)

        # Bathroom
        fig = px.histogram(
            filtered_df,
            x="Bathroom",
            title="🚿 Bathroom Distribution",
            color_discrete_sequence=[ACCENT_COLOR]
        )
        fig.update_layout(template=custom_template)
        st.plotly_chart(fig, use_container_width=True)

        # Balcony
        fig = px.histogram(
            filtered_df,
            x="Balcony",
            title="🌇 Balcony Distribution",
            color_discrete_sequence=["#AB63FA"]
        )
        fig.update_layout(template=custom_template)
        st.plotly_chart(fig, use_container_width=True)

        # BHK
        bhk_counts = filtered_df["BHK"].value_counts().reset_index()
        bhk_counts.columns = ["BHK", "Count"]

        fig = px.bar(
            bhk_counts,
            x="BHK",
            y="Count",
            title="🏠 BHK Distribution",
            color="Count",
            color_continuous_scale="Blues"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

        # Current Floor
        current_floor = filtered_df["Current_Floor"].value_counts().head(15).reset_index()
        current_floor.columns = ["Floor", "Count"]

        fig = px.bar(
            current_floor,
            x="Floor",
            y="Count",
            title="🏢 Top 15 Current Floors",
            color="Count",
            color_continuous_scale="Teal"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

        # Total Floors
        total_floor = filtered_df["Total_Floors"].value_counts().head(15).reset_index()
        total_floor.columns = ["Total Floors", "Count"]

        fig = px.bar(
            total_floor,
            x="Total Floors",
            y="Count",
            title="🏗️ Top 15 Total Floors",
            color="Count",
            color_continuous_scale="Oranges"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 📊 Categorical Features
    # =========================
    with cat_tab:

        # Furnishing
        fig = px.pie(
            filtered_df,
            names="Furnishing",
            title="🛋️ Furnishing Distribution",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(template=custom_template)
        st.plotly_chart(fig, use_container_width=True)

        # Transaction
        fig = px.pie(
            filtered_df,
            names="Transaction",
            title="💼 Transaction Type",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(template=custom_template)
        st.plotly_chart(fig, use_container_width=True)

        # Ownership
        fig = px.pie(
            filtered_df,
            names="Ownership",
            title="📜 Ownership Distribution",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(template=custom_template)
        st.plotly_chart(fig, use_container_width=True)

        # Facing
        facing_counts = filtered_df["facing"].value_counts().reset_index()
        facing_counts.columns = ["Facing", "Count"]

        fig = px.bar(
            facing_counts,
            x="Count",
            y="Facing",
            orientation="h",
            title="🧭 Facing Direction",
            color="Count",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(template=custom_template, yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)

        # Locations
        top_loc = filtered_df["location"].value_counts().head(15).reset_index()
        top_loc.columns = ["Location", "Count"]

        fig = px.bar(
            top_loc,
            x="Count",
            y="Location",
            orientation="h",
            title="📍 Top 15 Locations",
            color="Count",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(template=custom_template, yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)

        # Views
        view_cols = ['View_Garden_Park', 'View_Main_Road', 'View_Pool', 'View_Unknown']
        view_counts = filtered_df[view_cols].sum().sort_values().reset_index()
        view_counts.columns = ["View Type", "Count"]

        fig = px.bar(
            view_counts,
            x="Count",
            y="View Type",
            orientation="h",
            title="🌄 Property Views",
            color="Count",
            color_continuous_scale="Magma"
        )
        fig.update_layout(template=custom_template)
        st.plotly_chart(fig, use_container_width=True)
# =========================
# TAB 3: Bivariate
# =========================
with tab3:
    st.subheader("📈 Bivariate Analysis")

    # 🔥 Sub Tabs
    num_tab2, cat_tab2, geo_tab = st.tabs([
        "📈 Numerical vs Price",
        "📊 Categorical vs Price",
        "🌍 Location & Views"
    ])

    # =========================
    # 📈 Numerical Relationships
    # =========================
    with num_tab2:

        # Area vs Price 
        fig = px.scatter(
            filtered_df,
            x="Super Area",
            y="Amount(in rupees)",
            title="📐 Area vs Price",
            color="BHK",
            opacity=0.6,
            color_continuous_scale="Viridis"
        )
        fig.update_layout(template=custom_template)
        fig.update_traces(
            marker=dict(size=6, line=dict(width=0.5, color="white")),
            hovertemplate="<b>Area:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>"
        )
        st.plotly_chart(fig, use_container_width=True)

        # BHK vs Price
        fig = px.box(
            filtered_df,
            x="BHK",
            y="Amount(in rupees)",
            title="🏠 BHK vs Price",
            color="BHK"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Bathroom vs Price
        fig = px.box(
            filtered_df,
            x="Bathroom",
            y="Amount(in rupees)",
            title="🚿 Bathroom vs Price",
            color="Bathroom"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Balcony vs Price
        fig = px.box(
            filtered_df,
            x="Balcony",
            y="Amount(in rupees)",
            title="🌇 Balcony vs Price",
            color="Balcony"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Current Floor
        top_curr = filtered_df["Current_Floor"].value_counts().head(15).index
        df_curr = filtered_df[filtered_df["Current_Floor"].isin(top_curr)]

        fig = px.box(
            df_curr,
            x="Current_Floor",
            y="Amount(in rupees)",
            title="🏢 Current Floor vs Price",
            color="Current_Floor"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Total Floors
        top_tot = filtered_df["Total_Floors"].value_counts().head(15).index
        df_tot = filtered_df[filtered_df["Total_Floors"].isin(top_tot)]

        fig = px.box(
            df_tot,
            x="Total_Floors",
            y="Amount(in rupees)",
            title="🏗️ Total Floors vs Price",
            color="Total_Floors"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 📊 Categorical Relationships
    # =========================
    with cat_tab2:

        # Furnishing
        fig = px.violin(
            filtered_df,
            x="Furnishing",
            y="Amount(in rupees)",
            box=True,
            title="🛋️ Furnishing vs Price",
            color="Furnishing"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Transaction
        fig = px.violin(
            filtered_df,
            x="Transaction",
            y="Amount(in rupees)",
            box=True,
            title="💼 Transaction vs Price",
            color="Transaction"
        )
        fig.update_layout(template=custom_template, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Ownership Median
        ownership_df = (
            filtered_df.groupby("Ownership")["Amount(in rupees)"]
            .median()
            .reset_index()
            .sort_values(by="Amount(in rupees)", ascending=False)
        )

        fig = px.bar(
            ownership_df,
            x="Ownership",
            y="Amount(in rupees)",
            title="📜 Median Price by Ownership",
            color="Amount(in rupees)",
            color_continuous_scale="Teal"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

        # Facing Median
        facing_df = (
            filtered_df.groupby("facing")["Amount(in rupees)"]
            .median()
            .reset_index()
            .sort_values(by="Amount(in rupees)", ascending=False)
        )

        fig = px.bar(
            facing_df,
            x="facing",
            y="Amount(in rupees)",
            title="🧭 Median Price by Facing",
            color="Amount(in rupees)",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 🌍 Location & Views
    # =========================
    with geo_tab:

        # Top Locations
        top_loc_names = filtered_df["location"].value_counts().nlargest(15).index

        loc_df = (
            filtered_df[filtered_df["location"].isin(top_loc_names)]
            .groupby("location")["Amount(in rupees)"]
            .median()
            .reset_index()
            .sort_values(by="Amount(in rupees)", ascending=False)
        )

        fig = px.bar(
            loc_df,
            x="Amount(in rupees)",
            y="location",
            orientation="h",
            title="📍 Top 15 Locations by Price",
            color="Amount(in rupees)",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(template=custom_template, yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)

        # Garden View
        garden_df = (
            filtered_df.groupby("View_Garden_Park")["Amount(in rupees)"]
            .median()
            .reset_index()
        )

        fig = px.bar(
            garden_df,
            x="View_Garden_Park",
            y="Amount(in rupees)",
            title="🌳 Garden View Impact",
            color="Amount(in rupees)",
            color_continuous_scale="Greens"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

        # Road View
        road_df = (
            filtered_df.groupby("View_Main_Road")["Amount(in rupees)"]
            .median()
            .reset_index()
        )

        fig = px.bar(
            road_df,
            x="View_Main_Road",
            y="Amount(in rupees)",
            title="🛣️ Main Road Impact",
            color="Amount(in rupees)",
            color_continuous_scale="Oranges"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

        # Pool View
        pool_df = (
            filtered_df.groupby("View_Pool")["Amount(in rupees)"]
            .median()
            .reset_index()
        )

        fig = px.bar(
            pool_df,
            x="View_Pool",
            y="Amount(in rupees)",
            title="🏊 Pool Impact",
            color="Amount(in rupees)",
            color_continuous_scale="Blues"
        )
        fig.update_layout(template=custom_template, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
# =========================
# TAB 4: Multivariate
# =========================
with tab4:
    st.subheader("📉 Multivariate Analysis")

    # 🔥 Sub Tabs
    inter_tab, corr_tab = st.tabs([
        "📊 Feature Interactions",
        "🔥 Correlation Matrix"
    ])

    # =========================
    # 📊 Feature Interactions
    # =========================
    with inter_tab:

        # Area vs Price (Pool Effect)
        fig = px.scatter(
            filtered_df,
            x="Super Area",
            y="Amount(in rupees)",
            color="View_Pool",
            title="🏊 Area vs Price (Pool Effect)",
            opacity=0.6,
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_layout(template=custom_template)

        fig.update_traces(
            marker=dict(size=7, line=dict(width=0.5, color="white")),
            hovertemplate="<b>Area:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Area vs Price (BHK Effect)
        df_bhk = filtered_df[filtered_df["BHK"].isin([1, 2, 3, 4, 5])]

        fig = px.scatter(
            df_bhk,
            x="Super Area",
            y="Amount(in rupees)",
            color="BHK",
            title="🏠 Area vs Price (BHK Effect)",
            opacity=0.6,
            color_continuous_scale="Viridis"
        )

        fig.update_layout(template=custom_template)

        fig.update_traces(
            marker=dict(size=7, line=dict(width=0.5, color="white")),
            hovertemplate="<b>BHK:</b> %{marker.color}<br><b>Area:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>"
        )

        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 🔥 Correlation Matrix 
    # =========================
    with corr_tab:

        numeric_df = filtered_df.select_dtypes(include=["int64", "float64"])
        corr = numeric_df.corr()

        fig = px.imshow(
            corr,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            title="📊 Correlation Matrix",
            aspect="auto"
        )

        fig.update_layout(
            template=custom_template,
            xaxis=dict(side="bottom"),
            coloraxis_colorbar=dict(title="Correlation")
        )

        
        fig.update_traces(
            hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z}<extra></extra>"
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================
# TAB 5: Location
# =========================
with tab5:
    st.subheader("📍 Top Locations")

    top_loc = filtered_df["location"].value_counts().nlargest(10).reset_index()
    top_loc.columns = ["Location", "Count"]

    fig = px.bar(
        top_loc,
        x="Count",
        y="Location",
        orientation="h",
        color="Count",
        color_continuous_scale="Tealgrn",
        title="Top 10 Locations by Listings"
    )

    fig.update_layout(
        template=custom_template,
        title_x=0.3,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(fig, use_container_width=True)


    # =========================
    # 💰 Avg Price per Location
    # =========================
    st.subheader("💰 Avg Price per Location")

    avg_price = (
        filtered_df
        .groupby("location")["Amount(in rupees)"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        avg_price,
        x="Amount(in rupees)",
        y="location",
        orientation="h",
        color="Amount(in rupees)",
        color_continuous_scale="Sunset",
        title="Top 10 Locations by Average Price"
    )

    fig.update_layout(
        template=custom_template,
        title_x=0.25,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(fig, use_container_width=True)

