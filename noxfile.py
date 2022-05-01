import nox

@nox.session(python=["3.8", "3.9"])
def tests(session):
    session.install('pytest')
    session.run('pytest')


@nox.session
def package_install(session):
    # same as pip install .
    session.install(".")
