FROM apache/airflow:2.10.5

ENV AIRFLOW_HOME=/opt/airflow

COPY . $AIRFLOW_HOME

RUN pip install --no-cache-dir -r $AIRFLOW_HOME/requirements.txt

WORKDIR $AIRFLOW_HOME

CMD ["airflow", "standalone"]
