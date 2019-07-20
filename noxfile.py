import nox


@nox.session(python=["3.6", "3.7"])
@nox.parametrize("dateutil", ["2.6.1", "2.7.5", "2.8.0"])
def test(session, dateutil):
    session.install(
        f"python-dateutil=={dateutil}",
        "pytest", 
    )

    session.run("pytest", "--quiet", "--tb=line")
