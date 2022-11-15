import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Jaquet Watkins, B.S.
##### *Python and Java Developer* 
''')

image = Image.open('1516756574808.jpeg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Problem-solver with almost 4 years of experience in developing web and mobile applications with a passion for learning. 
- Strong verbal and written communication skills as demonstrated by rising to leadership postions in the US Army and civilian organizations that I have been apart of.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/quetga" target="_blank">Jaquet Watkins</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Science** (Information Technology), *Strayer University*, Atlanta',
    '2020-2022')
st.markdown('''
- GPA: `3.5`
- Graduated with Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Senior LAN Manager**, US Army',
    '2009-2014')
st.markdown('''
• Supervise, install, operate and perform unit level maintenance on multifunctional information processing systems, peripheral equipment, associated devices in mobile and fixed facilities.

• Perform analyst and information assurance functions and conduct data system studies and prepare documentation and specifications for proposals.

• Perform Information Service Support Office duties of printing, publications, records management and Communication Security custodian functions and certification authority duties in support of the Defense Management System.

• Configure information processing equipment into required operating configurations. Perform senior operator and system administrator duties, unit level maintenance functions on assigned computer systems and information assurance duties.

• Requisition, receive, store, issue, account for Communication Security equipment, associated keying materials and supervise the maintenance of files and records. Generate reports for the Information Services Support Office, set up and maintain logs, rosters, status boards, charts, graphs and viewgraphs.

• Compile production report data and quality control information. Assist less experienced associates in the installation, operation, and maintenance of information processing equipment. Draft program operation manuals and technical program requirements documents. Troubleshoot software using established debugging procedures and served as a supervisor for the Defense Message System. Active directory and Microsoft supervisor.


''')

txt('**Various Manufacturing Positions**, Matheson, Pella, Saputo',
    '2014-2020')

txt('**Self-employed Developer/PC Repair **,',
    '2019-Present')

st.markdown('''
- Creating scalable web and mobile applications for personal projects, friends, and family. PC refreshing and PC repair for customers daily. Firewall, networking, and software troubleshooting computers and desktops for 2 years. 2 years of ServiceNow ticketing system and Micro POS system repair and installation experience. I build desktop PC's from scratch, and restore computers to their original state.
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Java`, `Linux`, `SQL`, `C++`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `plotly`')
txt3('Web development', '`JavaScript`, `HTML`, `CSS`')
txt3('Frameworks', '`BootStrap`, `Node.js`, `React`, `Spring`, `Django`, `Flask`')
txt3('Model deployment',
     '`streamlit`, `Heroku`, `AWS`, `Docker`')
txt3('CI/CD', '`Jenkins`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/jaquet-watkins-70a3747a/')
txt2('GitHub', 'https://github.com/quetga')
