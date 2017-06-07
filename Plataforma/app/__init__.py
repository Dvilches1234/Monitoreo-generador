from flask import Flask, request

app = Flask(__name__, template_folder='template')
from app import views
