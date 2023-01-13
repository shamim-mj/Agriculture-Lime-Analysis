#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Lime Calculator with Charts",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="expanded"
)


## Making Manues

# 3. CSS style definitions
with st.sidebar:
    selected1 = option_menu("", ["Home","Calculator", "Contact"], 
        icons=['house', 'calculator', 'person lines fill'], 
        menu_icon="cast", default_index=0, #orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#0033A0"},
        }
    )

#End manues



# This is a CSS styling that affects some part of the App.
st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: light blue;
}

[class^="st-b"] {
    color: black;
    font-size = 25px;
    font-weight= bold;
    color: black;
    font-family: monospace;
}

</style>
""",
    unsafe_allow_html=True,
)


# Lets add a title to our App 
# add some information
if selected1=='Home':
    st.markdown("<h1 style='background-color: #0033A0; text-align: center; color: 	white;'>Lime Calculator with Color Charts</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='background-color: #0033A0;text-align: center; color: 	white;'>Particle Analysis, CCE, RNV, pH, Buffer pH, Rates, and Cost/Acre</h4>", unsafe_allow_html=True)
    st.markdown(
    """<div style="text-align: justify;">
    All rights reserved. </br>
    This web application was developed by <a href = 'https://www.linkedin.com/in/mohammad-jan-shamim-693136112/'>Mohammad Shamim</a>, and Robbie Williams in Henderson, Kentucky, USA.</br>
    You can perfom your calculation either by manually inserting values into the cells on the "Calculator" Menu or by uploading the values in a CSV file. 
    The manual form allows up to five lime sources calculations. 
    Uploading an CSV file allows an unlimited number of lime sources calculations. </br>
    Be sure to check boxes/toggle buttons for desired calculations as graphs. 
    This web app uses Sikora-2 buffer for determining the quantity and cost of lime to be applied in an acre. </br>
    We are greatly indebted to His Excellency <a href =' https://pss.ca.uky.edu/person/frank-sikora'>Dr. Frank Sikora</a>, 
    Adjunct Associate Professor and Director of Laboratories and Soils Program Regulatory Services, the University of  Kentucky, USA, for his invaluable input in this Web App. </br>
    </br>
    Read more...</br>
     <a href = 'http://www2.ca.uky.edu/agcomm/pubs/id/id163/id163.pdf'> Agicultural Lime Recommendation Based on Lime Quality </a> </br>
     <a href = "https://www.rs.uky.edu/soil/technical_info/">Rock Quarry Lime Reports - University of Kentucky</a>
    </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    image1, image2 = st.columns(2)
    img1 = plt.imread('Lime particles .jpg')
    img2 = plt.imread('Sieves1.jpg')
    image1.image(img2)
    image2.image(img1)


    
#     st.markdown("<h2 style='background-color: #0033A0; text-align: center; color: 	white;'>Instructions</h1>", unsafe_allow_html=True)
#     st.markdown("<h3 style='background-color: white; text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)
#     container2 = st.container()
#     container2.markdown("""
#     <div style="text-align: justify;">
#     <span style='color: #0033A0; font-weight: bold;'>A) Using the App:</span> This web App has three menus. In the <span style='color: blue; font-weight: bold;'>Home </span> manu, you can read about the App.
#     The main menu is the <span style='color: #0033A0; font-weight: bold;'>Calculator </span> where you can input your data and calculate your samples for 
#     particle size,  RNV, lime amount recommendation, its application cost  per acre, and see the charts. Manually,  you can open up to 5 slots for your agricultural lime analysis. For example, if you are interested in analyzing 
#     3 lime sources, you will select 3 from  the sample selector which is titled as "# of Samples". 
#     After that, the form will show 3 columns for you. You can populate the cells and see the charts. Alternatively, you can upload a comma separated values (.csv) file with unlimited samples.  <span style='color: black; font-weight: bold;'> Be sure to have your Target pH higher than your soil water pH.</span>
#     The default color of the charts is "Dark2" but you can choose from  over 100 colors from the drop-down list. </br>To save a chart to your computer, right-click on the chart 
#     and then choose "save image as" or "copy image" and then paste it as a picture in other places (press and hold in the case of a smartphone or iPad). To save data, 
#     you will need to go to the <span style='color: #0033A0; font-weight: bold;'>Download </span> section in the "Calculator" menu. By clicking the download button,  
#     the data will be saved to your machine automatically. In the data, you will see many columns. "Initial" is the initial weight of the sample, "gten" means the amount that did not pass through the #10 Sieve, 
#     "lten" is the amount that passed through the #10 Sieve, "lfifty" is the amount that passed through the #50 Sieve, 
#     "wph" is soil water pH, "bph" is soil buffer pH, "cce" is Culcium Carbonate Equivalent (CCE), "Zero%_eff" is the percent of lime with particle size bigger than #10 Sieve. "Fifty%_eff" is the percent of lime with particle size smaller than #10 Sieve and bigger than #50 Seive, and "Hund%_eff" is the percent of lime that is 100 
#     percent effective or the percent of lime with particle size smaller than #50 Sieve. RNV is the relative neutralizing value, "Bulk_rec" is the amount of lime need to be applied and "Cost" is the cost per acre.
#     If you want all slots opened side by side, please rotate the screen of your mobile device. If you want to change the theme, Go to Setting> Theme> and then choose one from the drop-down list. </br> 
    
#     <span style='color: #0033A0; font-weight: bold;'>B) Calculating RNV:</span> To know the relative neutralizing value (RNV) of the lime, you will need to know the value of
#     Calcium Carbonate Equivalent (CCE) and the particle size fraction. 
#     You can obtain this information from yuor  lime supplier or from various state and university lab reports. For example, <a href = "https://www.rs.uky.edu/soil/technical_info/">Rock Quarry Lime Reports - University of Kentucky</a>
#     This app is set up for #10 and #50 sieves and accepts lime particle size fractions in (%) of total or individual  sieve weights. The University of Kentucky 
#     uses #10 and #50 sieves for lime particle analysis. Other testing labs may use different sieve sets. For example, #8, #20,  #60, and #100 sieves. 
#     If you have access to a sieve shaker and wish to separate and weigh your own particle size fractions, dry the lime overnight at 230 degrees F (110 degress C).
#     Graphs are  automatically created. You can view and save graphs and download the data as a CSV file. 
#     You can view and save graphs and download the data as a CSV file.
#     </div>
#         """, unsafe_allow_html=True)

# # A refernce to the paper I used for buffer
#     st.markdown("<h3 style='background-color: white; text-align: left; color: #0033A0;'>Reference</h1>", unsafe_allow_html=True)
#     container8 = st.container()
#     container8.write("""
#     <div style="text-align: justify;">
#     <span style='color: black; text-align: justify'>Ritchey, E.L., Murdock, L.W., Ditsch, D., and McGrath, J.M. 2016. Agicultural Lime Recommendation Based on Lime Quality. Plant and Soil Science.
#     F.J. Sikora, Division of Regolatory Services, College of Agriculture, Food and Environment, University of Kentucky.</span>
#     <a href = 'http://www2.ca.uky.edu/agcomm/pubs/id/id163/id163.pdf'> Click here to read!</a> </div>
#     """, 
#     unsafe_allow_html = True)


if selected1=="Calculator":
    # Add a tile to the sources of the lime
    st.markdown("<h2 style='background-color: #0033A0; font-size:35px; text-align: center; color: 	white;'>Lime and Soil Data</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>" "</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>" "</h1>", unsafe_allow_html=True)
    


    # Lets make some empty dictionary to save data
    # This is used to loop through the data in dynamic columns. You can use pandas dataframe directly too. 

    quarries = {}
    initial ={}
    gten  = {}
    lfifty = {}
    CCE = {}
    Price ={}
   

    # Lets give the users option. In some cases the users may do the analysis themselves and know the weight of the sammpls
    # in other cases the users recieve data from special laboratories and the laboratories only give them data in percentage, not weight
    # So we have option for either case.
    percent_weight = option_menu(None, ["Lab Results (Weight)", "Lab Results (Percentage)"], 
        icons=[], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#ffe6e6"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#ff0000"},
        }
    )






    # percent_weight = st.radio("**Is your result based on percentage or weight?**", options =("Lab Results (Weight)", "Lab Results (Percentage)"))

    # Lets make the columns or slots dynamic

    # Telling the user wheather s/he wants to enter the data manually (convinient for smartphone)
    # st.markdown("<h3 style='text-align: center; color: white; font-size:25px; background-color: #0033A0; margin: 0px'>Manual Input</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: blue;'>" "</h5>", unsafe_allow_html=True)

    # Here, I am setting a condition if the data is in percentage or weight
    # Lets loop through the columns
    if percent_weight =="Lab Results (Weight)":
        f_container = st.container()
        samp_cont1, samp_cont2 = f_container.columns([1, 3])
        samp_cont1.markdown("<h5 style='text-align: center; color: blue;'>" "</h5>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: white; background-color: #0033A0;'>Lime Data</h4>", unsafe_allow_html=True)
        samp_cont1.markdown("<h5 style='text-align: center; color: white; background-color: #0033A0;'># Samples</h5>", unsafe_allow_html=True)
        ncol = samp_cont1.number_input("# Sample", 1, 5, 2, label_visibility='collapsed')
        cols = st.columns(ncol)
        for i, x in enumerate(cols):

            quarries[i]= x.text_input('**Lime Source:**', value = f'Sample {i+1}',key = f"q_{i}_name")
            initial[i] = x.number_input('**Initial Amount (g)**: ', value = 100.00, key = f"q_{i}_initial", format="%.2f")
            gten[i] = x.number_input('**Amount > #10 (g)**: ', value = 10.00, key = f"q_{i}_10", format="%.2f")
            lfifty[i] = x.number_input('**Amount < #50 (g):**', value = 60.00, key = f"q_{i}_50", format="%.2f")
            CCE[i] = x.number_input("**Culcium Carbonate Equivalent (CCE):** ", value = 90.0, key = f'cce{i}', format="%.1f")
            Price[i] = x.number_input("**Price ($/ton)**", value = 20.0, key = f'price{i}', format="%.1f")

        st.markdown("<h4 style='text-align: center; color: white; background-color: #0033A0;'>Soil Data </h4>", unsafe_allow_html=True)
        s_container = st.container()
        c1, c2, c3= s_container.columns(3)
        wph = c1.slider('**Soil Water pH:**', min_value=4.0, max_value=8.0, value=5.8, step=0.1, key='wph', format="%.1f")
        bph = c2.slider('**Buffer pH (Sikora-2):**', min_value=4.0, max_value=8.0, value=6.5, step=0.1, key='bph', format="%.1f")
        tph= c3.slider('**Target pH**', min_value=4.0, max_value=8.0, value=6.5, step=0.1, key='tph', format="%.1f")
        # soilW = c4.slider('**Soil Weight (g):**',min_value=8.0, max_value=14.0, value=12.0, step=0.1, key='sw', format="%.1f")

        # This datafram is dynamic and therefore making the charts easy to plot

        df = pd.DataFrame({"Quarry": [i for i in quarries.values()],
            "initial": [i  for i in initial.values()], 
            "gten":[i for i in gten.values()],
            "lten": [i-j for i, j in zip(initial.values(), gten.values())],
            "lfifty": [i for i in lfifty.values()],
            'cce': [i for i in CCE.values()],
            'price': [i for i in Price.values()]
        })

        # Lets give an option to upload an excel file.
        st.markdown("<h6 style='text-align: left; font-size:25px; --hover-color: #eee '>Upload a CSV file</h6>", unsafe_allow_html=True)
        uploadcond = st.checkbox("**_Check to read instructions and proceed!_**", label_visibility='collapsed')
        uploadfile = None
        if uploadcond:
            st.write("**:blue[Your file should look like this. The number of rows depends on the number of your samples]**")
            # A demo file used to show the users how their file should be
            st.dataframe(pd.DataFrame({"Lime Source":"Sample1", "Initial (g)": 100, "> #10 (g)": 10, "< #10": 90,"< #50 (g)":60,
            "cce": 97.8,  'price': 20}, index =[1]))
            subcontainer1= st.container()
            # Lets give some instructions to users how to create file and how it should look like
            subcontainer1.markdown("""
            <div style="text-align: justify;">
            <span style='color: #0033A0; font-weight: bold; '>Tips:</span> Your file must be an excel.csv file with a tabular format. To create a CSV file, 
            open excel, spreadsheet (Google), or numbers (Mac). The first row must be the header row. 
            The file must have "7 columns" in order of "Column A: Lime Source", "Column B: Initial amount (g) of lime sample", "Column C: The amount (g) of lime retained 
            in #10 Sieve", "Column D: The amount (g) of lime passed through #10 Sieve", "Column E: The amount (g) of lime passed through #50 Sieve", 
            "Column F: CCE", and "Column G: price per ton". You can give any name to the headers. If the water pH and buffer pH are unknown, 
            use default values of 4.5 and 5.5 for all your samples, respectively. The default value of CCE is 90 and the default value of price is 20. 
            Once you insert values, press Ctrl + S or cmd + S. A file saving window will appear. Name your file and change the extension of 
            your file from ".xlsx" to ".csv" and then save it. 
            Keep in mind that in the case of default values, the calculations and graphs for the default parameters, as you know, are incorrect.
            Default values are used to run the model smoothly. They have no scientific meaning. If an "error" 
            occurs, please double check that that you have selected the correct type of data (weight based or percentage-based) at the 
            top of the App and check if the number of columns and the extension of the file is correct.
            </div>
            """, unsafe_allow_html=True)
            uploadfile = st.file_uploader("")
        else:
            pass
        # Lets give a condition if the upload file exist or not. If it exists then make it read it. 
        if uploadfile is not None:
            st.success("**File uploaded successfully!**")
            df = pd.read_csv(uploadfile)
            df.columns= ["Quarry", "initial", "gten", "lten", "lfifty", 'cce', 'price']
            st.write(df.head())
            st.caption("**:red[Here are the first five rows of your data]**")
        else:
            pass


        # adding  columns with new calculations
        df["Zero%_eff"] = (df.gten/df.initial)*100
        df['Fifty%_eff'] = ((((df.lten-df.lfifty)))/df.initial)*100
        df['Hund%_eff'] = (df.lfifty/df.initial)*100
        df["RNV"] = df.cce/100.00*((((df.lten-df.lfifty)/2.0)+df.lfifty)/df.initial)*100

        SWPH = wph
        BPH = bph
        TPH = tph
        SW  = 12
        RNV = df.RNV
        part1 = -1.1 *(TPH-SWPH)*(BPH-7.55)
        part2  = (BPH -(1.1*SWPH)+1.47)
        part3 = 13.75/SW
        ELR = part1/part2*part3
        cffa = [(3.62 - (0.734*ELR)) if ELR <=3 else 1.42][0]
        pure_lime = cffa*ELR 

        # if TPH> SWPH:
        #     if 3<(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW):
        #         df['Bulk_Rec'] = 1.42*(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW)/RNV
        #     else:
        #         df['Bulk_Rec'] = (3.62-(0.734*(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW)))*(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW)/(RNV/100)
        # else:
        #     df['Bulk_Rec'] = 0
        df['Bulk_Rec'] = pure_lime/df.RNV*100 if TPH>SWPH else df.RNV *0
        df['Cost'] = df.Bulk_Rec * df.price

# Lab results based on percentage
    if percent_weight == "Lab Results (Percentage)":
        f_container = st.container()
        samp_cont1, samp_cont2 = f_container.columns([1, 3])
        samp_cont1.markdown("<h5 style='text-align: center; color: blue;'>" "</h5>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: white; background-color: #0033A0;'>Lime Data</h4>", unsafe_allow_html=True)
        samp_cont1.markdown("<h5 style='text-align: center; color: white; background-color: #0033A0;'># Samples</h5>", unsafe_allow_html=True)
        ncol = samp_cont1.number_input("# Sample", 1, 5, 2, key = 'first', label_visibility='collapsed')
        cols = st.columns(ncol)
        for i, x in enumerate(cols):
            quarries[i]= x.text_input('**Lime Source:**', value = f'Sample {i+1}', key = f"q_{i}_name")
            gten[i] = x.number_input('**% > #10:**', value = 10.00, key = f"q_{i}_10", format="%.2f")
            lfifty[i] = x.number_input('**% < #50:**', value = 60.00, key = f"q_{i}_50", format="%.2f")
            CCE[i] = x.number_input("**Culcium Carbonate Equivalent (CCE):**", value = 90.0, key = f'cce{i}', format="%.1f")
            Price[i] = x.number_input("**Price ($/ton):**", value = 20.0, key = f'price{i}', format="%.1f")

        st.markdown("<h4 style='text-align: center; color: white; background-color: #0033A0;'>Soil Data </h4>", unsafe_allow_html=True)
        s_container = st.container()
        c1, c2, c3= s_container.columns(3)
        wph = c1.slider('**Soil Water pH:**', min_value=4.0, max_value=8.0, value=5.8, step=0.1, key='wph', format="%.1f")
        bph = c2.slider('**Buffer pH (Sikora-2):**', min_value=4.0, max_value=8.0, value=6.5, step=0.1, key='bph', format="%.1f")
        tph= c3.slider('**Target pH**', min_value=4.0, max_value=8.0, value=6.5, step=0.1, key='tph', format="%.1f")
        # soilW = c4.slider('**Soil Weight (g):**',min_value=8.0, max_value=14.0, value=12.0, step=0.1, key='sw', format="%.1f")

        # This datafram is dynamic and therefore making the charts easy to plot

        df = pd.DataFrame({"Quarry": [i for i in quarries.values()],
            "gten":[i for i in gten.values()],
            "lten": [i-j for i, j in zip([100 for i in gten.values()], gten.values())],
            "lfifty": [i for i in lfifty.values()],
            'cce': [i for i in CCE.values()],
            'price': [i for i in Price.values()]
        })

        # Lets give an option to upload an excel file
        st.markdown("<h6 style='text-align: left; font-size:25px; --hover-color: #eee '>Upload a CSV file</h6>", unsafe_allow_html=True)
        uploadcond = st.checkbox("**_Check to read instructions and proceed!_**", label_visibility='collapsed')
        uploadfile = None
        if uploadcond:
            st.write("**:blue[Your file should look like this. The number of rows depends on the number of your sample]**")
            # A demo data frame
            st.dataframe(pd.DataFrame({"Lime Source":"Sample1","> #10 (%)": 10, "< #10 (%)":90,
            "< #50 (%)": 60, "cce": 97.8, 'price': 20}, index =[1]))
            subcontainer1= st.container()
            # instruction on how to create a file
            subcontainer1.markdown("""
            <div style="text-align: justify;">
            <span style='color: #0033A0; font-weight: bold;'>Tips:</span> Your file must be an excel.csv file with a tabular format. The first row must be the header row. 
            The file must have "6 columns" in order of "Column A: Source names", "Column B: Percent of lime retained 
            in #10 Sieve", "Column C: Percent of lime passed through #10 Sieve", "Column D: Percent of lime passed through #50 Sieve", 
            "Column E: CCE", and "Column F: price per ton". Once you insert values, press Ctrl + S or cmd + S. A file saving window will appear. 
            Name your file and change the extension of your file from ".xlsx" to ".csv" and then save it. 
            You can give any name to headers. <br /> If the water pH and buffer pH are unknown, 
            use the default values of 4.5 and 5.5 for all your samples, respectively. The default value of CCE is 90 and the default value of price is 20. 
            The remaining columns are automatically calculated. In the case of default values, the calculations and graphs for the default parameters, as you know, are incorrect.
            Default values are used to run the model smoothly. They have no scientific meaning. If an "error" 
            occurs, please double check that you have selected the correct type of data (weight based or percentage-based) at the 
            top of the App and check if the number of columns and the extension of the file is correct.
            </div>
            """, unsafe_allow_html=True)
            uploadfile = st.file_uploader("")
        else:
            pass
        # upload a file if it exists. Skip if it doesn't 
        if uploadfile is not None:
            st.success("**File uploaded successfully!**")
            df = pd.read_csv(uploadfile)
            df.columns= ["Quarry", "gten", "lten", "lfifty", "wph", "bph", 'cce', 'price']
            st.write(df.head())
            st.caption("**:red[Here are the first few rows of your data]**")
        else:
            pass


        # adding  columns with new calculations
        df["Zero%_eff"] = df.gten
        df['Fifty%_eff'] = (df.lten-df.lfifty)
        df['Hund%_eff'] = df.lfifty
        df["RNV"] = df.cce/100.00*(((df.lten-df.lfifty)/2.0)+df.lfifty)
        SWPH =wph
        BPH = bph
        TPH = tph
        SW  = 12
        RNV = df.RNV
        part1 = -1.1 *(TPH-SWPH)*(BPH-7.55)
        part2  = (BPH -(1.1*SWPH)+1.47)
        part3 = 13.75/SW
        ELR = part1/part2*part3 #Equation LR
        cffa = [(3.62 - (0.734*ELR)) if ELR <=3 else 1.42][0]
        pure_lime = cffa*ELR 

        # if TPH> SWPH:
        #     if 3<(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW):
        #         df['Bulk_Rec'] = 1.42*(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW)/RNV
        #     else:
        #         df['Bulk_Rec'] = (3.62-(0.734*(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW)))*(-1.1*(TPH-SWPH)*(BPH-7.55)/(BPH-(1.1*SWPH)+1.47)*13.75/SW)/(RNV/100)
        # else:
        #     df['Bulk_Rec'] = 0
        df['Bulk_Rec'] = pure_lime/df.RNV*100 if TPH > SWPH else df.RNV * 0
        df['Cost'] = df.Bulk_Rec * df.price
        


# title for the fineness of the lime and its RNV
    # Lets create color pallete for our charts. There are over 100 color pallete to choose from
    # So one can pick up a color s/he wants
    st.markdown("<h3 style='text-align: center; color: blue;'>" "</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>" "</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='background-color: #0033A0; text-align: center; color: 	white;'>Lime Particles and RNV</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>" "</h3>", unsafe_allow_html=True)
    color_cont1, color_cont2 = st.columns([1, 2])
    color_cont1.markdown("<h5 style='text-align: center; color: white; background-color: #0033A0;'>Choose color palette</h5>", unsafe_allow_html=True)

    # colcol,_,_ = st.columns(3)
    pallete = color_cont1.selectbox("pallete", ["Dark2","Accent", "Accent_r", "autumn", "Blues", "Blues_r", "bright", "BuGn", 
    "BuGn_r", "BuPu", "BuPu_r", "binary", "binary_r", "bone", "bone_r", "bwr", "colorblind",  "cool", "coolwarm", "copper", "cubehelix", "dark",
    "Dark2_r", "deep","GnBu", "GnBu_r", "gnuplot" ,"gnuplot2","Greens", "Greens_r", "Greys", "Greys_r" ,"gray", "hot", "hot_r" ,"jet_r","nipy_spectral", "muted",
    "OrRd", "OrRd_r","ocean", "ocean_r" ,"Oranges", "Oranges_r", "PRGn", "PRGn_r", "pink", "pink_r" ,"Paired", "Paired_r","pastel", "Pastel1", "Pastel1_r",
    "Pastel2", "Pastel2_r", "PiYG", "PiYG_r",  "PuBu", "PuBuGn", "PuBuGn_r", "PuBu_r", "PuOr", "PuOr_r", "PuRd", "PuRd_r",
    "Purples", "Purples_r","rainbow","rainbow_r" ,"RdBu", "RdBu_r", "RdGy", "RdGy_r", "RdPu", "RdPu_r", "RdYlBu", "RdYlGn", "Reds", "Reds_r", "Set1", "Set1_r",
    "Set2", "Set2_r", "Set3", "Set3_r", "Spectral", "Spectral_r" , "seismic", "seismic_r" ,"spring","spring_r", "summer","summer_r", "YlGn", "YlGnBu", "YlOrBr", "YlOrRd",
    "prism", "terrain", "terrain_r","winter", "winter_r"], label_visibility ='collapsed')

    # Lets give some dynamic condisiton to the charts. 
    # How they should resize if the number of samples is more than five. a fixed width creates problem
    @st.cache
    def graph_h():
        if df.shape[0]>5:
            eff_h = 5+(df.shape[0]-5)*0.45
            others = 2+(df.shape[0]-2)*0.15
            rotation = 0
            data_labels = 'edge'
            return eff_h, others, rotation, data_labels
        else:
            return 5,  2, 0, 'edge'
    eff_h, others, rotation, data_labels= graph_h()

    # By default the charts are not shown. So if someone wants to see charts, they check the box and then the graphs 
    # appear. 
    fig,(ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (7, eff_h), sharex=True, gridspec_kw={'hspace':0.15})
    Fplot = sns.barplot(x = "Zero%_eff", y = 'Quarry', data=df, ax=ax1, palette=pallete)
    ax1.set_ylabel(None)
    ax1.set_xlabel(None)
    ax1.axes.xaxis.set_visible(False)
    ax1.text(0.45, -0.11, s="#10 Seive", transform = ax1.transAxes)
    ax1.text(0.95, 0.18+eff_h*0.012, "RNV (0%)", rotation =270, transform= ax1.transAxes)
    ax1.bar_label(Fplot.containers[0], fmt="%.2f", rotation =0)
    ax1.set_title("Lime Fineness (%)", fontsize = 18)


    Splot =sns.barplot(x = "Fifty%_eff", y = 'Quarry', data=df, ax=ax2, palette=pallete)
    ax2.set_ylabel(None)
    ax2.set_xlabel(None)
    ax2.axes.xaxis.set_visible(False)
    ax2.text(0.45, -0.11, s="#50 Seive", transform = ax2.transAxes)
    ax2.text(0.95, 0.18+eff_h*0.012, "RNV (50%)", rotation =270, transform= ax2.transAxes)
    ax2.bar_label(Splot.containers[0], fmt="%.2f", rotation = 0)


    Tplot = sns.barplot(x = "Hund%_eff", y = 'Quarry', data=df, ax=ax3, palette=pallete)
    ax3.set_xlim((0, 100))
    ax3.set_ylabel(None)
    ax3.set_xlabel(None)
    ax3.text(0.95, 0.18+eff_h*0.012, "RNV (100%)", rotation =270, transform= ax3.transAxes)
    ax3.bar_label(Tplot.containers[0],fmt="%.2f", rotation = 0)
    ax3.set_xlabel("", fontsize = 14)
    ax3.axes.xaxis.set_visible(False)
    ax3.set_xticklabels([])

    rect = plt.Rectangle(
        # (lower-left corner), width, height
        (0.1232, 0.11), 0.776, 0.77, fill=False, color="k", lw=1, 
        zorder=1000, transform=fig.transFigure, figure=fig
    )
    fig.patches.extend([rect]);

    # plot for RNV_______________

    fig1, ax4= plt.subplots(figsize = (7,others))
    ax4.set_xlabel('RNV (%)')
    ax4.set_ylabel(None)
    ax4.set_title("Relative Neutralizaing Value (RNV (%))", fontsize = 18)

    FrPlot = sns.barplot(x='RNV', y = 'Quarry', data=df, ax=ax4, palette=pallete)
    ax4.set_xlim((0, 100))
    ax4.bar_label(FrPlot.containers[0], fmt="%.2f", rotation=0)
    ax4.set_ylabel(None)
    ax4.set_xlabel("", fontsize = 14)
    ax4.axes.xaxis.set_visible(False)
    ax4.set_xticklabels([])
    st.pyplot(fig)
    st.pyplot(fig1)


    # Plot for Bulk Recommendation of  Lime
    st.markdown("<h3 style='text-align: center; color: blue;'>" "</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>" "</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>" "</h3>", unsafe_allow_html=True)

    st.markdown("<h5 style='background-color: #0033A0; font-size:35px; text-align: center; color: 	white;'>Lime Recommendation and Application Cost</h5>", unsafe_allow_html=True)

    # Here I also want to give an option 
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    fig2, ax5 = plt.subplots(figsize =(7,others) )
    ax5.set_ylabel(None)
    ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\nto raise soil water pH of {SWPH} to a target pH of {TPH}", fontsize = 14)

    FiPlot = sns.barplot(x='Bulk_Rec', y = 'Quarry', data=df, ax=ax5, palette=pallete)
    ax5.bar_label(FiPlot.containers[0], fmt="%.2f", rotation = rotation, label_type=data_labels)
    ax5.set_ylabel(None)
    ax5.set_xlim([0, max(df.Bulk_Rec)+max(df.Bulk_Rec)*0.1]) # This syntax max the x axis length dynamic. Without it the data lable makes a problem
    ax5.set_xlabel("", fontsize = 14)
    ax5.axes.xaxis.set_visible(False)
    ax5.set_xticklabels([])
        
        # Plot for Cost of  Lime

    fig3, ax6 = plt.subplots(figsize =(7,others) )
    ax6.set_ylabel(None)
    ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\nto raise soil water pH of {SWPH} to a target pH of {TPH}", fontsize = 14)

    SiPlot = sns.barplot(x='Cost', y = 'Quarry', data=df, ax=ax6, palette=pallete)
    ax6.bar_label(SiPlot.containers[0], fmt="%.2f", rotation = rotation, label_type=data_labels)
    ax6.set_ylabel(None)
    ax6.set_xlabel(None)
    ax6.set_xlim([0, max(df.Cost)+max(df.Cost)*0.1])
    ax6.axes.xaxis.set_visible(False)
    ax6.set_xticklabels([])
    st.pyplot(fig2)
    st.pyplot(fig3)

    st.markdown("<h3 style='text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='background-color: #0033A0; font-size:35px; text-align: center; color: 	white;'>Output File</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>""</h3>", unsafe_allow_html=True)

    # Lets generate a datetime stamp. This is used for saving file. SO each time you save a file, the date of the 
    # will be automatically attached to your file's name. So you can later on see and refernce each measurement and keep track of it.
    date1, _,_,_,_ = st.columns(5)

    date1.markdown("<h5 style=' background-color: #0033A0; text-align: center; color: white;'>Date</h5>", unsafe_allow_html=True)

    date = date1.date_input("date", label_visibility='collapsed')
    time = datetime.datetime.now().time()
    st.dataframe((df.set_index('Quarry').style.format("{:.2f}")))
    st.caption("**:blue[This dataframe is interactive, You can scroll left-to-right or top-to-bottom. Please download the file before navigating to another manu. You will lose the data otherwise!]**")

# Preparing data to download
    df1 = df.to_csv().encode('utf-8')
    # this checkbox will allow us to download data
    st.markdown("### **:blue[Download!]**")
    st.download_button(
        key = 'b_csv',
        label = "Download data as csv file",
        data = df1,
        file_name = f"Lime_particle_analysis_[{date}]_[{time}].csv",
        mime = 'text/csv'
    )
    st.caption(":red[Note that a default dataset, corresponding to the number of open slots, is downloaded if you don't insert values in the form or don't upload  a file]")

        
# If someone wants to tell us about it or give us suggestions
if selected1 =='Contact':
    contact_col1, contact_col2= st.columns(2)
    with contact_col1:
        contact_col1.markdown("<h4 style='background-color: #0033A0; text-align: center; color: 	white;'>Robbie Williams</h2>", unsafe_allow_html=True)
        contact_form = """
        <form action="https://formsubmit.co/rwilliamsfarms@bellsouth.net" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name"required>
        <input type="email" name="email" placeholder = "Email Address" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html = True)
        def local_css(file_name):
            with open(file_name) as f:
                contact_col1 .markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
        local_css("style.css")
    with contact_col2:
        contact_col2.markdown("<h4 style='background-color: #0033A0; text-align: center; color: 	white;'>Mohammad Shamim</h2>", unsafe_allow_html=True)
        contact_form = """
        <form action="https://formsubmit.co/shamim.one@outlook.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name"required>
        <input type="email" name="email" placeholder = "Email Address" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html = True)
        def local_css(file_name):
            with open(file_name) as f:
                contact_col2 .markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
        local_css("style.css")