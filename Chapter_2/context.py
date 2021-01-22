from Chapter_2.hello import app
from flask import current_app

#print(current_app.ame)

app_ctx = app.app_context()  # приобретаем контекст приложения
app_ctx.push()
print(current_app.name)