from distutils.core import setup

setup(
    name='dagger',
    version='1.3.0',
    author='Remik Ziemlinski',
    author_email='first.surname@gmail',
    packages=['dagger',],
    url='http://pythondagger.sourceforge.net/',
    license='GPL',
    description='File dependency graph evaluator.',
    classifiers="""
Development Status :: 5 - Production/Stable,
Intended Audience :: Developers,
License :: OSI Approved :: GNU General Public License (GPL),
Natural Language :: English,
Operating System :: OS Independent,
Programming Language :: Python,
Topic :: Software Development :: Build Tools
""".replace('\n','').split(',')
)
