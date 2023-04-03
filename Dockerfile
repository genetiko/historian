# `base` sets up all shared environment variables.
FROM python:3.11-slim as base

    # Python.
ENV PYTHONUNBUFFERED=1 \
    # Prevents python creating .pyc files.
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # Pip.
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry.
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.4.0 \
    # Make poetry install to this location.
    POETRY_HOME="/opt/poetry" \
    # Make poetry create the virtual environment in the project's root.
    # It gets named `.venv`.
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # Do not ask any interactive question.
    POETRY_NO_INTERACTION=1 \
    \
    # Paths.
    # This is where requirements + virtual environment will live.
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Prepend poetry and venv to path.
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# `builder` stage is used to build deps + create virtual environment.
FROM base as builder
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # Deps for installing poetry.
        curl \
        # Deps for building python deps.
        build-essential

# Install poetry - respects $POETRY_VERSION & $POETRY_HOME.
RUN curl -sSL https://install.python-poetry.org | python -

# Copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY pyproject.toml ./

# Install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally.
RUN poetry install --only main

# `final` image used for runtime
FROM base as final
COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /historian
COPY ./historian ./historian
COPY settings.yaml ./
EXPOSE 80
CMD ["uvicorn", "historian.main:app", "--host", "0.0.0.0", "--port", "80"]
