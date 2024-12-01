
FROM python:3.12-slim

RUN groupadd -r backstage \
    && useradd -r -g backstage -m backstage

RUN pip install uv


COPY pyproject.toml /backstage/
COPY .python-version /backstage/
COPY .env /backstage/
COPY uv.lock /backstage/
COPY ./migrations/ /backstage/migrations
COPY ./Backstage/ /backstage/Backstage

RUN chown -R backstage:backstage backstage

WORKDIR /backstage

ENV UV_PROJECT_ENVIRONMENT venv/
ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH"
USER backstage

RUN uv sync --locked


