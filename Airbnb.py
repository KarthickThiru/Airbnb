import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os

# Streamlit part

st.set_page_config(layout="wide")

st.title("AIRBNB :compass:")
st.write(" 🧑‍💻 Tech Used: Python scripting, Data Preprocessing, Visualization, EDA, Streamlit, PowerBI or Tableau.")

def datafr():
    df= pd.read_csv("K:/DS/Airbnb/Airbnb_dataX_v3.csv")
    return df

df= datafr()
    
select=option_menu(
    menu_title= None,
    options= ["About Airbnb","Exploration & Visualization","Process Followed"],
    icons=["browser-safari", "clipboard2-data", "bounding-box"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal")

if select == "About Airbnb":

    col1,col2=st.columns(2)

    with col1:
        image1= Image.open("K:/DS/Airbnb/Airbnb_logo.jpeg")
        st.image(image1)
    
    with col2:
        
        st.header("About Airbnb")
        st.write("")
        st.write('''Airbnb is an online marketplace that connects people who want to rent out
                their property with people who are looking for accommodations,
                typically for short stays. Airbnb offers hosts a relatively easy way to
                earn some income from their property. Guests often find that Airbnb rentals
                are cheaper and homier than hotels.''')
        st.write("")
        st.write('''Airbnb is an American company operating an online marketplace for short- and long-term homestays and experiences. 
                 The company acts as a broker and charges a commission from each booking. 
                 The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. 
                 Airbnb is a shortened version of its original name, AirBedandBreakfast.com.''')
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("Click the below link to vist airbnb website")
        st.write("https://www.airbnb.co.in/login")

if select == "Exploration & Visualization":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["AVAILABILITY","PRICE", "LOCATION", "GEOSPATIAL VISUALIZATION", "CHARTS"])

    with tab1:
        def datafr():
            df_a= pd.read_csv("K:/DS/Airbnb/Airbnb_dataX_v3.csv")
            return df_a

        df_a= datafr()

        st.title("**AVAILABILITY**")
        col1,col2= st.columns(2)

        with col1:

            country_a= st.selectbox("Select the Country for Availability",df_a["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type to find Availability",df1_a["property_type"].unique())

            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

        with col1:

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_30)
        
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            
            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Burgyl_r)
            st.plotly_chart(df_a_sunb_60)
        
        col1,col2= st.columns(2)

        with col1:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Blackbody_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Mint_r)
            st.plotly_chart(df_a_sunb_365)
        
        roomtype_a= st.selectbox("Select the Room Type to view Host Response Time", df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Inferno,width=1000)

        st.plotly_chart(fig_df_mul_bar_a)

    with tab2:

        def datafr():
            df_a= pd.read_csv("K:/DS/Airbnb/Airbnb_dataX_v4.csv")
            return df_a

        df_a= datafr()

        st.title("**PRICE**")
        col1,col2= st.columns(2)

        with col1:

            country= st.selectbox("Select the Country to view Price Details",df["country"].unique())

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Hot_r, width=600, height=500)
            st.plotly_chart(fig_bar)
        
        with col2:
            
            proper_ty= st.selectbox("Select the Property Type",df2["property_type"].unique())

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.amp,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2= st.columns(2)

        with col1:

            
            hostresponsetime= st.selectbox("Select the host response time",df4["host_response_time"].unique())

            df5= df4[df4["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Pinkyl, width=600, height=500)
            

            st.plotly_chart(fig_do_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS BASED ON ACCOMMODATION',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.amp, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)
    
    with tab3:

        st.title("LOCATION")
        st.write("")

        def datafr():
            df= pd.read_csv("K:/DS/Airbnb/Airbnb_dataX_v4.csv")
            return df

        df_l= datafr()

        country_l= st.selectbox("Select the Country to view based on Location",df_l["country"].unique())

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property Type to view based on Location",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=["name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "host_name", "host_location",                   
                                            "host_response_time",            
                                            "host_response_rate","host_is_superhost",         
                                            "host_neighbourhood",
                                            "host_identity_verified",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","house_rules","is_location_exact",
                                            "amenities"]).corr()
        
        # st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATION",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Electric_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room Type for viewing", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Sunsetdark_r,width=1000)
        st.plotly_chart(fig_2)

    with tab4:

        country_l= st.selectbox("Select the Country to view on Map",df_l["country"].unique())

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property Type to on Map",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df2_l, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "Inferno",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)
    
    with tab5:

        country_t= st.selectbox("Select the Country to view",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST NEIGHBOURHOOD", color_discrete_sequence=px.colors.sequential.Sunsetdark_r, width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST NEIGHBOURHOOD",color_discrete_sequence=px.colors.sequential.Sunsetdark, width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Viridis_r,
                                title= "PRICE BASED ON HOST LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Viridis,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room Type",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                color_continuous_scale= "Magma",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM NIGHTS MAXIMUM NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                color_continuous_scale= "Viridis",
                                title= "BEDROOMS, BEDS, ACCOMMODATES AND BED TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)

if select == "Process Followed":

    st.header("ABOUT THIS PROJECT")


    st.subheader(":blue[DATA COLLECTION:]")

    st.write('''**Establish a MongoDB connection, retrieve the Airbnb dataset and ensured efficient data retrieval for analysis**''')
    
    st.subheader(":blue[DATA CLEANING AND PROCESSING:]")

    st.write('''**Cleaned and prepared the dataset, addressing the missing values, duplicates and data type conversions for accurate
              analysis.**''')
    
    st.subheader(":blue[EDA - EXPLORATORY DATA ANALYSIS:]")

    st.write('''**Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.**''')
    
    st.subheader(":blue[GEOSPATIAL & VISUALIZATION:]")

    st.write('''**Developed a streamlit web application with interactive maps showcasing the distribution of Airbnb listings, 
             allowing users to explore prices, ratings, and other relevant factors. 
             Conducted price analysis and visualization, exploring variations based on location and 
             property type using dynamic plots and charts. Investigated location-based insights by extracting and visualizing 
             data for specific regions or neighborhoods.**''')
    
    st.subheader(":red[POWER BI:]")

    st.write('''**Built a comprehensive dashboard using Power BI, combining various visualizations to present key 
             insights from the analysis.**''')