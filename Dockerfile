FROM ruby:3.3

ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="CMU-CLeaR"

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    locales \
    imagemagick \
    build-essential \
    zlib1g-dev \
    inotify-tools \
    procps && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    JEKYLL_ENV=development

RUN mkdir -p /srv/jekyll

WORKDIR /srv/jekyll

# Copy dependency files first for layer caching
COPY Gemfile Gemfile.lock* ./

# Install bundler and gems
RUN gem install bundler && \
    bundle config set --local without 'development test' && \
    bundle install --jobs 4 --retry 3

EXPOSE 8080 35729

COPY bin/entry_point.sh /tmp/entry_point.sh
RUN chmod +x /tmp/entry_point.sh

CMD ["/tmp/entry_point.sh"]
