from invoke import task

@task
def dev(c):
    c.run('export $(cat env.dev | xargs) && python manage.py runserver --settings config.settings_dev 0.0.0.0:8000')

@task
def dev_migrate(c):
    c.run('export $(cat env.dev | xargs) && python manage.py migrate --settings config.settings_dev')


@task
def test(c):
    c.run('export $(cat env.dev | xargs) && python manage.py test --settings config.settings_dev plaid_utils')

@task
def bash(c):
    c.run('bash', pty=True)

@task
def prod_migrate(c):
    c.run('export $(cat env.prod | xargs) && python manage.py migrate --settings config.settings_prod')

@task
def collect_static(c):
    c.run('export $(cat env.prod | xargs) && python manage.py collectstatic --settings config.settings_prod --no-input')

@task
def serve(c):
    c.run('export $(cat env.prod | xargs) && gunicorn wsgi:application --bind 0.0.0.0:80')
