from pathlib import Path

import streamlit as st
from PIL import Image


# ---- PATH Settings -----
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_EN = current_dir / "assets" / "Bartosz Banik CV EN.pdf"
resume_file_PL = current_dir / "assets" / "CV Bartosz Banik PL.pdf"
profile_pic = current_dir / "assets" / "Profile 01.png"


# --- General Settings ---
Page_title = "Bartosz Banik Resume"
Page_icon = ":wave"
Name = "Bartosz Banik"
Description = """ Senior SAP Master Data Specialist, Automation Specialist, Reportin Specialist, Data Analyst """
Email = "bartosz.banik@gmail.com"
SOCIAL_MEDIA = {
"Linkedin" : "https://www.linkedin.com/in/bartosz-banik-76aab458/",
"GitHub" : "https://github.com/BartoszBanik?tab=repositories",
}

st.set_page_config(page_title=Page_title, page_icon=Page_icon)

#--- load css, pdf and png files ---
with open(css_file) as f:
    st.markdown ("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file_EN, "rb") as pdf_file_en:
    PDFbyteEN = pdf_file_en.read()
with open(resume_file_PL, "rb") as pdf_file_pl:
    PDFbytePL = pdf_file_pl.read()
profile_pic = Image.open(profile_pic)


#--- Hero section ---
col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label = "📄 Download Resume English Version",
        data = PDFbyteEN,
        file_name = resume_file_EN.name,
        mime = "application/octet-stream",
    )
    st.download_button(
        label = "📄 Download Resume Polish Version",
        data = PDFbytePL,
        file_name = resume_file_PL.name,
        mime = "application/octet-stream",
        )
    st.write( "✉️ bartosz.banik@gmail.com")


    #--- social links----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#----- experience & qi ----
st.write ("#")
st.subheader("Experience & Qualifications")
st.write(
"""
- ✔️ 4 Years SAP experience
- ✔️ Strong hands on experience and knowledge in Excel and SQL
- ✔️ Good team-player
- ✔️ Citizen Developer with UiPath and VBA skills
"""
)

#----Skils ----
st.write("#")
st.subheader ("Hard Skills")
st.write(
"""
- 👨‍💻Programing: VBA, SQL, Python
- 📊Data Analyst and Visualization: MS Excel, Power Query, Power Pivot, Power BI
- 📇SAP modeules: MM, SD, PP
- 🤖RPA/Automation - UiPath, Selenium, Power Platform (Power Apps, Power Automate)
- 🧏Langudage skills:
    - Polish: Native
    - English: B2
"""
)

#----Skils ----
st.write("#")
st.subheader ("Work History")

#- job 1 ---

st.write ("Senior SAP MDM Specialist | Automation specialist")
st.write ("Olympus Business Services Sp. z o.o.")
st.write ("02/2019 - Present")
st.write(
"""
- ► New data creation in SAP based on predefined input
- ► Creation and maintenance of the plant/sales org. specific material master data in SAP
- ► Price data entry in SAP and price list maintenance
- ► Mass uploads in SAP (prices, settings, extension)
- ► Data cleansing in SAP
- ► Working with SQVI - internal reports for other departments
- ► Reviews SAP configuration; proposes and implements master data corrections and enhancements/optimizations.
- ► VBA and SAP scripting automations across Olympus
- ► Applications creation in C# and VB.NET for internal purpose (Visual Studio based applications)
- ► Reports automation in SAP (SAP-Excel VBA automation)
- ► Support role in RPA implementation in SCM department (UiPath solution)
- ► Testing SAP new functionalities, Tcodes, taking part in SAP release testing process
- ► Taking part in SAP implementation process for new companies - OMDS Digital Solution and Evident Europe GmbH:
    - SAP MM data migration
    - SAP training for new employees
    - processes transfer
"""
)
st.write("---")
#--- job2 --
st.write ("Billing Associate")
st.write ("EY Global Delivery Services Poland")
st.write ("01/2018 - 02/2019")
st.write(
"""
- ► Create Draft and Finalize internal and external invoices in financial billing system (GIN, Oracle PeopleSoft)
- ► Process all customers, customers engagement setup and maintenance in financial system (Oracle PeopleSoft)
- ► Responding to customer queries via e-mail
- ► Creating reports (implementing automation in VBA)
- ► Process automation (VBA, Autohotkey)
- ► Applications creation in C# and web quiz for new employees in HTML, CSS and JS
"""
)

st.write("---")
#--- job3 --
st.write ("Billing and Order Specialist")
st.write ("SI-Consulting Sp. z o.o.")
st.write ("09/2017 - 12/2018")
st.write(
"""
- ► Creating purchase orders and issuing invoices in SAP ERP system
- ► Support the logistics department in the purchasing process in the IT sector (customer contact, valuation, ordering of hardware, software and IT services)
- ► Responding to customer queries via e-mail and phone
- ► Accepting and verifying the compliance of deliveries against invoices
- ► Creating delivery notes based on customers orders
- ► Creating reports
"""
)
st.write("---")

#--- job4 --
st.write ("Software Tester - Intership")
st.write ("TestArmy Group S.A.")
st.write ("09/2017 - 12/2018")
st.write(
"""
- ► Write and execute test cases (Testlink)
- ► Reporting bugs (Mantis)
- ► Reporting test results
- ► Taking part in crowdtesting projects
"""
)
st.write("---")

#--- job5 --
st.write ("Shipping, Order and Customer service specialist")
st.write ("Digital Revolution Poland sp. z o.o.")
st.write ("01/2013 - 08/2017")
st.write(
"""
- ► Process and manage all customer orders
- ► Issuing invoices based on customer orders
- ► Issuing corrective invoice
- ► Enter orders to company system
- ► Verifying the quantity of items received against invoices
- ► Order preparation – creating delivery note, invoices, packing, updating data about customers, cooperation with warehouse, post office and courier company
- ► Explanation of delivery delay
- ► Monitoring and adjusting product availability data in company system
- ► New customer master data creation in EKN and Probit
- ► Taking part in implementing process of a new warehouse and accounting management software in Digital Revolution Poland
"""
)
st.write("#")
st.subheader ("Education")
# - 1 school --
st.write("WSB University in Wroclaw")
st.write("Postgraduate studies – Integrated IT system SAP ERP")
st.write("10/2017 - 07/2018")
st.write("---")
# - 2 school --
st.write("The International University of Logistics and Transport in Wroclaw")
st.write("Logistics - master's degree")
st.write("10/2011 - 09/2013")
st.write("---")
# - 2 school --
st.write("University of Wroclaw")
st.write("European Studies – master's degree")
st.write("10/2006 - 07/2011")
