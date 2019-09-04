#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime

months = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декября': '12'
}


def convert_date(date_str):
    date = date_str.split()
    date[1] = months[date[1]]
    date = ''.join(date)
    date = datetime.strptime(date, '%d%m%Y,%H:%M')
    return date
