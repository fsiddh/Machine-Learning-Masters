from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, ConversationState
from botbuilder.schema import Activity
import asyncio
from luis.luisApp import LuisConnect
import os
from logger.logger import Log

# Now we'll create instances of our classes
app = Flask(__name__)
loop = asyncio.get_event_loop()

bot_settings = BotFrameworkAdapterSettings("", "")
bot_adapter = BotFrameworkAdapter(bot_settings)

#CON_MEMORY = ConversationState(MemoryStorage())
luis_bot_dialog = LuisConnect

@app.route("/api/messages", methods = ["POST"])
def messages():
    if "application/jason" in request.headers["content-type"]:
        log = Log()
        request_body = request.jason

        # Activity is basically what user says and what we are sending as a response
        # they are termed as bot activity.
        # So the message exchange between the bot and the user is Activity
        user_says = Activity().deserialize(request_body)

        # Whatever user has said
        log.write_log(sessionID = "session1", log_message = "user says: "+str(user_says))
        authorization_header = (request.headers["Authorization"] if "Authorization" in request.headers else "")

        # Here the 2 new words async and await mean to make the code asyncronous
        # so that parts of our code doesn't wait for this piece of code to get executed!
        async def call_user_fun(turncontext):
            await luis_bot_dialog.turn_on(turncontext)

        task = loop.create_task(
            bot_adapter.process_activity(user_says, authorization_header, call_user_fun)
        )
        loop.run_until_complete(task)
        return ""
    else:
        return Response(status=406)  # status for Not Acceptable


if __name__ == '__main__':
    # app.run(port= 3978)
    app.run()

