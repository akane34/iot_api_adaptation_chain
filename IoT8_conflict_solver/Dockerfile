FROM python:2-alpine

EXPOSE 5000

WORKDIR "/usr/src/app"

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV CONFLICT_SOLVER_PORT=5000 \
  CONFLICT_SOLVER_DATABASE='sqlite:///conflict_solver.db'

CMD python conflict_solver/main.py
