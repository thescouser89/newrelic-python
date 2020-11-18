import app
import newrelic.agent

newrelic.agent.initialize()
application = app.app
