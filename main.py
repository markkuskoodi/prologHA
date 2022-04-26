from webhook import Webhook
from rawdata import Data
from prolog_invoker import invoke_prolog
from rest_response.response import Response
from apscheduler.schedulers.background import BackgroundScheduler

# Token millega Webhook saab ennast Home-Assistantiga külge haakides ära authentida.
token = ""
hook = Webhook(token)
rest = Response(token)

# Loeme home-assistantist sisse kõik sensorid ja täiturid ning mapi need ära
data = Data(hook.get_states())

# Loome planeeria ning lisame planeeriasse invoke_prolog meetodi mida me jooksutame iga viie sekundi
# tagant. See on selleks, et anda natuke aega Prologil tööd teha.
scheduler = BackgroundScheduler()
scheduler.add_job(invoke_prolog, 'interval', args=[data, rest], seconds=5, max_instances=5)
scheduler.start()
#invoke_prolog(data, rest)
# Hakkame kuulama Home-Assistant's täiturite ning sensorite muudatusi
hook.subscribe_states()

try:
    while (True):
        # Kui muudatus tuleb, siis ta muudab mapis vastavat välja.
        data.update_data(hook.ws.recv())
        print("updated")
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()