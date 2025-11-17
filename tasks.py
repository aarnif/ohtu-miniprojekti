from invoke import task

@task
def build(ctx):
    ctx.run("python3 src/db_helper.py", pty=True)


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test_unit(ctx):
    ctx.run("pytest src/tests", pty=True)

@task
def test_e2e(ctx):
    ctx.run("robot --variable HEADLESS:true src/story_tests", pty=True)