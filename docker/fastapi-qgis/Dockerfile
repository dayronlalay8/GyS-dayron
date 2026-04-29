FROM qgis/qgis:ltr-noble

WORKDIR /app

ENV QT_QPA_PLATFORM=offscreen
ENV PYTHONPATH=/usr/share/qgis/python:/usr/share/qgis/python/plugins

COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages --ignore-installed -r requirements.txt

COPY src /app/src
COPY app.py /app/app.py

EXPOSE 8001

CMD ["fastapi", "run", "app.py", "--host", "0.0.0.0", "--port", "8001"]