import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

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
.Widget>label {
    color: black;
    font-weight: bold;
    font-size = 30px;
    font-family: monospace;
}

.Widget .Widget {
    color: black;
    font-weight: bold;
    font-size = 30px;
    font-family: monospace;
}

[class^="st-b"]  {
    color: black;
    font-family: monospace;
}
.st-bb {
    background-color: light blue;
}
.st-at {
    background-color: #0c8080;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}
header .decoration {
    background-image: none;
}

</style>
""",
    unsafe_allow_html=True,
)



st.markdown("<h1 style='text-align: center; color: blue;'>Lime Particle Analysis</h1>", unsafe_allow_html=True)


# add some information
container1 = st.container()
container1.write("""**:red[All rights reserved]**.
    This web application was developed by **Mohammad Shamim (Ph.D.)** and **Robbie Williams**, a farmer in Henderson County, Kentucky, USA. 
    Please read the **:green[instructions]** carefully before proceeding with your calculations. You can eitheer use 
    the form and insert values manually in the cells below or upload an excel file. 
    The manual form has a capacity of calculating five lime sources whereas uploading an excel file allows you to 
    calculate as many lime soures as you want. Graphs and data are not shown by default, so you will need to check boxes or toggle buttons 
    for your desired calculation. This app works for both Sikora-2 buffer (which is default buffer here) and SMP 
    buffer. To perform SMP analysis, you will need to enter CCE value (in the case of excel file, please use defaul values in other columsn) 
     and just the target pH and buffer pH from the drop-down lsits""")


st.markdown("<h2 style='text-align: center; color: blue;'>Lime Sources</h2>", unsafe_allow_html=True)


# This data is important for finding the 100 % effective amount of lime with relevant PH
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
        index = index= [4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 5.7, 5.9, 6.1]
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


pdf = data_generate(ph=6.4)
pdf66 = data_generate(ph=6.6)
pdf68 = data_generate(ph=6.8)


# Lets make some empty dictionary to  save data

quarries = {}
initial ={}
gten  = {}
# lten = {}
lfifty = {}
wph = {}
bph = {}
CCE = {}
Price ={}
   

# st.subheader("Is your result based on percentage or weight?")

date1, _,_,_,_ = st.columns(5)
date = date1.date_input("**Date**")
time = time = datetime.datetime.now().time()


percent_weight = st.radio("**Is your result based on percentage or weight?**", options =("Lab Results (Weight)", "Lab Results (Percentage)"))
st.markdown(" ### Fill in the form manually")
# Lets crete a date and use it as a file name so each time the file is save is unque with a time stamp.

# Lets loop through the columns
# Dynamic columns
ncol = st.sidebar.number_input("**Number of Lime sources?**", 1, 5, 1)
cols = st.columns(ncol)
# Here, I am setting a condition if the data is in percentage or weight

if percent_weight =="Lab Results (Weight)":
    for i, x in enumerate(cols):
        quarries[i]= x.text_input('**Lime Source:**', key = f"q_{i}_name")
        initial[i] = x.number_input('**Initial Amount (g)**: ', value = 100.00, key = f"q_{i}_initial", format="%.2f")
        gten[i] = x.number_input('**Amount > #10 (g)**: ', value = 10.00, key = f"q_{i}_10", format="%.2f")
        lfifty[i] = x.number_input('**Amount < #50 (g):**', value = 60.00, key = f"q_{i}_50", format="%.2f")
        wph[i] = x.selectbox('**Soil Water pH:**', options = pdf.index, key = f"q_{i}_wph")
        bph[i] = x.selectbox('**Buffer pH (Sikora-2):**', options = [5.5, 5.7, 5.9, 6.1, 6.3, 6.5, 6.7, 6.9, "NA"], key = f"q_{i}_bph")
        CCE[i] = x.number_input("**Culcium Carbonate Equivalent (CCE):** ", value = 90.0, key = f'cce{i}', format="%.1f")
        Price[i] = x.number_input("**Price ($/ton)**", value = 10.0, key = f'price{i}', format="%.1f")

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

    # Lets give an option to upload an excel file
    st.markdown(" ### Upload an Excel file")
    uploadcond = st.checkbox("**Check to read instructions and proceed!**")
    uploadfile = None
    if uploadcond:
        st.write("**:blue[Your file should look like this]**")
        st.dataframe(pd.DataFrame({"Lime Source":"Sample1", "Initial (g)": 100, "> #10 (g)": 10, "< #10": 90,"< #50 (g)":60,
        "wph": 4.5, "bph":5.4, "cce": 90, 'price': 20}, index =[1]))
        subcontainer1= st.container()
        subcontainer1.write("""
        **:blue[Tips: ]** Your file must be an excel file with a tabular format. The first row must be the header row. 
        The file must have **"9 columns"** in order of "Lime Source", "Initial amount (g) of lime sample", "The amount (g) of lime retained 
        in #10 Sieve", "The amount (g) of lime passed through #10 Sieve", "The amount (g) of lime passed through #50 Sieve", 
        "Water pH", "Buffer pH", "CCE", and "Price per ton". The left most column with empty header and a value of **"1"** is automatically generated 
        so it sould not be in your file. You can give any name to the headers. If the water pH and buffer pH are unknown, 
        use default values of 4.5 and 5.5 for all your samples, respectively. The default value of CCE is 90 and the default value of price is 20.
        In the case of default values, the calculations and graphs, as you know, are incorrect.
        Default values are used to run the model smoothly. They have no scientific meaning. 
        """)
        uploadfile = st.file_uploader("")
    else:
        pass

    if uploadfile is not None:
        st.success("**File uploaded successfully!**")
        df = pd.read_excel(uploadfile)
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
    # For some PH values,there is no 100 percent effective lime. Model will throug an error so we need to correct it
    if "" in [i for i in df.Hun_eff_lime64]:
        phvs = df.loc[df.Hun_eff_lime64=="", ["wph", "bph"]]
        st.write(f"**:red[For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.4 is not calculated. A default value of 3.33 is used. Consider using lime recommendation based on SMP values below.]**")
        df['Hun_eff_lime64'] = [3.33 for i in range(df.shape[0])]

    df['Hun_eff_lime66'] = [pdf66.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

    if "" in [i for i in df.Hun_eff_lime66]:
        phvs = df.loc[df.Hun_eff_lime66=="", ["wph", "bph"]]
        st.write(f"**:red[For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.6 is not calculated. A default value of 3.33 is used. Consider using lime recommendation based on SMP values below.]**")
        df['Hun_eff_lime66'] = [3.33 for i in range(df.shape[0])]

    df['Hun_eff_lime68'] = [pdf68.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

    if "" in [i for i in df.Hun_eff_lime68]:
        phvs = df.loc[df.Hun_eff_lime66=="", ["wph", "bph"]]
        st.write(f"**:red[For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.6 is not calculated. A default value of 3.33 is used. Consider using lime recommendation based on SMP values below.]**")
        df['Hun_eff_lime68'] = [3.33 for i in range(df.shape[0])]


    df['Bulk_Rec64'] = (df.Hun_eff_lime64/df.RNV)*100
    df['Bulk_Rec66'] = (df.Hun_eff_lime66/df.RNV)*100
    df['Bulk_Rec68'] = (df.Hun_eff_lime68/df.RNV)*100
    df['Cost64'] = df.price*df['Bulk_Rec64']
    df['Cost66'] = df.price*df['Bulk_Rec66']
    df['Cost68'] = df.price*df['Bulk_Rec68']

elif percent_weight == "Lab Results (Percentage)":
    for i, x in enumerate(cols):
        quarries[i]= x.text_input('**Lime Source:**', key = f"q_{i}_name")
        gten[i] = x.number_input('**% > #10:**', value = 10.00, key = f"q_{i}_10", format="%.2f")
        lfifty[i] = x.number_input('**% < #50 (g):**', value = 60.00, key = f"q_{i}_50", format="%.2f")
        wph[i] = x.selectbox('**Soil Water pH:**', options = pdf.index, key = f"q_{i}_wph")
        bph[i] = x.selectbox('**Buffer pH (Sikora-2):**', options = [5.5, 5.7, 5.9, 6.1, 6.3, 6.5, 6.7, 6.9, "NA"], key = f"q_{i}_bph")
        CCE[i] = x.number_input("**Culcium Carbonate Equivalent (CCE):**", value = 90.0, key = f'cce{i}', format="%.1f")
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
    st.markdown(" ### Upload an Excel file")
    uploadcond = st.checkbox("**Check to read the instruction and proceed!**")
    uploadfile = None
    if uploadcond:
        st.write("**:blue[Your file should look like this]**")
        st.dataframe(pd.DataFrame({"Lime Source":"Sample1","> #10 (%)": 10, "< #10 (%)":90,
        "< #50 (%)": 60, "wph": 4.5, "bph":5.4, "cce": 90, 'price': 20}, index =[1]))
        subcontainer1= st.container()
        subcontainer1.write("""
        **:blue[Tips: ]** Your file must be an excel file with a tabular format. The first row must be the header row. 
        The file must have **"8 columns"** in order of "Source names", " Percent of lime retained 
        in #10 Sieve", "Percent of lime passed through #10 Sieve", "Percent of lime passed through #50 Sieve", 
        "Water pH", "Buffer pH", "CCE", and "Price per ton". The left most column with empty header and a value of **"1"** is automatically generated 
        so it sould not be in your file. You can give any name to headers.  If the water pH and buffer pH are unknown, 
        use default values of 4.5 and 5.5 for all your samples, respectively. The default value of CCE is 90 and the default value of price is 20. 
        The remaining columns are automatically calculated. In the case of default values, the calculations and graphs, as you know, are incorrect.
        Default values are used to run the model smoothly. They have no scientific meaning. 
        """)
        uploadfile = st.file_uploader("")
    else:
        pass

    if uploadfile is not None:
        st.success("**File uploaded successfully!**")
        df = pd.read_excel(uploadfile)
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
        st.write(f"**:red[For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.4 is not calculated. A default value of 3.33 is used. Consider using lime recommendation based on SMP values below.]**")
        df['Hun_eff_lime64'] = [3.33 for i in range(df.shape[0])]

    df['Hun_eff_lime66'] = [pdf66.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

    if "" in [i for i in df.Hun_eff_lime66]:
        phvs = df.loc[df.Hun_eff_lime66=="", ["wph", "bph"]]
        st.write(f"**:red[For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.6 is not calculated. A default value of 3.33 is used. Consider using lime recommendation based on SMP values below.]**")
        df['Hun_eff_lime66'] = [3.33 for i in range(df.shape[0])]

    df['Hun_eff_lime68'] = [pdf68.loc[i, str(j)] for i, j in zip (df.wph, df.bph)]

    if "" in [i for i in df.Hun_eff_lime68]:
        phvs = df.loc[df.Hun_eff_lime68=="", ["wph", "bph"]]
        st.write(f"**:red[For the given soil water pH of {phvs.iloc[0, 0]} and buffer pH {phvs.iloc[0, 1]}, a 100 effective lime amount for a target pH of 6.8 is not calculated. A default value of 3.33 is used. Consider using lime recommendation based on SMP values below.]**")
        df['Hun_eff_lime68'] = [3.33 for i in range(df.shape[0])]


    df['Bulk_Rec64'] = (df.Hun_eff_lime64/df.RNV)*100
    df['Bulk_Rec66'] = (df.Hun_eff_lime66/df.RNV)*100
    df['Bulk_Rec68'] = (df.Hun_eff_lime68/df.RNV)*100
    df['Cost64'] = df.price*df['Bulk_Rec64']
    df['Cost66'] = df.price*df['Bulk_Rec66']
    df['Cost68'] = df.price*df['Bulk_Rec68']


st.markdown("<h3 style='text-align: center; color: blue;'>Lime Particle and RNV Analysis</h3>", unsafe_allow_html=True)
# Make charts

colcol,_,_,_ = st.columns(4)
pallete = colcol.selectbox("**Choose color palette for graphs**", ["Dark2","Accent", "Accent_r", "autumn", "Blues", "Blues_r", "bright", "BuGn", 
"BuGn_r", "BuPu", "BuPu_r", "binary", "binary_r", "bone", "bone_r", "bwr", "colorblind",  "cool", "coolwarm", "copper", "cubehelix", "dark",
"Dark2_r", "deep","GnBu", "GnBu_r", "gnuplot" ,"gnuplot2","Greens", "Greens_r", "Greys", "Greys_r" ,"gray", "hot", "hot_r" ,"jet_r","nipy_spectral", "muted",
"OrRd", "OrRd_r","ocean", "ocean_r" ,"Oranges", "Oranges_r", "PRGn", "PRGn_r", "pink", "pink_r" ,"Paired", "Paired_r","pastel", "Pastel1", "Pastel1_r",
"Pastel2", "Pastel2_r", "PiYG", "PiYG_r",  "PuBu", "PuBuGn", "PuBuGn_r", "PuBu_r", "PuOr", "PuOr_r", "PuRd", "PuRd_r",
"Purples", "Purples_r","rainbow","rainbow_r" ,"RdBu", "RdBu_r", "RdGy", "RdGy_r", "RdPu", "RdPu_r", "RdYlBu", "RdYlGn", "Reds", "Reds_r", "Set1", "Set1_r",
"Set2", "Set2_r", "Set3", "Set3_r", "Spectral", "Spectral_r" , "seismic", "seismic_r" ,"spring","spring_r", "summer","summer_r", "YlGn", "YlGnBu", "YlOrBr", "YlOrRd",
"prism", "terrain", "terrain_r","winter", "winter_r"])


@st.cache
def graph_h():
    if df.shape[0]>4:
        eff_h = 5+(df.shape[0]-5)*0.45
        others = 2+(df.shape[0]-2)*0.15
        rotation = 0
        return eff_h, others, rotation
    else:
        return 5,  2, -90
eff_h, others, rotation = graph_h()


if st.checkbox("Show graphs"):

    # st.markdown("<h1 style='text-align: center; color: black;'>Lime Particle Analysis</h1>", unsafe_allow_html=True)
    fig,(ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (7, eff_h), sharex=True, gridspec_kw={'hspace':0})
    Fplot = sns.barplot(x = "Zero%_eff", y = 'Quarry', data=df, ax=ax1, palette=pallete)
    ax1.set_ylabel(None)
    ax1.text(0.65, 0, s="#10 Seive", transform = ax1.transAxes)
    ax1.text(0.95, 0.18, "RNV (0%)", rotation =270, transform= ax1.transAxes)
    ax1.text(0.90, 0.22, "Discard", rotation =270, transform= ax1.transAxes)
    ax1.bar_label(Fplot.containers[0], fmt="%.2f", rotation =0)
    ax1.set_title("Lime Fineness (%)", fontsize = 18)


    Splot =sns.barplot(x = "Fifty%_eff", y = 'Quarry', data=df, ax=ax2, palette=pallete)
    ax2.set_ylabel(None)
    ax2.text(0.65, 0, s="#50 Seive", transform = ax2.transAxes)
    ax2.text(0.95, 0.18, "RNV (50%)", rotation =270, transform= ax2.transAxes)
    ax2.bar_label(Splot.containers[0], fmt="%.2f", rotation = 0)


    Tplot = sns.barplot(x = "Hund%_eff", y = 'Quarry', data=df, ax=ax3, palette=pallete)
    ax3.set_xlim((0, 100))
    ax3.set_ylabel(None)
    ax3.text(0.95, 0.18, "RNV (100%)", rotation =270, transform= ax3.transAxes)
    ax3.bar_label(Tplot.containers[0],fmt="%.2f", rotation = 0)
    ax3.set_xlabel("", fontsize = 14)
    ax3.axes.xaxis.set_visible(False)
    ax3.set_xticklabels([])

    # plot for RNV_______________

    fig1, ax4= plt.subplots(figsize = (7,others))
    ax4.set_xlabel('RNV (%)')
    ax4.set_ylabel(None)
    ax4.set_title("Relative Neutralizaing Value (RNV (%))", fontsize = 18)

    FrPlot = sns.barplot(x='RNV', y = 'Quarry', data=df, ax=ax4, palette=pallete)
    ax4.set_xlim((0, 100))
    ax4.bar_label(FrPlot.containers[0], fmt="%.2f", rotation=rotation)
    ax4.set_ylabel(None)
    ax4.set_xlabel("", fontsize = 14)
    ax4.axes.xaxis.set_visible(False)
    ax4.set_xticklabels([])
    st.pyplot(fig)
    st.pyplot(fig1)
else:
    pass


# Plot for Bulk Recommendation of  Lime
st.markdown("<h3 style='text-align: center; color: blue;'>Lime Recommendation and Its Cost Based on Sikora-2 Buffer</h3>", unsafe_allow_html=True)
reccost = st.radio("**Show adjusted lime recommendation and its cost**", ("No", "Yes"))
if reccost =="Yes":
    phcol, _,_,_,_ = st.columns(5)
    target = phcol.selectbox("**What is the target pH:**", [6.4, 6.6, 6.8], key = 'target')

    if target==6.4:
        fig2, ax5 = plt.subplots(figsize =(7,others) )
        ax5.set_ylabel(None)
        ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH of {target}", fontsize = 14)

        FiPlot = sns.barplot(x='Bulk_Rec64', y = 'Quarry', data=df, ax=ax5, palette=pallete)
        ax5.bar_label(FiPlot.containers[0], fmt="%.1f", rotation = rotation)
        ax5.set_ylabel(None)
        ax5.set_xlabel("", fontsize = 14)
        ax5.axes.xaxis.set_visible(False)
        ax5.set_xticklabels([])
        
        # Plot for Cost of  Lime

        fig3, ax6 = plt.subplots(figsize =(7,others) )
        ax6.set_ylabel(None)
        ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH of {target}", fontsize = 14)

        SiPlot = sns.barplot(x='Cost64', y = 'Quarry', data=df, ax=ax6, palette=pallete)
        ax6.bar_label(SiPlot.containers[0], fmt="%.1f", label_type='edge', rotation = rotation)
        ax6.set_ylabel(None)
        ax6.set_xlabel(None)
        ax6.axes.xaxis.set_visible(False)
        ax6.set_xticklabels([])
        st.pyplot(fig2)
        st.pyplot(fig3)

    elif target ==6.6:
        fig2, ax5 = plt.subplots(figsize =(7,others) )
        ax5.set_ylabel(None)
        ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH of {target}", fontsize = 14)

        FiPlot = sns.barplot(x='Bulk_Rec66', y = 'Quarry', data=df, ax=ax5, palette=pallete)
        ax5.bar_label(FiPlot.containers[0], fmt="%.2f", rotation =rotation)
        ax5.set_ylabel(None)
        ax5.set_xlabel("", fontsize = 14)
        ax5.axes.xaxis.set_visible(False)
        ax5.set_xticklabels([])

        # Plot for Cost of  Lime

        fig3, ax6 = plt.subplots(figsize =(7,others) )
        ax6.set_ylabel(None)
        ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH of {target}", fontsize = 14)

        SiPlot = sns.barplot(x='Cost66', y = 'Quarry', data=df, ax=ax6, palette=pallete)
        ax6.bar_label(SiPlot.containers[0], fmt="%.1f", label_type='edge', rotation = rotation)
        ax6.set_ylabel(None)
        ax6.set_xlabel(None)
        ax6.axes.xaxis.set_visible(False)
        ax6.set_xticklabels([])
        st.pyplot(fig2)
        st.pyplot(fig3)

    elif target ==6.8:
        fig2, ax5 = plt.subplots(figsize =(7,others) )
        ax5.set_ylabel(None)
        ax5.set_title("Bulk Recommendation of Lime (T/Acre)", fontsize = 18)

        FiPlot = sns.barplot(x='Bulk_Rec68', y = 'Quarry', data=df, ax=ax5, palette=pallete)
        ax5.bar_label(FiPlot.containers[0], fmt="%.2f",  rotation = rotation)
        ax5.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH of {target}", fontsize = 14)
        ax5.set_ylabel(None)

        # Plot for Cost of  Lime

        fig3, ax6 = plt.subplots(figsize =(7,others) )
        ax6.set_ylabel(None)
        ax6.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH of {target}", fontsize = 14)

        SiPlot = sns.barplot(x='Cost68', y = 'Quarry', data=df, ax=ax6, palette=pallete)
        ax6.bar_label(SiPlot.containers[0], fmt="%.1f", label_type='edge', rotation = rotation)
        ax6.set_ylabel(None)
        ax6.set_xlabel(None)
        ax6.axes.xaxis.set_visible(False)
        ax6.set_xticklabels([])

        st.pyplot(fig2)
        st.pyplot(fig3)



    
st.markdown("<h3 style='text-align: center; color: blue;'>Lime Recommendation based on SMP Method</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>You will need to djust the Target pH and Buffer pH </h5>", unsafe_allow_html=True)

# This data is used to to calculate the recommended amount of lime based on target pH and soil buffer.
data3 = {
    "6.0": [1.0, 1.4, 1.8, 2.3, 2.7, 3.1, 3.5, 3.9, 4.4, 4.8, 5.2, 5.6, 6.0, 6.5, 6.9],
    "6.4": [1.2, 1.7, 2.2, 2.7, 3.2, 3.7, 4.2, 4.7, 5.2, 5.7, 6.2, 6.7, 7.2, 7.7, 8.2],
    "6.8": [1.4, 1.9, 2.5, 3.1, 3.7, 4.2, 4.8, 5.4, 6.0, 6.5, 7.1, 7.7, 8.3, 8.9, 9.4]
}

index3 =   [6.7, 6.6, 6.5, 6.4, 6.3, 6.2, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6, 5.5, 5.4, 5.3]

df_smpbubber = pd.DataFrame(data=data3, index=index3)

check1 = st.checkbox("Check to Proceed", key='check1')

if check1:
    col1, col2 = st.columns( 2)
    TarPH = col1.selectbox('**:red[Targe PH]**', options = ["6.0", "6.4", "6.8"])
    Soil_bf = col2.selectbox("**:red[Soil Buffer (SMP)]**", options = index3)
    df['Bulk_smp_buffer'] = (df_smpbubber.loc[Soil_bf, TarPH]/df.cce) * 100
    df['Cost_smp_buffer'] = df.Bulk_smp_buffer * df.price

    fig4, ax7 = plt.subplots(figsize =(7,others) )
    ax7.set_ylabel(None)
    ax7.set_title(f"Adjusted Lime Recommendation ($Tons\ Acre^{-1}$)\n for a Target pH {TarPH}", fontsize = 14)

    SePlot = sns.barplot(x='Bulk_smp_buffer', y = 'Quarry', data=df, ax=ax7, palette=pallete)
    ax7.bar_label(SePlot.containers[0], fmt="%.2f", rotation = rotation)
    ax7.set_ylabel(None)
    ax7.set_xlabel("", fontsize = 14)
    ax7.axes.xaxis.set_visible(False)
    ax7.set_xticklabels([])

    # Plot for Cost of  Lime

    fig5, ax8 = plt.subplots(figsize =(7,others) )
    ax8.set_ylabel(None)
    ax8.set_title(f"Total Cost of Lime Application ($\$\ Acre^{-1}$)\n for a target pH {TarPH}", fontsize = 14)

    EiPlot = sns.barplot(x='Cost_smp_buffer', y = 'Quarry', data=df, ax=ax8 , palette=pallete)
    ax8.bar_label(EiPlot.containers[0], fmt="%.1f", label_type='edge', rotation = rotation)
    ax8.set_xlabel("", fontsize = 14)
    ax8.axes.xaxis.set_visible(False)
    ax8.set_ylabel(None)
    ax8.set_xticklabels([])

    st.pyplot(fig4)
    st.pyplot(fig5)

st.markdown("<h4 style='text-align: center; color: blue;'> Output File</h4>", unsafe_allow_html=True)
show_data = st.checkbox("Show data")
if show_data:
    st.dataframe((df.set_index('Quarry').style.format("{:.2f}")))
    st.caption("**:blue[This dataframe is interactive, You can scroll left-to-right or top-to-bottom]**")
else:
    pass

# Preparing data to download

df = df.to_csv().encode('utf-8')

# this checkbox will allow us to download data
st.header(":green[Download!]")
st.download_button(
    key = 'b_csv',
    label = "Download data as csv file",
    data = df,
    file_name = f"Lime_particle_analysis_[{date}]_[{time}].csv",
    mime = 'text/csv'
)
st.caption("A default dataset is downloaded if you don't insert values in the form or don't upload  a file")

st.title("**:green[Instructions]** ")


inst = st.checkbox('Check the box to read', key = 'inst')
if inst:
    container2 = st.container()
    container2.write("""
    **A) Using the App:** You can open up to 5 slots for your Agriculture lime analysis. For example, if you are interested in analyzing 
    3 lime sourcess, you will select 3 from  the left-hand side selector which is titled as **"Number of Lime Sources"** on the top left corner. 
    After that, the form will show 3 columns for you. You can insert values there and check :green["Show graphs"]. 
    It will draw charts and create a CSV file for you. To save a chart to your computer, right-click on the chart 
    and then choose **:blue["save image as"]** or **:blue["copy image"]** and then paste it as a picture in other places. To save data, 
    You will need to go to the **:green[Download]** section and check the box. an option will pop up. Pressing that button will 
    save the data to your machine. In the data, you will see many columns. **:blue[Initial]** is the initial weight of the sample, **:blue[gten]** means the amount that did not pass through the #10 Sieve, 
    **:blue[lten]** is the amount that passed through the #10 Sieve, **:blue[lfifty] is the amount that passed through the #50 Sieve, 
    **:blue[wph]** is water pH, **:blue[bph]** is buffer pH, **:blue[cce]** is CCE, **:blue[Zero%_eff]** is the percent of lime that is not effective at all (discad) 
    **:blue[Fifty%_eff]** is the percent of lime that is 50 percent effective, and **:blue[Hund%_eff]** is the percent of lime that is 100 
    percent effective, **:blue[Hun_eff_lime]** is the amount of lime needed if it is 100 percent effective, **:blue[Bulk_Rec]** is the adjusted lime 
    recommendation (ton/acre) and **:blue[Cost]** is the cost of application per acre. Numbers at the end of the names stand for target pH. For example Bulk_Rec64 
    is the amount (ton/acre) that will raise the pH of soil to a target pH of 6.4,
    Bulk_Rec66 is the amount (ton/acre) that will raise the pH of soil to a target pH of of 6.6, etc. In other words, you will need this amount of 
    lime that you jsut analyzed to increase the soil pH to a target pH. The same applies to the costs too. 
    For example **cost64** is the application cost of lime per acre that will raise the soil pH to 6.4. **:blue[Bulk_smp_buffer]** is the amount of lime needed to raise to a target Ph using SMP buffer , 
    **:blue[Cost_smp_buffer]** is the cost of application per Acre. In the case of percentage based data, the number of columns differs but the names remains the same.

    """)

    container3 = st.container()
    container3.write("""
    **B) Sampling and moisture contnet:** Take 10 samples from the various parts of the lime stockpile and mix them. 
    This will ensure that the stockpile is represented well by the sample. 
    Measure the weight, oven-dry it, and measure the weight again. 
    The difference is the amount of moisture. For example; The amount of sample is 500 g. 
    After drying in the oven, the weight of the sample was reduced to 470 g. 500 - 470 = 30 g, 
    meaning that there was 30 g (6%) water in the lime. 

    """)

    container4 = st.container()
    container4.write("""
    **C) Partilce size and their effectiveness:** Measure the empty weights of the #10 Sieve, #50 Sieve, and the pan that catches the lime passing through both 
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
    #50 and is 100 (g) percent effective.If you want to know the amount that passes through #10 Sieve, then the initial amount minus the amount of 
    lime that did not pass through #10 Sieve is the anwer. In our example, 20 g or 6.6(%) did not pass thorugh #10 Sieve which means that 280 g 
    or (280/300 *100 = 93.3%) passed through #10 Sieve. In this form, if you are aploading a excel file, you must know the amount of lime that 
    is retained by the #10 Sieve, the amount that passes through #10 Sieve, and the amount that passes through #50 Sieve. If you are inserting values 
    manually, then you only need to inter values for the amount of lime that is retained by #10 Sieve and the amount of lime that passes through 
    #50 Sieve. The rest is calculated automatically. 
    """)

    container5 = st.container()
    container5.write("""
    **D) Calculating RNV:** To know the relative neutralizing value (RNV) of the lime, you will need to know the value of
    Calcium Carbonate in addition to the particle size amounts. 
    You can find this either in the **:blue[website of University of Kentucky]** or ask the lime seller. Our calculator will take 
    care of the rest. You can view and save graphs and download the data as a CSV file.
    """)

    container6 = st.container()
    container6.write("""
    **E) Adjusted lime recommendation:** Adjusted Lime Recommendation (T/Acre) is the amount of lime that you will  need to apply to your soil in 
    order to raise the pH to a Target level. If depends on many factors such as soil water pH, buffer pH, and CCE (used to calculate RNV) :blue[(Our calcualtion 
    of the buffer pH is based on Sikora-2 buffer)]. Insert the values in the form. You can only select the values that have been determined by Dr. Sikora laboratory. If your 
    pH is not listed there; you may find the average of the two nearest values. For example, if your water pH is 
    5.4, you can measure once for 4.3, and once 5.5, the average will be the level you need to apply (consult Dr. Sikora). 
    It is important to know the target pH. A target pH of **:red[6.4]** is ideal for corn, soybean, small grains, cool-season grass hay and 
    pasture, bermudagrass, native warm-season grasses, sudangrass, millets, 
    sorghum-sudangrass hybrids, lawns, tree fruits, strawberries, blackberries, 
    raspberries, and grapes. A target pH of **:red[6.6]** is ideal for tobacco and a target pH of **:red[6.8]** is 
    ideal for alfalfa, alfalfa/cool-season grass mixtures. 
    **:red[In some cases, the model will warn you about the pH values you entered which means that the 100 percent effective lime is not calculated]** . 
    For example, if the soil water pH is 6.1 and buffer pH is 5.5, you will see a red warning which says that the model is using defaul  values for 
    100(%) effective lime. Read the References for more details. 
    """)

    container7 = st.container()
    container7.write("""
    **F) Cost per acre:** This is the cost of lime application per acre that will raise the pH of soil to a target pH.
    You will need to knwo the cost of lime per ton. Otherwise, the data
    is shown for default values. 
    """)



st.subheader('Reference')
container8 = st.container()
container8.write("""Ritchey, E.L., Murdock, L.W., Ditsch, D., and McGrath, J.M. 2016. Agicultural Lime Recommendation Based on Lime Quality. Plant and Soil Science.
F.J. Sikora, Division of Regolatory Services, College of Agriculture, Food and Environment, University of Kentucky """)

st.subheader('Contact us!')
container9 = st.container()
container9.write("""
**:black[Robbie Williams:]** rwilliamsfarms@bellsouth.net
**:black[Mohammad Shamim:]** shamim.one@outlook.com
""")