from database import connect, cursor
import os
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.methods.delete_webhook import DeleteWebhook
from aiogram import Router, F
from aiogram.filters import Command