from decouple import config
from isserviceup.services.aws import AWS
from isserviceup.services.azure import Azure
from isserviceup.services.circleci import CircleCI
from isserviceup.services.compose import Compose
from isserviceup.services.dnsimple import Dnsimple
from isserviceup.services.cloudflare import Cloudflare
from isserviceup.services.digitalocean import DigitalOcean
from isserviceup.services.linode import Linode
from isserviceup.services.gcloud import GCloud
from isserviceup.services.heroku import Heroku
from isserviceup.services.pingdom import Pingdom
from isserviceup.services.redislabs import RedisLabs
from isserviceup.services.sentry import Sentry
from isserviceup.services.github import GitHub
from isserviceup.services.travis import Travis
from isserviceup.services.twillio import Twillio
from isserviceup.services.sendgrid import SendGrid
from isserviceup.services.sparkpost import SparkPost
from isserviceup.services.stormpath import StormPath
from isserviceup.services.datadog import DataDog
from isserviceup.services.statuspage import StatusPage
from isserviceup.services.rollbar import RollBar
from isserviceup.services.quay import Quay
from isserviceup.services.gotomeeting import GotoMeeting
from isserviceup.services.pagerduty import PagerDuty
from isserviceup.services.victorops import VictorOps
from isserviceup.services.duo import Duo
from isserviceup.services.pingidentity import PingIdentity
from isserviceup.services.disqus import Disqus
from isserviceup.services.bitbucket import BitBucket
from isserviceup.services.packagecloud import PackageCloud
from isserviceup.services.fastly import Fastly
from isserviceup.services.dyn import Dyn
from isserviceup.services.sendwithus import SendWithUs
from isserviceup.services.authorizedotnet import AuthorizeDotNet
from isserviceup.services.hashicorp import HashiCorp
from isserviceup.services.npm import NPM
from isserviceup.services.pypi import PythonInfra
from isserviceup.services.maxcdn import MaxCDN
from isserviceup.services.mailgun import MailGun
from isserviceup.services.loggly import Loggly
from isserviceup.services.opbeat import OpBeat
from isserviceup.services.pusher import Pusher
from isserviceup.services.rubygems import RubyGems
from isserviceup.services.chargify import Chargify
from isserviceup.services.atlassian import Atlassian
from isserviceup.services.gocardless import GoCardless
from isserviceup.services.harvest import Harvest
from isserviceup.services.codeclimate import CodeClimate
from isserviceup.services.box import Box
from isserviceup.services.dropbox import Dropbox
from isserviceup.services.codeship import CodeShip
from isserviceup.services.shotgun import Shotgun
from isserviceup.services.ftrack import FTrack
from isserviceup.services.newrelic import NewRelic

from isserviceup.notifiers.slack import Slack

DEBUG = config('DEBUG', cast=bool, default=False)
REDIS_URL = config('REDIS_URL', default='redis://redis:devpassword@redis')
STATUS_UPDATE_INTERVAL = config('STATUS_UPDATE_INTERVAL', cast=int, default=30)

SENTRY_DSN = config('SENTRY_DSN', default=None)

CELERY_EAGER = config('CELERY_EAGER', cast=bool, default=False)
CELERY_BROKER = config('CELERY_BROKER', default=REDIS_URL)
CELERY_BACKEND = config('CELERY_BACKEND', default=REDIS_URL)

SLACK_WEB_HOOK_URL = config('SLACK_WEB_HOOK_URL', default=None)

NOTIFIERS = [
    # Slack(SLACK_WEB_HOOK_URL)
]

SERVICES = [
    AWS(),
    GCloud(),
    GitHub(),
    Heroku(),
    RedisLabs(),
    Compose(),
    Sentry(),
    Pingdom(),
    Dnsimple(),
    Cloudflare(),
    Linode(),
    DigitalOcean(),
    Travis(),
    CircleCI(),
    Azure(),
    Twillio(),
    SendGrid(),
    SparkPost(),
    StormPath(),
    DataDog(),
    StatusPage(),
    RollBar(),
    Quay(),
    GotoMeeting(),
    PagerDuty(),
    VictorOps(),
    Duo(),
    PingIdentity(),
    Disqus(),
    BitBucket(),
    PackageCloud(),
    Fastly(),
    Dyn(),
    SendWithUs(),
    AuthorizeDotNet(),
    HashiCorp(),
    NPM(),
    PythonInfra(),
    MaxCDN(),
    MailGun(),
    Loggly(),
    OpBeat(),
    Pusher(),
    RubyGems(),
    Chargify(),
    Atlassian(),
    GoCardless(),
    Harvest(),
    CodeClimate(),
    Box(),
    Dropbox(),
    CodeShip(),
    Shotgun(),
    FTrack(),
    NewRelic(),
]
