from pelican import signals


def archive_dates(gen):
    uniq_dates = []
    dates = []
    for article in gen.articles:
        date_fmt = article.date.strftime("%Y/%m")
        if date_fmt not in uniq_dates:
            uniq_dates.append(date_fmt)
            dates.append({'url': date_fmt, 'string': article.date.strftime("%B %Y")})
    gen.context['archive_dates'] = dates


def register():
    signals.article_generator_finalized.connect(archive_dates)
