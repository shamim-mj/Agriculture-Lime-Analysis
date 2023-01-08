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
    selected1 = option_menu("", ["Home", "Calculator", 'Instructions', "Contact"], 
        icons=['house', 'calculator', 'book', 'person lines fill'], 
        menu_icon="cast", default_index=0, #orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
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
    st.markdown("<h2 style='background-color: #00FF00; text-align: center; color: 	black;'>Lime Calculator with Color Charts</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: 	black;'>Particle Analysis, CCE, RNV, pH, Buffer pH, Rates, and Cost/Acre</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: 	black;'>All rights reserved. </h6>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: 	black;'> This web application was developed by Mohammad Shamim, Ph.D., and Robbie Williams in Henderson, Kentucky, USA.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: 	black;'> Please read the instructions carefully before proceeding. Calculations can be determined either by manually inserting values into the cells below or by uploading the values in an Excel file. The manual form allows up to five lime source calculations. Uploading an Excel file allows an unlimited number of lime source calculations. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color: 	black;'>Be sure to check boxes/toggle buttons for desired calculations as graphs. This web app uses Sikora-2 buffer for determining the quantity and cost of  lime to be applied in an acre.</p>", unsafe_allow_html=True)
    image1, image2 = st.columns(2)
    img1 = plt.imread('Lime particles .jpg')
    img2 = plt.imread('Sieves1.jpg')
    image1.image(img2)
    image2.image(img1)





# This data is important for finding the 100 % effective amount of lime with relevant PH
# We will alos use the experimental_memo so it is not run repeatedly.
# This data is taken directly from a paper published by Dr. Sikora Laboratory at the Univesity of Kentucky
@st.experimental_memo
def data_generate(ph = 6.4):
    if ph in [6.4, 6.6]:
        data ={
            
            '5.5': [4.67,4.67,4.67,4.67,4.67,4.0,4.0,"",""],
            "5.7": [4.0, 4.0, 4.0, 4.0, 4.0, 3.33, 3.33,3.33, ""],
            "5.9": [4.0, 4.0, 4.0, 3.33, 3.33, 3.33, 2.67, 2.67, 2.0],
            "6.1": [3.33, 3.33, 3.33, 3.33, 2.67, 2.67, 2.67, 2.0, 2.0],
            "6.3": [2.67,2.67,2.67,2.67,2.67,2.67,2.0, 2.0, 1.33], 
            "6.5": [2.67,2.67,2.67,2.0, 2.0, 2.0, 2.0, 1.33, 1.33],
            "6.7": [2.0, 2.0,2.0,2.0,2.0, 1.33, 1.33, 1.33, 0.67],
            "6.9": [2.0, 2.0, 2.0, 1.33, 1.33, 1.33, 1.33, 0.67, 0.67],
            "NA" : [2.67,2.67,2.67,2.67, 2.33, 2.0, 1.67, 1.33,1.00]
        }
        index = [4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 5.7, 5.9, 6.1]
        return pd.DataFrame(data=data, index= index)
    elif ph ==6.8:
        data2 ={
        
        '5.5': [4.67,4.67,4.67,4.67,4.67,4.67,4.67,"","", "", ""],
        "5.7": [4.67,4.67,4.67,4.67,4.67,4.67,4.67, 4.0,"", "", ""],
        "5.9": [4.67,4.67,4.67,4.67,4.67,4.00,4.00,3.33, 3.33, "", ""],
        "6.1": [4.00, 4.00, 4.00, 4.00, 4.00, 3.33, 3.33, 3.33, 2.67, 2.00, ""],
        "6.3": [3.33,3.33, 3.33, 3.33, 3.33, 3.33, 3.33, 2.67, 2.67, 2.00, 1.33], 
        "6.5": [3.33,3.33, 3.33, 3.33,2.67, 2.67,2.67, 2.67, 2.00, 2.00, 1.33],
        "6.7": [2.67, 2.67,2.67, 2.67,2.00, 2.00,2.00, 2.00, 1.33, 1.33, 1.33],
        "6.9": [2.00, 2.00,2.00, 2.00,2.00, 2.00,1.33, 1.33, 1.33, 0.67, 0.67],
        "NA" : [4.00, 4.00, 4.00, 4.00, 3.67, 3.33, 3.00, 2.33, 2.00, 1.67, 1.33]
        }
        index1 = [4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 5.7, 5.9, 6.1, 6.3, 6.5]
        return pd.DataFrame(data=data2, index= index1)

#Lets generate data using the fuction we just made.
pdf = data_generate(ph=6.4)
pdf66 = data_generate(ph=6.6)
pdf68 = data_generate(ph=6.8)

if selected1=="Calculator":
    # Add a tile to the sources of the lime
    st.markdown("<h3 style='background-color: #00FF00; font-size:35px; text-align: center; color: 	black;'>Lime Sources and Data</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)
    


    # Lets make some empty dictionary to save data
    # This is used to loop through the data in dynamic columns. You can use pandas dataframe directly too. 

    quarries = {}
    initial ={}
    gten  = {}
    # lten = {}
    lfifty = {}
    wph = {}
    bph = {}
    CCE = {}
    Price ={}
    

    # Lets give the users option. In some cases the users may do the analysis themselves and know the weight of the sammpls
    # in other cases the users recieve data from special laboratories and the laboratories only give them data in percentage, not weight
    # So we have option for either case.
    percent_weight = option_menu(None, ["Lab Results (Weight)", "Lab Results (Percentage)"], 
        icons=[], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )






    # percent_weight = st.radio("**Is your result based on percentage or weight?**", options =("Lab Results (Weight)", "Lab Results (Percentage)"))

    # Lets make the columns or slots dynamic

    # Telling the user wheather s/he wants to enter the data manually (convinient for smartphone)
    st.markdown("<h2 style='text-align: center; color: blue; font-size:25px; background-color: yellow; margin: 0px'>Manual Input</h2>", unsafe_allow_html=True)
    samp_cont1, samp_cont2 = st.columns([1, 3])
    samp_cont1.markdown("<h5 style='text-align: center; color: blue;'>" "</h5>", unsafe_allow_html=True)

    samp_cont1.markdown("<h5 style='text-align: center; color: white; background-color: black;'>Number of Samples</h5>", unsafe_allow_html=True)

    ncol = samp_cont1.number_input("", 1, 5, 2, label_visibility='collapsed')
    cols = st.columns(ncol)



    # Here, I am setting a condition if the data is in percentage or weight
    # Lets loop through the columns
    if percent_weight =="Lab Results (Weight)":
        for i, x in enumerate(cols):
            # st.markdown("<h2 style='text-align: center; color: blue;'>Lime Data</h2>", unsafe_allow_html=True)

            quarries[i]= x.text_input('**Lime Source:**', value = f'Sample {i+1}',key = f"q_{i}_name")
            initial[i] = x.number_input('**Initial Amount (g)**: ', value = 100.00, key = f"q_{i}_initial", format="%.2f")
            gten[i] = x.number_input('**Amount > #10 (g)**: ', value = 10.00, key = f"q_{i}_10", format="%.2f")
            lfifty[i] = x.number_input('**Amount < #50 (g):**', value = 60.00, key = f"q_{i}_50", format="%.2f")
        # for i, x in enumerate(cols):
            CCE[i] = x.number_input("**Culcium Carbonate Equivalent (CCE):** ", value = 90.0, key = f'cce{i}', format="%.1f")
            wph[i] = x.selectbox('**Soil Water pH:**', options = [5.7,4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 5.9, 6.1, 6.3, 6.5], key = f"q_{i}_wph")
            bph[i] = x.selectbox('**Buffer pH (Sikora-2):**', options = [6.3, 5.5, 5.7, 5.9, 6.1, 6.5, 6.7, 6.9, "NA"], key = f"q_{i}_bph")

            Price[i] = x.number_input("**Price ($/ton)**", value = 20.0, key = f'price{i}', format="%.1f")

        # This datafram is dynamic and therefore making the charts easy to plot

        df = pd.DataFrame({"Quarry": [i for i in quarries.values()],
            "initial": [i  for i in initial.values()], 
            "gten":[i for i in gten.values()],
            "lten": [i-j for i, j in zip(initial.values(), gten.values())],
            "lfifty": [i for i in lfifty.values()],
            "wph": [i for i in wph.values()],
            "bph": [i for i in bph.values()], 
            'cce': [i for i in CCE.values()],
            'price': [i for i in Price.values()]
        })

        # Lets give an option to upload an excel file.
        st.markdown("<h2 style='text-align: center; color: blue; font-size:25px; background-color: yellow;'>Upload a CSV file</h2>", unsafe_allow_html=True)
        uploadcond = st.checkbox("**_Check to read instructions and proceed!_**")
        uploadfile = None
        if uploadcond:
            st.write("**:blue[Your file should look like this. The number of rows depends on the number of your samples]**")
            # A demo file used to show the users how their file should be
            st.dataframe(pd.DataFrame({"Lime Source":"Sample1", "Initial (g)": 100, "> #10 (g)": 10, "< #10": 90,"< #50 (g)":60,
            "wph": 4.5, "bph":5.4, "cce": 90, 'price': 20}, index =[1]))
            subcontainer1= st.container()
            # Lets give some instructions to users how to create file and how it should look like
            subcontainer1.markdown("""
            <div style="text-align: justify;">
            <span style='color: green; font-weight: bold; '>Tips:</span> Your file must be an excel.csv file with a tabular format. To create a CSV file, 
            open excel, spreadsheet (Google), or numbers (Mac). The first row must be the header row. 
            The file must have "9 columns" in order of "Column A: Lime Source", "Column B: Initial amount (g) of lime sample", "Column C: The amount (g) of lime retained 
            in #10 Sieve", "Column D: The amount (g) of lime passed through #10 Sieve", "Column E: The amount (g) of lime passed through #50 Sieve", 
            "Column F: Water pH", "Column G: Buffer pH", "Column H: CCE", and "Column I: Price per ton". You can give any name to the headers. If the water pH and buffer pH are unknown, 
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
            df.columns= ["Quarry", "initial", "gten", "lten", "lfifty", "wph", "bph", 'cce', 'price']
            st.write(df.head())
            st.caption("**:red[Here are the first five rows of your data]**")
        else:
            pass


        # adding  columns with new calculations
        df["Zero%_eff"] = (df.gten/df.initial)*100
        df['Fifty%_eff'] = ((((df.lten-df.lfifty)))/df.initial)*100
        df['Hund%_eff'] = (df.lfifty/df.initial)*100
        df["RNV"] = df.cce/100.00*((((df.lten-df.lfifty)/2.0)+df.lfifty)/df.initial)*100
        df['Hun_eff_lime64'] = [pdf.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]
        # For some PH values,there is no 100 percent effective lime. Model will throug an error so we need to tweek it to a default value
        if "" in [i for i in df.Hun_eff_lime64]:
            phvs = df.loc[df.Hun_eff_lime64=="", ["wph", "bph"]]
            st.write(f"**:red[Warning!: For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.4 is not calculated. A default value of 3.33 is used.]**")
            df['Hun_eff_lime64'] = [3.33 for i in range(df.shape[0])]

        df['Hun_eff_lime66'] = [pdf66.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

        if "" in [i for i in df.Hun_eff_lime66]:
            phvs = df.loc[df.Hun_eff_lime66=="", ["wph", "bph"]]
            st.write(f"**:red[Warning!: For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.6 is not calculated. A default value of 3.33 is used.]**")
            df['Hun_eff_lime66'] = [3.33 for i in range(df.shape[0])]

        df['Hun_eff_lime68'] = [pdf68.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

        if "" in [i for i in df.Hun_eff_lime68]:
            phvs = df.loc[df.Hun_eff_lime66=="", ["wph", "bph"]]
            st.write(f"**:red[Warning!: For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.6 is not calculated. A default value of 3.33 is used.]**")
            df['Hun_eff_lime68'] = [3.33 for i in range(df.shape[0])]


        df['Bulk_Rec64'] = (df.Hun_eff_lime64/df.RNV)*100
        df['Bulk_Rec66'] = (df.Hun_eff_lime66/df.RNV)*100
        df['Bulk_Rec68'] = (df.Hun_eff_lime68/df.RNV)*100
        df['Cost64'] = df.price*df['Bulk_Rec64']
        df['Cost66'] = df.price*df['Bulk_Rec66']
        df['Cost68'] = df.price*df['Bulk_Rec68']
        st.session_state['df'] = df

    # here the file is generated for percentage-based data
    if percent_weight == "Lab Results (Percentage)":
        for i, x in enumerate(cols):
            quarries[i]= x.text_input('**Lime Source:**', value = f'Sample {i+1}', key = f"q_{i}_name")
            gten[i] = x.number_input('**% > #10:**', value = 10.00, key = f"q_{i}_10", format="%.2f")
            lfifty[i] = x.number_input('**% < #50:**', value = 60.00, key = f"q_{i}_50", format="%.2f")
            CCE[i] = x.number_input("**Culcium Carbonate Equivalent (CCE):**", value = 90.0, key = f'cce{i}', format="%.1f")
            wph[i] = x.selectbox('**Soil Water pH:**', options = [5.7,4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 5.9, 6.1, 6.3, 6.5], key = f"q_{i}_wph")
            bph[i] = x.selectbox('**Buffer pH (Sikora-2):**', options = [6.3, 5.5, 5.7, 5.9, 6.1, 6.5, 6.7, 6.9, "NA"], key = f"q_{i}_bph")
            Price[i] = x.number_input("**Price ($/ton):**", value = 10.0, key = f'price{i}', format="%.1f")

        # This datafram is dynamic and therefore making the charts easy to plot

        df = pd.DataFrame({"Quarry": [i for i in quarries.values()],
            "gten":[i for i in gten.values()],
            "lten": [i-j for i, j in zip([100 for i in gten.values()], gten.values())],
            "lfifty": [i for i in lfifty.values()],
            "wph": [i for i in wph.values()],
            "bph": [i for i in bph.values()], 
            'cce': [i for i in CCE.values()],
            'price': [i for i in Price.values()]
        })

        # Lets give an option to upload an excel file
        st.markdown("<h2 style='text-align: center; color: blue; font-size:25px; background-color: yellow;'>Upload a CSV file</h2>", unsafe_allow_html=True)
        uploadcond = st.checkbox("**Check to read the instruction and proceed!**")
        uploadfile = None
        if uploadcond:
            st.write("**:blue[Your file should look like this. The number of rows depends on the number of your sample]**")
            # A demo data frame
            st.dataframe(pd.DataFrame({"Lime Source":"Sample1","> #10 (%)": 10, "< #10 (%)":90,
            "< #50 (%)": 60, "wph": 4.5, "bph":5.4, "cce": 90, 'price': 20}, index =[1]))
            subcontainer1= st.container()
            # instruction on how to create a file
            subcontainer1.markdown("""
            <div style="text-align: justify;">
            <span style='color: green; font-weight: bold;'>Tips:</span> Your file must be an excel.csv file with a tabular format. The first row must be the header row. 
            The file must have "8 columns" in order of "Column A: Source names", "Column B: Percent of lime retained 
            in #10 Sieve", "Column C: Percent of lime passed through #10 Sieve", "Column D: Percent of lime passed through #50 Sieve", 
            "Column E: Water pH", "Column F: Buffer pH", "Column G: CCE", and "*Column H: Price per ton". Once you insert values, press Ctrl + S or cmd + S. A file saving window will appear. 
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
            st.caption("**:red[Here are the first five rows of your data]**")
        else:
            pass


        # adding  columns with new calculations
        df["Zero%_eff"] = df.gten
        df['Fifty%_eff'] = (df.lten-df.lfifty)
        df['Hund%_eff'] = df.lfifty
        df["RNV"] = df.cce/100.00*(((df.lten-df.lfifty)/2.0)+df.lfifty)
        df['Hun_eff_lime64'] = [pdf.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]
        # For some PH values,there is no 100 percent effective lime. Model will throug an error so we need to correct it
        if "" in [i for i in df.Hun_eff_lime64]:
            phvs = df.loc[df.Hun_eff_lime64=="", ["wph", "bph"]]
            st.write(f"**:red[Warning!: For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.4 is not calculated. A default value of 3.33 is used.]**")
            df['Hun_eff_lime64'] = [3.33 for i in range(df.shape[0])]

        df['Hun_eff_lime66'] = [pdf66.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

        if "" in [i for i in df.Hun_eff_lime66]:
            phvs = df.loc[df.Hun_eff_lime66=="", ["wph", "bph"]]
            st.write(f"**:red[Warning!: For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.6 is not calculated. A default value of 3.33 is used.]**")
            df['Hun_eff_lime66'] = [3.33 for i in range(df.shape[0])]

        df['Hun_eff_lime68'] = [pdf68.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

        if "" in [i for i in df.Hun_eff_lime68]:
            phvs = df.loc[df.Hun_eff_lime68=="", ["wph", "bph"]]
            st.write(f"**:red[Warning!: For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.8 is not calculated. A default value of 3.33 is used.]**")
            df['Hun_eff_lime68'] = [3.33 for i in range(df.shape[0])]


        df['Bulk_Rec64'] = (df.Hun_eff_lime64/df.RNV)*100
        df['Bulk_Rec66'] = (df.Hun_eff_lime66/df.RNV)*100
        df['Bulk_Rec68'] = (df.Hun_eff_lime68/df.RNV)*100
        df['Cost64'] = df.price*df['Bulk_Rec64']
        df['Cost66'] = df.price*df['Bulk_Rec66']
        df['Cost68'] = df.price*df['Bulk_Rec68']
    st.session_state['df'] = df

# title for the fineness of the lime and its RNV
    # Lets create color pallete for our charts. There are over 100 color pallete to choose from
    # So one can pick up a color s/he wants
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='background-color: #00FF00; font-size:35px; text-align: center; color: 	black;'>Lime Particles, RNV, Recommended Amount, and Application Cost Analysis</h5>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    color_cont1, color_cont2 = st.columns([1, 2])
    color_cont1.markdown("<h5 style='text-align: center; color: white; background-color: black;'>Choose color palette for graphs</h5>", unsafe_allow_html=True)

    # colcol,_,_ = st.columns(3)
    pallete = color_cont1.selectbox("", ["Dark2","Accent", "Accent_r", "autumn", "Blues", "Blues_r", "bright", "BuGn", 
    "BuGn_r", "BuPu", "BuPu_r", "binary", "binary_r", "bone", "bone_r", "bwr", "colorblind",  "cool", "coolwarm", "copper", "cubehelix", "dark",
    "Dark2_r", "deep","GnBu", "GnBu_r", "gnuplot" ,"gnuplot2","Greens", "Greens_r", "Greys", "Greys_r" ,"gray", "hot", "hot_r" ,"jet_r","nipy_spectral", "muted",
    "OrRd", "OrRd_r","ocean", "ocean_r" ,"Oranges", "Oranges_r", "PRGn", "PRGn_r", "pink", "pink_r" ,"Paired", "Paired_r","pastel", "Pastel1", "Pastel1_r",
    "Pastel2", "Pastel2_r", "PiYG", "PiYG_r",  "PuBu", "PuBuGn", "PuBuGn_r", "PuBu_r", "PuOr", "PuOr_r", "PuRd", "PuRd_r",
    "Purples", "Purples_r","rainbow","rainbow_r" ,"RdBu", "RdBu_r", "RdGy", "RdGy_r", "RdPu", "RdPu_r", "RdYlBu", "RdYlGn", "Reds", "Reds_r", "Set1", "Set1_r",
    "Set2", "Set2_r", "Set3", "Set3_r", "Spectral", "Spectral_r" , "seismic", "seismic_r" ,"spring","spring_r", "summer","summer_r", "YlGn", "YlGnBu", "YlOrBr", "YlOrRd",
    "prism", "terrain", "terrain_r","winter", "winter_r"], label_visibility ='collapsed')

    # df = st.session_state['df']
    # pallete = st.session_state['pallete']
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
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)

    st.markdown("<h5 style='background-color: #00FF00; font-size:35px; text-align: center; color: 	black;'>Lime Recommendation and Its Cost Based on Sikora-2 Buffer Method</h5>", unsafe_allow_html=True)

    # Here I also want to give an option 
    st.markdown("<h3 style='text-align: center; color: blue;'>""</h3>", unsafe_allow_html=True)
    tarph_cont1, tarph_cont2 = st.columns([1, 2])
    tarph_cont1.markdown("<h5 style='text-align: center; color: white; background-color: black;'>Target pH</h5>", unsafe_allow_html=True)
    target = tarph_cont1.selectbox("", [6.4, 6.6, 6.8], key = 'target', label_visibility='collapsed')
    # Becasue the amount of lime differs with a target pH, I want to give them options.
    if target==6.4:
        fig2, ax5 = plt.subplots(figsize =(7,others) )
        ax5.set_ylabel(None)
        ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH of {target}", fontsize = 14)

        FiPlot = sns.barplot(x='Bulk_Rec64', y = 'Quarry', data=df, ax=ax5, palette=pallete)
        ax5.bar_label(FiPlot.containers[0], fmt="%.1f", rotation = rotation, label_type=data_labels)
        ax5.set_ylabel(None)
        ax5.set_xlim([0, max(df.Bulk_Rec64)+max(df.Bulk_Rec64)*0.1]) # This syntax max the x axis length dynamic. Without it the data lable makes a problem
        ax5.set_xlabel("", fontsize = 14)
        ax5.axes.xaxis.set_visible(False)
        ax5.set_xticklabels([])
        
        # Plot for Cost of  Lime

        fig3, ax6 = plt.subplots(figsize =(7,others) )
        ax6.set_ylabel(None)
        ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH of {target}", fontsize = 14)

        SiPlot = sns.barplot(x='Cost64', y = 'Quarry', data=df, ax=ax6, palette=pallete)
        ax6.bar_label(SiPlot.containers[0], fmt="%.1f", rotation = rotation, label_type=data_labels)
        ax6.set_ylabel(None)
        ax6.set_xlabel(None)
        ax6.set_xlim([0, max(df.Cost64)+max(df.Cost64)*0.1])
        ax6.axes.xaxis.set_visible(False)
        ax6.set_xticklabels([])
        st.pyplot(fig2)
        st.pyplot(fig3)

    elif target ==6.6:
        fig2, ax5 = plt.subplots(figsize =(7,others) )
        ax5.set_ylabel(None)
        ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH of {target}", fontsize = 14)

        FiPlot = sns.barplot(x='Bulk_Rec66', y = 'Quarry', data=df, ax=ax5, palette=pallete)
        ax5.bar_label(FiPlot.containers[0], fmt="%.2f", rotation =rotation, label_type=data_labels)
        ax5.set_ylabel(None)
        ax5.set_xlim([0, max(df.Bulk_Rec66)+max(df.Bulk_Rec66)*0.1])
        ax5.set_xlabel("", fontsize = 14)
        ax5.axes.xaxis.set_visible(False)
        ax5.set_xticklabels([])

        # Plot for Cost of  Lime

        fig3, ax6 = plt.subplots(figsize =(7,others) )
        ax6.set_ylabel(None)
        ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH of {target}", fontsize = 14)

        SiPlot = sns.barplot(x='Cost66', y = 'Quarry', data=df, ax=ax6, palette=pallete)
        ax6.bar_label(SiPlot.containers[0], fmt="%.1f", rotation = rotation, label_type=data_labels)
        ax6.set_ylabel(None)
        ax6.set_xlabel(None)
        ax6.set_xlim([0, max(df.Cost66)+max(df.Cost66)*0.1])
        ax6.axes.xaxis.set_visible(False)
        ax6.set_xticklabels([])
        st.pyplot(fig2)
        st.pyplot(fig3)

    elif target ==6.8:
        fig2, ax5 = plt.subplots(figsize =(7,others) )
        ax5.set_ylabel(None)
        ax5.set_title("Bulk Recommendation of Lime (T/Acre)", fontsize = 18)

        FiPlot = sns.barplot(x='Bulk_Rec68', y = 'Quarry', data=df, ax=ax5, palette=pallete)
        ax5.bar_label(FiPlot.containers[0], fmt="%.2f",  rotation = rotation, label_type=data_labels)
        ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH of {target}", fontsize = 14)
        ax5.set_ylabel(None)
        ax5.set_xlim([0, max(df.Bulk_Rec68)+max(df.Bulk_Rec68)*0.1])

        # Plot for Cost of  Lime

        fig3, ax6 = plt.subplots(figsize =(7,others) )
        ax6.set_ylabel(None)
        ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH of {target}", fontsize = 14)

        SiPlot = sns.barplot(x='Cost68', y = 'Quarry', data=df, ax=ax6, palette=pallete)
        ax6.bar_label(SiPlot.containers[0], fmt="%.1f", rotation = rotation, label_type=data_labels)
        ax6.set_ylabel(None)
        ax6.set_xlabel(None)
        ax6.set_xlim([0, max(df.Cost68)+max(df.Cost68)*0.1])
        ax6.axes.xaxis.set_visible(False)
        ax6.set_xticklabels([])

        st.pyplot(fig2)
        st.pyplot(fig3)

# Lets give an option if someone wants to see the data rather than graphs

# st.markdown("<h3 style='text-align: center; color: blue;'> Output File</h3>", unsafe_allow_html=True)
# show_data = st.checkbox("Show data")
# if selected1=="Download":
    st.markdown("<h3 style='text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='background-color: #00FF00; font-size:35px; text-align: center; color: 	black;'>Output File</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=' text-align: center; color: 	black;'>""</h3>", unsafe_allow_html=True)

    df= st.session_state['df']
        # Lets generate a datetime stamp. This is used for saving file. SO each time you save a file, the date of the 
    # will be automatically attached to your file's name. So you can later on see and refernce each measurement and keep track of it.
    date1, _,_,_,_ = st.columns(5)

    date1.markdown("<h5 style=' background-color: black; text-align: center; color: white;'>Date</h5>", unsafe_allow_html=True)

    date = date1.date_input("", label_visibility='collapsed')
    time = datetime.datetime.now().time()
    st.dataframe((df.set_index('Quarry').style.format("{:.2f}")))
    st.caption("**:blue[This dataframe is interactive, You can scroll left-to-right or top-to-bottom. Please download the file before navigating to another manu. You will lose the data otherwise!]**")

# Preparing data to download
    df = df.to_csv().encode('utf-8')
    # this checkbox will allow us to download data
    st.markdown("### **:green[Download!]**")
    st.download_button(
        key = 'b_csv',
        label = "Download data as csv file",
        data = df,
        file_name = f"Lime_particle_analysis_[{date}]_[{time}].csv",
        mime = 'text/csv'
    )
    st.caption(":red[Note that a default dataset, corresponding to the number of open slots, is downloaded if you don't insert values in the form or don't upload  a file]")
    st.markdown("Generate Report")
# Instructions are important. If someone wants to read it, they can check the box. else the instructions are 
# hidden, which makes the App look cleaner.
# st.markdown("### **:green[Instructions]**")


if selected1=='Instructions':
        st.markdown("<h3 style='background-color: #00FF00; text-align: center; color: 	black;'>Instructions</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='background-color: white; text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)
        container2 = st.container()
        container2.markdown("""
        <div style="text-align: justify;">
        <span style='color: green; font-weight: bold;'>A) Using the App:</span> This web App has four menus. In the <span style='color: green; font-weight: bold;'>Home </span> manu, you can read about  the App and a brief introduction.
        The main menu is the <span style='color: green; font-weight: bold;'>Calculator </span> where you can input your data and calculate your  samples for 
        particle size,  RNV, lime amount recommendation, its application cost  per acre, and see the charts. Manually,  you can open up to 5 slots for your agricultural lime analysis. For example, if you are interested in analyzing 
        3 lime sources, you will select 3 from  the sample selector which is titled as "Number of Samples". 
        After that, the form will show 3 columns for you. You can populate the cells and see the charts. 
        Alternatively, you can upload a comma separated values (.csv) file with unlimited samples. 
        The default color of the charts is "Dark2" but you can choose from  over 100 colors from the drop-down list. To save a chart to your computer, right-click on the chart 
        and then choose "save image as" or "copy image" and then paste it as a picture in other places (press and hold in the case of a smartphone or iPad). To save data, 
        you will need to go to the <span style='color: green; font-weight: bold;'>Download </span> section in the "Calculator" menu. By clicking the download button,  
        the data will be saved to your machine automatically. In the data, you will see many columns. "Initial" is the initial weight of the sample, "gten" means the amount that did not pass through the #10 Sieve, 
        "lten" is the amount that passed through the #10 Sieve, "lfifty" is the amount that passed through the #50 Sieve, 
        "wph" is soil water pH, "bph" is soil buffer pH, "cce" is Culcium Carbonate Equivalent (CCE), "Zero%_eff" is the percent of lime that is not effective at all (discad) or 
        the percent of lime with particle size bigger than #10 Sieve. "Fifty%_eff" is the percent of lime that is 50 percent effective or 
        the percent of lime with particle size smaller than #10 Sieve and bigger than #50 Seive, and "Hund%_eff" is the percent of lime that is 100 
        percent effective or the percent of lime with particle size smaller than #50 Sieve, "Hun_eff_lime" is the amount of lime needed if it is 100 percent effective, "Bulk_Rec" is the adjusted lime 
        recommendation (ton/acre) that you will need to apply to your soil, and "Cost" is the cost of application per acre. Numbers at the end of the names stand for target pH. For example, Bulk_Rec64 
        is the amount of lime (ton/acre) that will raise the pH of soil to a target pH of 6.4,
        Bulk_Rec66 is the amount of lime (ton/acre) that will raise the pH of soil to a target pH of of 6.6, etc. In other words, you will need this amount of 
        lime to increase the soil pH to a target pH. The same applies to the costs too. 
        For example, "cost64" is the application cost of lime per acre that will raise the soil pH to 6.4. In the case of percentage-based data, the number of columns differs but the names remain the same. If you want all slots opened side by side, please rotate 
        the screen of your mobile device. The dark theme makes it difficult to see through, you will need to use light theme in the App setting located on top-right corner. 
        On the top-right corner of your  screen, tap the three lines. Go to Setting> Theme> and then choose "Light" from the drop-down list.  
        You can also check the "Wide mode" to let the  app occupy the entire width of  the screen. </br> 
        <span style='color: green; font-weight: bold;'>B) Sampling and Moisture Content:</span> Take 10 samples from the various parts of the lime stockpile and mix them well. 
        This will ensure that the stockpile is represented well by the sample. 
        Measure the weight, oven-dry it, and measure the weight again. 
        The difference is the amount of moisture. For example; The amount of sample is 500 g. 
        After drying in the oven, the weight of the sample was reduced to 470 g. 500 - 470 = 30 g, 
        meaning that there was 30 g (6%) water in the lime. </br>
        <span style='color: green; font-weight: bold;'>C) Particle size (Fineness) and their effectiveness:</span> Measure the empty weights of the #10 Sieve, #50 Sieve, and the pan that catches the lime passing through both 
        sieves. Add a known amount (initial amount) of lime and shake it for some time (consult Dr. Sikora or Mr. Robbie). Once the shaking 
        is over, weigh the #10 Sieve and subtract the empty weight from it, it will be the amount (g) of lime that has
        0 RNV and is 0 percent effective (discard!). Subtracting this value from the initial value will give you the amount that 
        passed through the 10# Sieve. Measuring the weight of the pan and subtracting the empty weight of pan from it will give us the weight of lime that passed through 
        50# Sieve. Lime particles that pass through the #50 Sieve are 100 percent effective.  Subtracting the amount passing 
        through #50 Sieve from the amount passing through #10 will give us the amount of lime that has passed through 
        10# Sieve but not through #50 Sieve, which is 50 percent effective. For example, the initial weight of a sample 
        before putting it into Sieves was 300 g. The weights of the empty #10 Sieve, #50 Sieve, and pan are 200 g, 210 g, and 300 g, 
        respectively. After shaking, the weight of the #10 Sieve, #50 Sieve, and Pan increased to 220 g, 300 g, and 490 g, respectively. 
        We can see that 220 - 200 = 20 g (or 20/300 * 100 = 6.6%) is the amount of lime that was retained by #10 Sieve and has zero effectiveness. 
        The amount of lime that passes through 10# and does not pass through #50 Sieve is 
        300 - 210 = 90 g (or 90/300 *100 = 30%), which is 50 percent effective. Lastly, 490 - 300 = 190 (or 190/300 *100 = 63.3%), which is the amount that passed through 
        #50 and is 100 (g) percent effective. If you want to know the amount that passes through #10 Sieve, then the initial amount minus the amount of 
        lime that did not pass through #10 Sieve is the answer. In our example, 20 g or 6.6(%) did not pass through #10 Sieve which means that 280 g 
        or (280/300 *100 = 93.3%) passed through #10 Sieve. In this form, if you are uploading an excel file, you must know the amount of lime that 
        is retained by the #10 Sieve, the amount that passes through #10 Sieve, and the amount that passes through #50 Sieve. If you are inserting values 
        manually, then you only need to inter values for the amount of lime that is retained by #10 Sieve and the amount of lime that passes through 
        #50 Sieve. The rest is calculated automatically. </br>
        <span style='color: green; font-weight: bold;'>D) Calculating RNV:</span> To know the relative neutralizing value (RNV) of the lime, you will need to know the value of
        Calcium Carbonate Equivalent (CCE) in addition to the particle size amounts. 
        You can find this either on the "website of University of Kentucky" or ask the lime seller. Our calculator will take 
        care of the rest. You can view and save graphs and download the data as a CSV file. </br>
        <span style='color: green; font-weight: bold;'>E) Adjusted Lime Recommendation:</span> Adjusted Lime Recommendation (T/Acre) is the amount of lime that you will need to apply to your soil in 
        order to raise the pH to a Target level. It depends on many factors such as, the fineness of lime, soil water pH, buffer pH, and CCE (used to calculate RNV) :blue[(our calculation 
        of the buffer pH is based on Sikora-2 buffer which takes these all into consideration)]. Insert the values in the form. You can only select the values that have been determined by Dr. Sikora laboratory. If your 
        sampled pH is not listed there; you may find the average of the two nearest values. For example, if your water pH is 
        5.4, you can measure once for 4.3, and once 5.5, the average will be the level you need to apply (consult Dr. Sikora). 
        It is important to know the target pH. A target pH of "6.4" is ideal for corn, soybean, small grains, cool-season grass hay and 
        pasture, bermudagrass, native warm-season grasses, sudangrass, millets, 
        sorghum-sudangrass hybrids, lawns, tree fruits, strawberries, blackberries, 
        raspberries, and grapes. A target pH of "6.6" is ideal for tobacco and a target pH of "6.8" is 
        ideal for alfalfa, alfalfa/cool-season grass mixtures. 
        "In some cases, the model will warn you about the pH values you entered which means that the 100 percent effective lime is not calculated" . 
        For example, if the soil water pH is 6.1 and buffer pH is 5.5, you will see a red warning which says that the model is using default values for 
        100(%) effective lime. Read the Reference for more details. </br> 
        <span style='color: green; font-weight: bold;'>F) Cost per Acre:</span> This is the cost of lime application per acre that will raise the pH of soil to a target pH.
        You will need to know the cost of lime per ton. Otherwise, the data is shown for default values. 
        </div>
            """, unsafe_allow_html=True)

# A refernce to the paper I used for buffer
        st.markdown("### **:green[Reference]**")
        container8 = st.container()
        container8.write("""Ritchey, E.L., Murdock, L.W., Ditsch, D., and McGrath, J.M. 2016. Agicultural Lime Recommendation Based on Lime Quality. Plant and Soil Science.
        F.J. Sikora, Division of Regolatory Services, College of Agriculture, Food and Environment, University of Kentucky """)

# If someone wants to tell us about it or give us suggestions
if selected1 =='Contact':
    st.markdown("<h3 style='background-color: #00FF00; text-align: center; color: 	black;'>Contact</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='background-color: white; text-align: center; color: 	black;'>""</h1>", unsafe_allow_html=True)

    container9 = st.container()
    container9.write("""
    <div style="text-align: justify;">
    <span style='color: black; font-weight: bold;'>Robbie Williams</span> </br>
    <a href = 'mailto: rwilliamsfarms@bellsouth.net'> Send Email </a> </br> 
    <span style='color: black; font-weight: bold;'>Mohammad Shamim</span> 
    </br>
    <a href = "mailto: shamim.one@outlook.com;">Send Email</a>

    </div> """, 
    unsafe_allow_html = True)