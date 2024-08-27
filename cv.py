from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "MOHIT POUDEL"
PAGE_ICON = ":heart:"
NAME = "Mohit Poudel"
DESCRIPTION = """
Self-taught Python Programmer,
Bioinformatics & Conservation Biology Enthusiast
"""
EMAIL = "poudelmohit59@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/pathsalaonline",
    "LinkedIn": "https://www.linkedin.com/in/mohit-poudel-134bba153/",
    "GitHub": "https://github.com/poudelmohit",
    "Twitter": "https://twitter.com/MohitPoudel11",
    "Medium": "https://medium.com/@poudelmohit59"
}
PROJECTS = {
    "🏆 Lotka-Volterra Model Simulator": "https://mohit254-lotka-volterra-model-streamlit-app-qsvyge.streamlit.app/",
    "🏆 Ramachandran Plot Generator": "https://mohit254-rc-plot-streamlit-app-gsua5l.streamlit.app/",
    "🏆 Phylogenetic Tree Construction ": "https://medium.com/@poudelmohit59/beginners-guide-to-phylogenetic-tree-construction-using-biopython-5accbd8345a2",
    "🏆 Genomic Sequence Analysis": "https://medium.com/@poudelmohit59/comparing-genetic-sequences-of-threatening-bat-borne-viruses-eea8c24d9bff",
    "🏆 GC Count in Python": "https://medium.com/@poudelmohit59/gc-count-in-python-855d38faf5cc",
    "🏆 Multiple Sequence Alignment": "https://medium.com/@poudelmohit59/multiple-sequence-alignment-and-jalview-9310a1abc000",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
#     st.download_button(
#         label=" 📄 Download Resume",
#         data=PDFbyte,
#         file_name=resume_file.name,
#         mime="application/octet-stream",
#     )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Commandable knowlegde on Bash Scripting, Git, R MarkDown
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, BioPython, Streamlit)
- 📊 Data Visulization: MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Bioinformatics Tools : Jalview, MuSCLE, MEGA, etc 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 0
st.write('\n')
st.write("🚧", "**Graduate Research Assistant @ Alvarado-Serrano Lab, Ohio University**")
st.write("01/08/2023 - Present")
st.write(
    """
- ► isolation of DNA sequences and amplification of specific gene regions using molecular biology techniques
- ► Working with Next-Generation-Sequencing (NGS) library preparation and becoming proficient in both dry and wetlab workflows
- ► Analyzing and interpreting NGS data using bioinformatics tools for the publication of the ongoing research projects
"""
)

# --- JOB 1
st.write('\n')
st.write("🚧", "**Research Intern @ Center for Biotechnology, Agriculture and Forestry University**")
st.write("01/2023 - 07/2023")
st.write(
    """
- ► Utilizing PCR machines to amplify specific DNA sequences, gaining proficiency in molecular biology techniques
- ► Working with bacteria culture devices and autoclaves, becoming proficient in standard microbiology techniques
- ► Analyzing and interpreting data using Excel and specialized analysis software, demonstrating strong analytical skills
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Intern @ Prime Minister Agriculture Modernization Project**")
st.write("01/2022 - 07/2022")
st.write(
    """
- ► Conducted ‘2-Days Training on Pesticide Usage’ for 200 farmers of the district
- ► Collaborated with officials for farmers’ data collection and preprocessing

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Teaching Volunteer @ Shree Nepal Rashtriya Samsher Secondary School**")
st.write("03/2019 - 03/2020")
st.write(
    """
- ► Worked as course instructor of Seccondary level Mathematics module
- ► Participated in questionnaire preparation, course evaluation and grading activities 

"""
)

# --- EDUCATIONAL BACKGROUND ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write(
    """
- ✔️ Masters in Biological Science, Ohio University, USA
- ✔️ Bachelor of Science in Agriculture, Agriculture & Forestry University, Nepal

    """
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
