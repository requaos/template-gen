FROM python:3-buster as builder

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

COPY data /data

RUN python3 template.py

FROM scratch as final

COPY --from=builder /app/output.et .

# CMD ["python3", "template.py"]
