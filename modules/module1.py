import discord
from discord.ext import commands

import pymysql
from dotenv import dotenv_values

config = dotenv_values(".env")

mysqlconnect = {
                "host": config['host'],
                "user": config['user'],
                "password": config['password'],
                "db": config['db'],
                "charset": config['charset'],
                "port":int(config['port'])
}

