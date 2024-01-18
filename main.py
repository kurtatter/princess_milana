import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types

import config


async def main():
    print(config.BOT_TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
